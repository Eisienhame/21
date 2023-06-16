from audioop import reverse

from django.views.generic import UpdateView, CreateView
from django.contrib.auth.views import PasswordResetView
from project import settings
from users.models import User
from django.urls import reverse_lazy
from users.forms import UserForm, UserRegisterForm
from users.services import confirm_account
from django.shortcuts import redirect, render
from django.contrib.auth.base_user import BaseUserManager
from django.core.mail import send_mail


class ProfileUpdateView(UpdateView):

    model = User
    form_class = UserForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user


class RegisterView(CreateView):

    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('catalog:homepage')

    def form_valid(self, form):
        self.object = form.save()
        self.object.is_active = False
        confirm_account(self.object)
        self.object.save()
        return super().form_valid(form)

    # def get_success_url(self):
    #     url_1 = super().get_success_url()
    #     return str(url_1) + str(self.object.email)


def activate_user(request, email):

    user = User.objects.filter(email=email).first()
    user.is_active = True
    user.save()
    return redirect('users:login')


def generate_pass(request, email):
    new_pass = BaseUserManager.make_random_password()
    user = User.objects.filter(email=email).first()
    send_mail(
        subject='Восстановление пароля',
        message=f'Ваш новый пароль {new_pass}',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user.email]
    )
    user.set_password(new_pass)
    user.save()
    return redirect(reverse('users:login'))

