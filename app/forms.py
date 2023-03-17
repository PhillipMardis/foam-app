from django import forms
from app.models import *
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class postForm(forms.ModelForm):
    class Meta:
        model = postModel
        fields = "__all__"
        labels = {"desc": "Description", "cond": "Condition"}


class buyForm(forms.ModelForm):
    class Meta:
        model = buyModel
        fields = "__all__"
        labels = {"cond": "Condition", "price": "Price"}


class create_userForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
