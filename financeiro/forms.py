from django import forms
from .models import Conta, Gasto

class ContaForm(forms.ModelForm):
    class Meta:
        model = Conta
        fields = '__all__'

class GastoForm(forms.ModelForm):
    class Meta:
        model = Gasto
        fields = '__all__'
