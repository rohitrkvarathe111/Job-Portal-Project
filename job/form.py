from django import forms
from .models import Job

class CreateJobForm(forms.ModelForm):
    class Meta:
        model = Job
        exclude = ('user', 'company')



class UpdateJobForm(forms.ModelForm):
    class Meta:
        model = Job
        exclude = ('user', 'company')