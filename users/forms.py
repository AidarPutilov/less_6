from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from users.models import User


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("email", "password1", "password2")


class UserProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ("email", "phone", "country", "avatar")
