from django import forms
from django.contrib.auth.forms import UserCreationForm

from djangopro.base.models import User


class UserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ["first_name", "email", "password1", "password2"]

        # widgets = {
        #     'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Type'}),
        #     'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Insert your email'}),
        #     'password1': forms.TextInput(attrs={'class': 'form-control'}),
        #     'password2': forms.TextInput(attrs={'class': 'form-control'}),
        # }
