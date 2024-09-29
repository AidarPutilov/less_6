import random
import secrets
import string
from django.core.mail import send_mail
from django.db.models import QuerySet
from django.db.models.base import Model as Model
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView

from config.settings import EMAIL_HOST_USER
from users.forms import UserProfileForm, UserRegisterForm
from users.models import User


class UserCreateView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy("users:login")

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        user.token = secrets.token_hex(16)
        user.save()

        confirm_url = reverse('users:email-confirm', user.token)
        url = request.build_absolute_url(confirm_url)
        send_mail(
            subject="Подтверждение почты",
            message=f"Перейди по ссылке для подтверждения почты {url}",
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email],
        )
        return super().form_valid(form)


def email_verification(request, token):
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse("users:login"))


class ProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy("users:profile")

    def get_object(self, queryset=None) -> Model:
        return self.request.user


def password_reset(request):

    if request.method == "POST":
        email = request.POST.get("email")

        if not User.objects.filter(email=email).exists():
            # это чтобы яндекс не пытался отправить письмо на не существующий адрес
            return render(request, template_name="users/password_reset.html")
        else:
            user = get_object_or_404(User, email=email)
            new_password = User.objects.make_random_password()
            user.set_password(new_password)
            user.save()
            send_mail(
                subject=f"Сброс пароля",
                message=f"Ваш новый пароль: {new_password}",
                from_email=EMAIL_HOST_USER,
                recipient_list=[email],
            )
        return redirect(reverse("users:login"))

    return render(request, template_name="users/password_reset.html")
