from django.conf import settings
from django.shortcuts import render



def homepage(request):
    return render(request,'core/home.html')
def aboutpage(request):
    return render(request,'core/about2.html')
def gallerypage(request):
    return render(request,'core/gallery.html')
def contactpage(request):
    return render(request,'core/contact.html')            

# Create your views here.
