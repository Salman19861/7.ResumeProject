from django.shortcuts import render
from django.template import context

# Create your views here.
def base(request):
    return render(request,'base.html')
def home(request):
    context={'home':'active'}
    return render(request,'home.html',context)

def services(request):
    context={'services':'active'}
    return render(request,'services.html',context)
def about(request):
    context={'about':'active'}
    return render(request,'about.html',context)
def contact(request):
    context={'contact':'active'}
    return render(request,'contact.html',context)