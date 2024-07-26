from django.forms import forms
from django.contrib.auth.forms import UserCreationForm

from .models import CustomUser

class RegistrationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email' ,'date_of_birth']