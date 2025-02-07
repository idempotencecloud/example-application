# app/forms.py
from django import forms
from .models import Company, Individual

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = '__all__'
        widgets = {
            'company_type': forms.Select,
        }

class IndividualForm(forms.ModelForm):
    class Meta:
        model = Individual
        fields = '__all__'
        widgets = {
            'company': forms.Select,
            'interested_in_marketing_email': forms.CheckboxInput,
        }
