from django import forms
from app.models import *


class postForm(forms.ModelForm):
    class Meta:
        model = postModel
        fields = "__all__"
        labels = {"desc": "Description", "cond": "Condition"}


class buyForm(forms.ModelForm):
    class Meta:
        model = buyModel
        fields = "__all__"
        labels = {"browse_by": "Browse by"}
