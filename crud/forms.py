# forms.py
from django import forms
from .models import Crud

class ProductForm(forms.ModelForm):
    class Meta:
        model = Crud
        fields = '__all__'
