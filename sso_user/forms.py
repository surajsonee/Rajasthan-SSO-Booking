from django import forms
from .models import Sso_Register


class SsoRegisterPostForm(forms.ModelForm):
    sso_id = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': "form-control"}))
    class Meta:
        model = Sso_Register
        fields = (
            'sso_id',
            'password')