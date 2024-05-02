from django import forms
from .models import NumbEmail

class NumbEmailForm(forms.ModelForm):
    class Meta:
        model = NumbEmail
        fields = '__all__'