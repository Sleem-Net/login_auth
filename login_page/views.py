import email
from django.shortcuts import render
from django.contrib.auth.models import User


# Create your views here.


def HomePage(request):
    return render(request, 'login_page/index.html', {})
  

def Register(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('sname')
        user_name = request.POST.get('uname')
        email = request.POST.get('email')
        password = request.POST.get('pass')



        new_user = User.objects.create_user(user_name, email, password)
        new_user.first_name = fname
        new_user.last_name = lname


        new_user.save()

    return render(request, 'login_page/register.html', {})


def Login(request):
    return render(request, 'login_page/login.html', {})
