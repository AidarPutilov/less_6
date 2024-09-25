
from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from users.models import User

from config.settings import EMAIL_HOST_USER


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("email", "password1", "password2")


class UserProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ("email", "phone", "country", "avatar")

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.fields['password'].widget = forms.HiddenInput()
