from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.TextField()
    massage = models.TextField()

    def __str__(self):
        return self.name


