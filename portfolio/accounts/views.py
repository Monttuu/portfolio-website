from django.shortcuts import render

# Create your views here.

from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth import (
    REDIRECT_FIELD_NAME, get_user_model, login as auth_login,
    logout as auth_logout, update_session_auth_hash,
)
from django.shortcuts import redirect

from . import forms

class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy("login")
    template_name = "accounts/signup.html"

class CustomLoginView(LoginView):
    """
    Custom login view.
    """

    form_class = forms.UserLoginForm
    template_name = 'login.html'

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated and self.request.user.is_staff and has_2fa(self.request):
            return redirect('{}'.format(self.request.GET.get('next', 'portal_home')))

        return super(CustomLoginView, self).get(request, *args, **kwargs)

    def form_valid(self, form):

        if self.request.user.is_staff and not has_2fa(self.request):
            #logger.info('is staff but does not have 2FA, redirecting to Authy account creator')
            auth_login(self.request, form.get_user(), backend='django.contrib.auth.backends.ModelBackend')
            return redirect('2fa_register')

        return super(CustomLoginView, self).form_valid(form)