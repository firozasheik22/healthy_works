from django.http import request
from django.shortcuts import redirect, render
from django.contrib.auth.models import User,auth
# Create your views here.
from django.contrib import messages

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            print('login successful')
            return redirect('../quiz')
        else:
            print('!!invalid user')
            messages.info(request,'invalid user')
            return redirect('login')

    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def contact(request):
    return render(request,'contact.html')
def registration(request):

    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username taken')
                print('username taken')

                return redirect('registration')
            elif  User.objects.filter(email=email).exists():
                messages.info(request,'email taken')
                print('email tagen')

                return redirect('registration')
            else:
                user=User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                
                user.save()
                print('user created')
                return redirect('login')
                
        else:
            messages.info(request,'password didnt match')
            print('password didnt match')
            return redirect('registration')


    else:
        return render(request,'registration.html')
    
    return redirect('/') 

