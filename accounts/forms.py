from django import forms
from django.contrib.auth.forms import (
    UserCreationForm, UserChangeForm
)
from .models import (
    User, 
)


class NewUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1']
       



class UpdateUserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email',]