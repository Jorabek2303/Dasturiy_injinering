from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','last_name','password','password2']
        
class ProfileForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = ['name','user_email','user_image','finger_image']