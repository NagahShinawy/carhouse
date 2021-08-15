from django.contrib.auth.forms import (
    AuthenticationForm as BaseAuthenticationForm,
    UsernameField,
)
from django.utils.translation import gettext_lazy as _

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError


class AuthenticationForm(BaseAuthenticationForm):
    username = UsernameField(
        widget=forms.TextInput(attrs={"autofocus": True, "placeholder": _("Username")})
    )
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"placeholder": _("Password")}),
    )

    error_messages = {
        "invalid_login": _("Invalid username/password."),
        "inactive": _("Invalid username/password."),
    }

    def get_invalid_login_error(self):
        return forms.ValidationError(
            {"password": self.error_messages["invalid_login"]},
            code="invalid_login",
            params={"username": self.username_field.verbose_name},
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # redefined according to user story
        self.fields["username"].error_messages = {"required": _("Enter Username")}
        self.fields["password"].error_messages = {"required": _("Enter Password")}


class UserSignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=200)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)

    def clean(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("Email already exists")
        return self.cleaned_data
