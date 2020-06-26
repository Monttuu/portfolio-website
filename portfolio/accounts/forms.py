from django.contrib.auth import get_user_model
from django.contrib.auth.forms import (UserCreationForm, AuthenticationForm,
                                       UserChangeForm, PasswordChangeForm)
from django import forms

class UserCreateForm(UserCreationForm):
    username = forms.CharField(max_length=254, label='',
                               widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password1 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Password Again'}))
    email = forms.EmailField(max_length=254, label='',
                               widget=forms.EmailInput(attrs={'placeholder': 'Email'}))

    class Meta:
        fields = ("username", "email", "password1", "password2")
        model = get_user_model()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #self.fields["username"].label = "Display name"
        #self.fields["email"].label = "Email address"

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(max_length=254,label='',
                               widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    class Meta:
        fields = ("username", "password")
        model = get_user_model()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #self.fields["username"].label = "Display name"
        #self.fields["password"].label = "Password"