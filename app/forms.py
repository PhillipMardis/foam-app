from django import forms
from app.models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.contrib.auth.models import User, Group


class postForm(forms.ModelForm):
    class Meta:
        model = postModel
        exclude = ["user"]
        labels = {"desc": "Description", "cond": "Condition"}


class buyForm(forms.ModelForm):
    class Meta:
        model = buyModel
        fields = "__all__"
        labels = {"cond": "Condition", "price": "Price"}


class CreateUserForm(UserCreationForm):
    type = forms.ModelChoiceField(queryset=Group.objects.all())

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2", "type"]


class loginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ["username", "password"]
