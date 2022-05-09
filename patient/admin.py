import imp
from django.contrib import admin
from . models import Appointment, Feedback,Symptom_Description,Symptom_Precaution


@admin.register(Appointment)
class Useradmin(admin.ModelAdmin):
    list_display = ['id','full_name','email','contact','sent_date','request','accepted','accepted_date','doctor_id']

@admin.register(Feedback)
class Useradmin(admin.ModelAdmin):
    list_display = ['username','message']

@admin.register(Symptom_Precaution)
class Useradmin(admin.ModelAdmin):
    list_display = ['id','Disease','Precaution_1','Precaution_2','Precaution_3','Precaution_4']

@admin.register(Symptom_Description)
class Useradmin(admin.ModelAdmin):
    list_display = ['id','Disease','Description']    


# Register your models here.
