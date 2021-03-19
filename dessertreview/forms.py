from django.cotrib.auth.models import User
from dessertreview.models import UserProfile, Review
from django import forms

# New user form

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
    model = User
    fields = ('username', 'email', 'password',)

#  Login form
class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password',)