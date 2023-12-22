# -*- encoding: utf-8 -*-

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm, SignUpForm

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.urls import reverse
from apps.students.models import Student

def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None

    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)

            if user is not None :
                login(request, user)
                user_id = user.id

                if (user.username.endswith('@student.com')):
                  studentId = Student.objects.filter(username=username).first().id
                  url = reverse('student-detailstud', kwargs={'pk': studentId})
                  return redirect( url)
                elif (user.username.endswith('@staff.com')):
                #return redirect("pagestud/<int:pk>/")
                    return redirect("/")
                else:
                    url = reverse('veri_fication', kwargs={'pk': user_id})
                    return redirect( url)
                    #return redirect("verification/")
                #return url 
            else:
                msg = 'Invalid credentials'
        else:
            msg = 'Error validating the form'

    return render(request, "registration/login.html", {"form": form, "msg": msg})

def register_user(request):
    msg = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)

            msg = 'User created successfully.'
            success = True

            # return redirect("/login/")

        else:
            msg = 'Form is not valid'
    else:
        form = SignUpForm()

    return render(request, "registration/register.html", {"form": form, "msg": msg, "success": success})

