from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def home (request):

    return render (request,"home.html")

def login (request):
    if request.method == "POST":
       username = request.POST.get("username")
       password = request.POST.get("password")
       if User.objects.filter(username=username).exists():
        
           user = auth.authenticate(username=username, password=password)

           if user is not None :
              auth.login(request,user)
              return redirect("dashboard")

           else:
              return redirect("invalid")
    return render (request,"login.html")

def signup (request):
    if request.method=="POST":
        username = request.POST.get("username")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        password = request.POST.get("password")

        new_User = User.objects.create(username = username,first_name = first_name,last_name = last_name,email = email) 

        new_User.set_password(password)

        new_User.save()
        return redirect("dashboard")


    return render (request,"signup.html")
    
def dashboard (request):
    return render (request,"dashboard.html")
    
def invalid (request):
    return render (request,"invalid.html")
def footer (request):
    return render (request,"footer.html")
def myteam(request):
    return render (request,"myteam.html")
def offers(request):
    return render (request,"offers.html")
def header(request):
    return render (request,"header.html")
def recorded_sessions(request):
    return render (request,"recorded_sessions.html")

