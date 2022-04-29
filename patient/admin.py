import imp
from django.contrib import admin
from . models import Feedback

@admin.register(Feedback)
class Useradmin(admin.ModelAdmin):
    list_display = ['username','message']

# Register your models here.
