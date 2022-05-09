from django.db import models
from doctor.models import UpdateForm

class Feedback(models.Model):
    username=models.CharField(max_length=200,default='unknown',blank=True)
    message=models.TextField(default='no feedback',blank=True)

class Appointment(models.Model):
    full_name = models.CharField(max_length=150)
    email = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    request = models.TextField(blank=True)
    sent_date = models.DateField(auto_now_add=True)
    accepted = models.BooleanField(default=False)
    accepted_date = models.DateField(auto_now_add=False, null=True, blank=True)
    doctor_id = models.ForeignKey(UpdateForm,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.full_name
    
    class Meta:
        ordering = ["-sent_date"]    
class Symptom_Precaution(models.Model):
    Disease=models.CharField(max_length=255)
    Precaution_1=models.CharField(max_length=255)
    Precaution_2=models.CharField(max_length=255)			
    Precaution_3=models.CharField(max_length=255)
    Precaution_4=models.CharField(max_length=255)

class Symptom_Description(models.Model):
    Disease=models.CharField(max_length=255)
    Description=models.CharField(max_length=400)        

# Create your models here.
