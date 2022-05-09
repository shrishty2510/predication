from typing_extensions import Required
from django.db import models
from django.contrib.auth.models import User
User_choice = (
    ('Doctor','Doctor'),
    ('Patient','Patient'),
)
class RegistrationForm(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    user_type = models.CharField(max_length=20,choices=User_choice)
    #dateofbirth = models.DateField(auto_now=False,auto_now_add=False,blank=True)
    contact = models.PositiveIntegerField()
    address= models.CharField(max_length=400)
    profile_image = models.ImageField(upload_to='media/profileimg', blank=True)

    def __str__(self):
        return str(self.user)
    

Type_choice = (
    ('Physiatrist','Physiatrist'),
    ('Dermatologist','Dermatologist'),
    ('Pediatrician','Pediatrician'),
    ('Cardiologist','Cardiologist'),
    ('Nephrologist','Nephrologist'),
    ('Gynecologist','Gynecologist'),
    ('Pathologist','Pathologist'),
    ('Podiatrist','Podiatrist'),
    ('Family Physician','Family Physician'),
    ('Other','Other'),
)
class UpdateForm(models.Model):
    #user = models.OneToOneField(User,on_delete=models.CASCADE,default=None)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    age = models.PositiveIntegerField()
    specialist = models.CharField(max_length=200,choices=Type_choice)
    about= models.CharField(max_length=600,default=None)
    contact = models.PositiveIntegerField()
    address= models.CharField(max_length=400)
    image = models.ImageField(upload_to='media/image')    
    
   

# Create your models here.
