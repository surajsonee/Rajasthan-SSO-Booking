from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

class UserLoginForm(forms.Form):
    username_or_email = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': "form-control"}))

class UserRegistrationForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password Confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            message = "Passwords do not match"
            raise ValidationError(message)

        return password2

    def save(self, commit=True):
        instance = super(UserRegistrationForm, self).save(commit=False)

        if commit:
            instance.save()

        return instance
    
class changePassForm(forms.Form):
    old_password_flag = True #Used to raise the validation error when it is set to False
    old_password = forms.CharField(label="Old Password", min_length=6, widget=forms.PasswordInput())
    new_password = forms.CharField(label="New Password", min_length=6, widget=forms.PasswordInput())
    re_new_password = forms.CharField(label="Re-type New Password", min_length=6, widget=forms.PasswordInput())

def set_old_password_flag(self): 

#This method is called if the old password entered by user does not match the password in the database, which sets the flag to False

    self.old_password_flag = False

    return 0

def clean_old_password(self, *args, **kwargs):
    old_password = self.cleaned_data.get('old_password')

    if not old_password:
        raise forms.ValidationError("You must enter your old password.")

    if self.old_password_flag == False:
    #It raise the validation error that password entered by user does not match the actucal old password.

        raise forms.ValidationError("The old password that you have entered is wrong.")

    return old_password