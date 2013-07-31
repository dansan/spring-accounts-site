# This file is part of the "spring accounts site / sas" program. It is published
# under the GPLv3.
#
# Copyright (C) 2012 Daniel Troeder (daniel #at# admin-box #dot# com)
#
#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <http://www.gnu.org/licenses/>.

from django import forms

class SpringPlayerLoginForm(forms.Form):
    splf_username = forms.CharField(label="Username", max_length=30, widget=forms.TextInput(attrs={"class": "span12 spraddform1"}))
    splf_password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={"class": "span12 spraddform2"}))
