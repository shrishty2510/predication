from django.urls import path
from . import views

urlpatterns = [
    path('patient/',views.patient_dashboard,name='patient'),
    path('feedback_form/',views.feedback,name='feedback'),
     path('doctor_list/',views.doctorlist,name='doctorlist'),
]
