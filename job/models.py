from django.db import models
from company.models import Company
from users.models import User
from resume.models import Resume

# Create your models here.

class State(models.Model):
    name = models.CharField(max_length=70)

    def __str__(self):
        return self.name

class Industry(models.Model):
    name = models.CharField(max_length=80)
    def __str__(self):
        return self.name










class Job(models.Model):
    job_type_choices = (
        ('Remote', 'Remote'),
        ('Onsite', 'Onsite'),
        ('hybrid', 'hybrid')
        
    )


    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    salary = models.PositiveIntegerField(default=40000)
    requirements = models.TextField()
    ideal_candidate = models.TextField()
    is_available = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    industry = models.ForeignKey(Industry, on_delete=models.DO_NOTHING, null=True, blank=True)
    state = models.ForeignKey(State, on_delete=models.DO_NOTHING, null=True, blank=True)
    job_type = models.CharField(max_length=30, choices=job_type_choices, null=True, blank=True)


    def __str__(self):
        return self.title
    






class ApplyJob(models.Model):
    status_choices = (
        ('Accepted', 'Accepted'),
        ('Declined', 'Declined'),
        ('Pending', 'Pending')
    )


    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=30, choices=status_choices)
  












