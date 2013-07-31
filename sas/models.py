# This file is part of the "spring accounts site / sas" program. It is published
# under the GPLv3.
#
# Copyright (C) 2012 Daniel Troeder (daniel #at# admin-box #dot# com)
#
#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <http://www.gnu.org/licenses/>.

from django.db import models
from django.contrib.auth.models import User

class SpringAccount(models.Model):
    name      = models.CharField(max_length=256)
    user      = models.ForeignKey(User)
    accountid = models.IntegerField(unique=True)
    timerank  = models.IntegerField()
    aliases   = models.CharField(max_length=2048, blank=True)
    country   = models.CharField(max_length=2)
    added     = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return "(%d) %s (#%d) [user: %s]"%(self.id, self.name, self.accountid, self.user)
