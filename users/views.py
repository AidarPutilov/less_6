from django.db.models import QuerySet
from django.db.models.base import Model as Model
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from users.forms import UserProfileForm, UserRegisterForm
from users.models import User

class UserCreateView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')


class ProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset = None) -> Model:
        return self.request.user