from django import forms
from .models import Resume

class UpdateResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        exclude = ('user',)