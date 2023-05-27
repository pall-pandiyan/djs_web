from django.shortcuts import render, resolve_url
from django.contrib.auth.views import LoginView, LogoutView

from . import forms


class Login(LoginView):
    template_name = "accounts/login.html"

    def get_default_redirect_url(self):
        if self.next_page:
            return resolve_url(self.next_page)
        else:
            return resolve_url("/")


class Logout(LogoutView):
    template_name = "accounts/logout.html"


def login_view(request):
    form = forms.LoginForm().render("form_snipet.html")
    return render(
        request=request,
        template_name="accounts/login.html",
        context={'form': form}
    )
