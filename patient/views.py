
from django.shortcuts import render,HttpResponseRedirect
from django.contrib import messages
from patient.models import Feedback,Appointment
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

def appointment(request,id):
  if request.user.is_authenticated:
    if request.method == 'POST':
        da=UpdateForm.objects.get(pk=id)
        print(da)
        fname = request.POST.get("fullname")
        email = request.POST.get("email")
        mobile = request.POST.get("contact")
        message = request.POST.get("message")

        appointment = Appointment.objects.create(
            full_name=fname,
            email=email,
            contact=mobile,
            request=message,
            doctor_id=da
        )

        appointment.save()

        messages.add_message(request, messages.SUCCESS, f"Thanks {request.user} !! For making an appointment, we will email you ASAP!")
        return HttpResponseRedirect("/user/patient/")     
    else:    
        return render(request,'patient/appointment.html',{'username':request.user,'pk':id})
  else:
    return HttpResponseRedirect('/login/')    

    


       


# Create your views here.
