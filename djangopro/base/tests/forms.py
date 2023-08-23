from django import forms
from djangopro.base.models import UserModified


class UserForm(forms.ModelForm):
    class Meta:
        model = UserModified
        fields = ["first_name", "email", "password"]
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Insert your email'}),
            'password': forms.TextInput(attrs={'class': 'form-control'}),
        }
