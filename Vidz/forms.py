from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class CreateUserForm(UserCreationForm):
     class Meta:
         model = User
         fields = ['username','email','password1','password2']


class VideoForm(ModelForm):
    class Meta:
        model = Video
        fields = '__all__'