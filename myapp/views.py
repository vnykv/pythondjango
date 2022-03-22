from pdb import post_mortem
from .models import users
from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return render(request,'index.html')

def home(request):
    return render(request,'home.html')

def samplepage(request):
    return render(request,'samplepage.html')

def signup(request):
    return render(request,'signup.html')


def newpage(request):
    if request.method =='POST':
        username=request.POST['user']
        password=request.POST['pass']
        age=request.POST['age']
        userdata=users(username=username,password=password,age=age)
        userdata.save()

    return render(request,'newpage.html')
     
    
