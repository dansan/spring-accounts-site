# This file is part of the "spring accounts site / sas" program. It is published
# under the GPLv3.
#
# Copyright (C) 2012 Daniel Troeder (daniel #at# admin-box #dot# com)
#
#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <http://www.gnu.org/licenses/>.

from django.utils.html import escape
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.http import Http404
import django.contrib.auth
from django.core.urlresolvers import reverse

from models import SpringAccount
from forms import SpringPlayerLoginForm

from suds.client import Client

import logging
logger = logging.getLogger(__package__)

@login_required
def home(request):
    c = {
        'playeraccounts': SpringAccount.objects.filter(
            user=request.user
        ).order_by("-id")
    }

    return render_to_response("home.html", c, context_instance=RequestContext(request))

def next_works(request):
    return HttpResponse('?next= bit works. <a href="/">Home</a>')

def logout_view(request):
    django.contrib.auth.logout(request)
    return HttpResponseRedirect(reverse(home))

def ajax_modal_add_player(request):
    c = dict()
    if request.method == 'POST':
        form = SpringPlayerLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("splf_username")
            password = form.cleaned_data.get("splf_password")
            if username and password:
                url = 'http://zero-k.info/ContentService.asmx?WSDL'
                try:
                    client = Client(url)
                    accountinfo = client.service.GetAccountInfo(username, password)
                    logger.debug("accountinfo returned by soap for '%s': '%s'", username, accountinfo)              
                    if accountinfo:
                        sa, created = SpringAccount.objects.get_or_create(accountid=accountinfo.LobbyID,
                                                                          defaults={"name": accountinfo.Name,
                                                                                    "user": request.user,
                                                                                    "accountid": accountinfo.LobbyID,
                                                                                    "timerank": accountinfo.LobbyTimeRank,
                                                                                    "country": accountinfo.Country})
                        if hasattr(accountinfo,  "Aliases"):
                            sa.aliases = accountinfo.Aliases
                            sa.save()
                        if created:
                            logger.info("Created SpringAccount(%d): %s", sa.id, sa)
                            c["success"] = sa
                        else:
                            logger.error("SpringAccount(%d): %s already registered by User(%d): %s", sa.id, sa, sa.user.id, sa.user)
                            if sa.user == request.user:
                                form._errors = {'splf_username': [u"Account already registered by you."]}
                            else:
                                form._errors = {'splf_username': [u"Account already registered by another user."]}
                    else:
                        logger.info("Wrong username/password.")
                        form._errors = {'splf_username': [u"Wrong username/password."]}
                except Exception, e:
                    logger.error("Exception while using SOAP to check username/password: %s", e)
                    form._errors = {'splf_username': [u"There was a technical problem. Please retry later or contact the administrator ('dansan' on springrts.com forums)."]}
            else:
                logger.info("Missing username/password.")
                form._errors = {'splf_username': [u"Missing username/password."]}
    else:
        form = SpringPlayerLoginForm()
    c["spp_form"] = form

    return render_to_response("ajax_modal_add_player.html", c, context_instance=RequestContext(request))

# change_per_player_account_password
# change_ranking_privacy_setting
# get_per_player_ingame_time
# get_per_player_lobbyrank
# link_to_replays/(per)player/
