
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages


# Create your views here.

def home(request):
    return render(request,'myapp/index.html')

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        myuser =User.objects.create_user(username,email,pass1)
        myuser.last_name = lname
        myuser.first_name = fname

        myuser.save()

        messages.success(request, "Your account is created")
        return redirect('/')
    
    return render(request, 'myapp/signup.html')


def signin(request):

    if request.method == "POST":
        username =request.POST['username']
        pass1 =request.POST['pass1']

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request,user)
            fname = user.first_name
            
            return render(request,"myapp/index.html",{'fname' :fname})
        
        else:
            messages.error(request,"SignUp first")
            return redirect('/')

    return render(request, "myapp/signin.html")

def signout(request):
    logout(request)
    messages.success(request, "Logged Out")
    return redirect('/')
