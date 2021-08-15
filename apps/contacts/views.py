from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth import authenticate, login
from django.views.generic import CreateView
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib import messages
from apps.contacts.forms.auth import UserSignUpForm


class ContactusView(TemplateView):
    template_name = "contacts/contact-us.html"


class SignUpView(CreateView):
    template_name = "contacts/signup.html"
    form_class = UserSignUpForm

    def get_success_url(self):
        return reverse("cars:index")

    def form_valid(self, form):
        # form already valid
        form.save()
        username = self.request.POST.get('username')
        password = self.request.POST.get('password1')
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return redirect("cars:index")


class LoginView(BaseLoginView):
    template_name = "contacts/login.html"

    def form_valid(self, form):
        messages.success(self.request, "Login Successfully")
        return super().form_valid(form)


class LogoutView(BaseLogoutView):
    def get_next_page(self):
        return reverse("cars:index")


class DashboardView(TemplateView):
    template_name = "contacts/dashboard.html"
