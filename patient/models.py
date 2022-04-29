from django.db import models

class Feedback(models.Model):
    username=models.CharField(max_length=200,default='unknown',blank=True)
    message=models.TextField(default='no feedback',blank=True)

# Create your models here.
