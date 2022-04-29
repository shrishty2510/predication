"""health_prediction_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from doctor import views
from django.conf import settings
from django.conf.urls.static import static

from django.views.static import serve
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('core/',include('core.urls')),
    path('user/',include('patient.urls')),
    path('register/',views.sign_up,name='SignUp'),
    path('login/',views.loginform,name='login'),
    path('logout/',views.logoutform,name='logout'),
    path('doctor/',views.doctorpage,name='doctor'),
    path('patient_list/',views.patient_list,name='patientlist'),
    path('update_details/',views.updatedetails,name='updatedetails'),
    path('change_password/',views.user_change_password,name='changepasslog'),
    path('changePassword/',views.user_change_password_with,name='changepasspro'),
    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

