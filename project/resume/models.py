from django.db import models

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    mobile = models.CharField(max_length=100)
    school = models.CharField(max_length=200)
    degree = models.TextField(max_length=200)
    university = models.CharField(max_length=200)
    skills = models.TextField(max_length=500)
    about_you = models.CharField(max_length=1000)
    previous_job = models.CharField(max_length=400)
