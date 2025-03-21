from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import HttpResponseRedirect, redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView
from django.views.generic.base import TemplateView
from django.contrib.auth import get_user_model
from . forms import UserRegistrationForm, UserLoginForm, ProfileForm
from .models import  User, EmailVerification
from django.contrib.auth.hashers import make_password
class TitleMixin:
    title = None

    def get_context_data(self, **kwargs):
        context = super(TitleMixin, self).get_context_data(**kwargs)
        context['title'] = self.title
        return context

User = get_user_model()


class UserCreationView(TitleMixin, SuccessMessageMixin, CreateView):
    model = User
    template_name = "users/signup.html"
    form_class = UserRegistrationForm
    success_url = reverse_lazy("users:login")
    success_message = "Congratulations, You successfully registered!"
    title = "Store - Registration"

    def form_valid(self, form):
        print("Form is valid!")  # Проверяем, срабатывает ли метод
        return super().form_valid(form)

    def form_invalid(self, form):
        print("🚨 FORM ERRORS:", form.errors)  # Выведет ошибки формы в консоль
        print("📦 POST DATA:", self.request.POST)  # Покажет, какие данные пришли
        return super().form_invalid(form)



class UserLoginView(LoginView):
    template_name = "users/login.html"
    form_class = UserLoginForm
    redirect_authenticated_user = True
    next_page = reverse_lazy("booking:index")


def logout(request):
    auth.logout(request)
    return redirect("booking:index")


class EmailVerificationView(TitleMixin, TemplateView):
    title = "Store - Confirm the email"
    template_name = "users/email_verification.html"

    def get(self, request, *args, **kwargs):
        code = kwargs['code']
        user = User.objects.get(email=kwargs['email'])
        email_verifications = EmailVerification.objects.filter(user=user, code=code)
        if email_verifications.exists() and not email_verifications.first().is_expired():
            user.is_verified = True
            user.save()
            return super(EmailVerificationView, self).get(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(reverse('products:index'))


class UserProfileView(UpdateView):
    model = User
    template_name = 'users/profile.html'
    form_class = ProfileForm

    def form_valid(self, form):
        user = form.instance

        # Удаление изображения, если отмечен чекбокс
        if form.cleaned_data.get("delete_image"):
            user.image.delete(save=False)
            user.image = None

        # Если введен новый пароль → хешируем его
        new_password = form.cleaned_data.get("password")
        if new_password:
            user.password = make_password(new_password)

        user.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("users:profile", args=(self.object.id,))



def base(request):
    return render(request, "users/base.html")