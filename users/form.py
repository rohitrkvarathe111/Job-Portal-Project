from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


class RegisterUserForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ['email', 'password1', 'password2']




#############################################################################3

from django.contrib.auth.forms import PasswordResetForm

class CustomPasswordResetForm(PasswordResetForm):
    class Meta:
        model = get_user_model()  
        fields = ['email']  


###############################################################################

# users/forms.py
from django import forms
from django.contrib.auth.forms import SetPasswordForm

class CustomSetPasswordForm(SetPasswordForm):
    class Meta:
        widgets = {
            'new_password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'new_password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }




















