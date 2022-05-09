from django.contrib import admin
from django.contrib import admin

from . models import RegistrationForm, UpdateForm

@admin.register(RegistrationForm)
class User(admin.ModelAdmin):
    list_display = ['id','user','user_type','contact','address','profile_image']

@admin.register(UpdateForm)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id','user','age','specialist','about','contact','address','image']    

# class UserAdmin(admin.ModelAdmin):
#     pass
# admin.site.register(RegistrationForm,UserAdmin)


# Register your models here.
