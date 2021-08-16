from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth import authenticate, login
from django.views.generic import CreateView
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib import messages
from apps.contacts.forms.auth import UserSignUpForm
from apps.core.constants import messages as msg


class ContactusView(TemplateView):
    template_name = "contacts/contact-us.html"


class SignUpView(CreateView):
    template_name = "contacts/signup.html"
    form_class = UserSignUpForm

    def get_success_url(self):
        return reverse("cars:index")

    @staticmethod
    def from_errorlist_to_str(form):
        return "<br>".join([v[0] for v in form.errors.values()])

    def form_invalid(self, form):
        # form has error(s)
        errors = self.from_errorlist_to_str(form)
        messages.error(self.request, errors)
        return super().form_invalid(form)

    def form_valid(self, form):
        # form already valid
        form.save()
        username = self.request.POST.get("username")
        password = self.request.POST.get("password1")
        user = authenticate(username=username, password=password)
        login(self.request, user)
        messages.success(self.request, msg.SIGNUP_SUCCESS)
        return redirect("cars:index")


class LoginView(BaseLoginView):
    template_name = "contacts/login.html"

    def form_invalid(self, form):
        messages.error(self.request, msg.LOGIN_FAILED)
        return super().form_invalid(form)

    def form_valid(self, form):
        messages.success(self.request, msg.LOGIN_SUCCESS)
        return super().form_valid(form)


class LogoutView(BaseLogoutView):
    def get_next_page(self):
        messages.success(self.request, msg.LOGOUT_SUCCESS)
        return reverse("cars:index")


class DashboardView(TemplateView):
    template_name = "contacts/dashboard.html"
