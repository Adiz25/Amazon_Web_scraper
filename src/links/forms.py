from  django import forms
from .models import Link
from django.http import HttpRequest

class AddLinkForm(forms.ModelForm):
    class Meta:
        model = Link
        fields  = ('url', )

