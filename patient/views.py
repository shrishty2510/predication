
from django.shortcuts import render,HttpResponseRedirect
from django.contrib import messages
from patient.models import Feedback
from doctor.models import UpdateForm

def patient_dashboard(request):
    if request.user.is_authenticated:
        return render(request,'patient/patient.html',{'username':request.user})
    else:
        return HttpResponseRedirect('/login/')     

def feedback(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            user=request.POST['username']
            feedback=request.POST['message']
            us=Feedback(username=user,message=feedback)
            us.save()
            messages.success(request,'Send Successfully!!')
            return HttpResponseRedirect('/user/feedback_form/')
        else:    
            return render(request,'patient/feedback.html',{'username':request.user})
    else:
        return HttpResponseRedirect('/login/')    

def doctorlist(request):
    if request.user.is_authenticated:
        fm= UpdateForm.objects.all()
        return render(request,'patient/doctorlist.html',{'username':request.user,'fm':fm})
    else:
        return HttpResponseRedirect('/login/')     




# Create your views here.
