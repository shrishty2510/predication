from django.shortcuts import render,HttpResponseRedirect
from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.models import User
from . models import RegistrationForm,UpdateForm
from . forms import login_form

def doctorpage(request):
    if request.user.is_authenticated:
       return render(request,'doctor/dr.dashboard.html',{'username':request.user})
    else:
        return HttpResponseRedirect('/login/')   


def sign_up(request):
    if request.method == 'POST':
        user = request.POST['username']
        fname = request.POST['first_name']
        lname = request.POST['last_name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        User_type = request.POST['user_type']
        address = request.POST['address']
        image = request.FILES['profile_image']
        contact=request.POST['contact']
        #dob = request.POST.get('dob',False)
        if password1 != password2:
            messages.error(request,"password does not matched!")  
            return redirect('/register/')
        elif User.objects.filter(username = user).first():
            messages.error(request, "This username is already taken")
            return redirect('/register/')
        else:    
            user1 = User.objects.create_user(user, email, password1)
            user1.first_name=fname
            user1.last_name=lname
            user1.save()
            user = User.objects.get(username=user)
            print(user)
            us2 = RegistrationForm(user=user,user_type=User_type, profile_image=image, address=address,contact=contact,)
            print(user)
            us2.save()
            return render(request,'doctor/loginform.html',{'usertype':User_type})
    return render(request,'doctor/Registration_form.html')

        
def loginform(request):
    if request.method == 'POST':
            uname=request.POST['username']
            upass=request.POST['password']
            user = authenticate(username=uname,password=upass)
            if user is not None:
                login(request,user)
                User=RegistrationForm.objects.get(user=user)
                if User.user_type == 'Doctor':
                   return HttpResponseRedirect('/doctor/')
                else:
                   return HttpResponseRedirect('/user/patient/')    
            else :
                 messages.error(request, "Please check your username and password!!")
                 return redirect('/login/')

    else:        
        fr = login_form()
    return render(request,'doctor/loginform.html',{'form':fr})  

def user_change_password(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
          fm=SetPasswordForm(user=request.user,data=request.POST)
          if fm.is_valid():
            fm.save()
            update_session_auth_hash(request,fm.user)
            messages.success(request,'Password change successfully!!')
            return HttpResponseRedirect('/login/')
        else:        
           fm=SetPasswordForm(user=request.user)
           print(request.user)
        return render(request,'doctor/changepasslogin.html',{'form':fm})
    else:
         return HttpResponseRedirect('/') 
#with old password         
def user_change_password_with(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
          fm=PasswordChangeForm(user=request.user,data=request.POST)
          if fm.is_valid():
            fm.save()
            update_session_auth_hash(request,fm.user)
            messages.success(request,'Password change successfully!!')
            return HttpResponseRedirect('/login/')
        else:        
           fm=PasswordChangeForm(user=request.user)
           print(request.user)
        return render(request,'doctor/changepassword.html',{'form':fm,'username':request.user})
    else:
         return HttpResponseRedirect('/')           


def logoutform(request):
    logout(request)
    return HttpResponseRedirect('/core/')   

def profilepage(request):
    if request.user.is_authenticated:
            us = User.objects.get(username = request.user)
            us1 = RegistrationForm.objects.get(user= request.user)
            #form=Postform()
            #return render(request,'core/profile.html',{'user':us,'detail':us1,'pform':form})              
    else:        
        return redirect('/login/') 

def userprofilepage(request):
    if request.user.is_authenticated:
            us = User.objects.get(username = request.user)
            us1 = RegistrationForm.objects.get(user= request.user)
            return render(request,'core/userprofile.html',{'user':us,'detail':us1,})              
    else:        
        return redirect('/login/')       

def patient_list(request):
    if request.user.is_authenticated:
        patient=RegistrationForm.objects.filter(user_type='Patient')
        return render(request,'doctor/patientlist.html',{'patient':patient,'username':request.user})
    else:
        return HttpResponseRedirect('/login/')               
             
def updatedetails(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            age=request.POST['age']
            Type=request.POST['Type']
            about=request.POST['about']
            visiting=request.POST['address']
            contact=request.POST['contact']
            profile=request.FILES['image']
            us2 = UpdateForm(user=request.user,image=profile, address=visiting,age=age,contact=contact,about=about,specialist=Type)
            us2.save()
            messages.success(request,'Updated successfully!!')
            return HttpResponseRedirect('/doctor/')
        else:    
            return render(request,'doctor/updatedetails.html',{'username':request.user})
    else:
        return HttpResponseRedirect('/login/')               
                          
         
                 
           

        

  

              


# Create your views here.
