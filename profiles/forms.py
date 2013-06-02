from django.contrib.auth.forms import PasswordChangeForm
from django.utils.translation import ugettext_lazy as _

from userena.forms import SignupForm, AuthenticationForm, ChangeEmailForm
from userena.contrib.umessages.forms import ComposeForm
from userena.utils import get_profile_model

from bootstrap.forms import * #BootstrapMixin, BootstrapModelForm

USERNAME_RE = r'^\S+$'
attrs_dict = {'class': 'required'}

class BsSignupForm(SignupForm, BootstrapMixin):
    username = forms.RegexField(regex=USERNAME_RE,
                                    max_length=30,
                                    widget=forms.TextInput(attrs=attrs_dict),
                                    label=_("Username"),
                                     error_messages={'invalid': _('Username must contain only letters, numbers, dots and underscores.')})
    def __init__(self, *args, **kw):
        super(BsSignupForm, self).__init__(*args, **kw)
        self.__bootstrap__()

class BsAuthenticationForm(AuthenticationForm, BootstrapMixin):

    def __init__(self, *args, **kw):
        super(BsAuthenticationForm, self).__init__(*args, **kw)
        self.__bootstrap__()

    class Meta:
        custom_fields = {'remember_me': 'profiles/field_remember_me.html'}

class BsPasswordChangeForm(PasswordChangeForm, BootstrapMixin):

    def __init__(self, *args, **kw):
        super(BsPasswordChangeForm, self).__init__(*args, **kw)
        self.__bootstrap__()

class BsChangeEmailForm(ChangeEmailForm, BootstrapMixin):

    def __init__(self, *args, **kw):
        print "------------xxx"
        super(BsChangeEmailForm, self).__init__(*args, **kw)
        self.__bootstrap__()

class BsEditProfileForm(BootstrapModelForm):

    class Meta:
        model = get_profile_model()
        exclude = ['user']

    def save(self, force_insert=False, force_update=False, commit=True):
        profile = super(BsEditProfileForm, self).save(commit=commit)
        user = profile.user
        user.save()
        return profile

class BsComposeForm(ComposeForm, BootstrapMixin):

    def __init__(self, *args, **kw):
        super(BsComposeForm, self).__init__(*args, **kw)
        self.__bootstrap__()
