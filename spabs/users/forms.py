from allauth.account.forms import SignupForm
from allauth.socialaccount.forms import SignupForm as SocialSignupForm
from django.contrib.auth import forms as admin_forms
from django.forms import EmailField
from django import forms
from django.utils.translation import gettext_lazy as _

from .models import User, JobEnrollment


class UserAdminChangeForm(admin_forms.UserChangeForm):
    class Meta(admin_forms.UserChangeForm.Meta):  # type: ignore[name-defined]
        model = User
        field_classes = {"email": EmailField}


class UserAdminCreationForm(admin_forms.UserCreationForm):
    """
    Form for User Creation in the Admin Area.
    To change user signup, see UserSignupForm and UserSocialSignupForm.
    """

    class Meta(admin_forms.UserCreationForm.Meta):  # type: ignore[name-defined]
        model = User
        fields = ("email",)
        field_classes = {"email": EmailField}
        error_messages = {
            "email": {"unique": _("This email has already been taken.")},
        }


class UserSignupForm(SignupForm):
    """
    Form that will be rendered on a user sign up section/screen.
    Default fields will be added automatically.
    Check UserSocialSignupForm for accounts created from social.
    """


class UserSocialSignupForm(SocialSignupForm):
    """
    Renders the form when user has signed up using social accounts.
    Default fields will be added automatically.
    See UserSignupForm otherwise.
    """


class JobEnrollmentForm(forms.ModelForm):
    date_of_birth = forms.DateField(
        widget=forms.TextInput(attrs={
            'class': 'form-control datepicker',
            'placeholder': 'Select a date'
        })
    )

    class Meta:
        model = JobEnrollment
        exclude = ['id', 'created_date', 'modified_date']


FORMAT_CHOICES = (
    ('xls', 'xls'),
    ('csv', 'csv'),
    ('json', 'json'),
)

class FormatForm(forms.Form):
    format = forms.ChoiceField(
        choices=FORMAT_CHOICES,
        # widget=forms.Select(attrs={'class':'form-select'})
    )
