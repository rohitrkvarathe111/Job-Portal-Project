from django import forms
from .models import Company


class UpdateCompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        exclude = ('user',)
