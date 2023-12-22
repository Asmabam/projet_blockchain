import csv

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.forms import widgets
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.views.generic.edit import CreateView, DeleteView, UpdateView
import base64
from .models import Student, StudentBulkUpload


class StudentListView(LoginRequiredMixin, ListView):
    model = Student
    template_name = "students/student_list.html"


class StudentDetailView(LoginRequiredMixin, DetailView):
    model = Student
    template_name = "students/student_detail.html"

    def get_context_data(self, **kwargs):
        context = super(StudentDetailView, self).get_context_data(**kwargs)
        return context
    
     
    
class StudentCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Student
    fields = "__all__"
    exclude = ['diplomcod']
    success_message = "New student successfully added."
    
    def get_form(self):
        """add date picker in forms"""
        form = super(StudentCreateView, self).get_form()
        form.exclude = ['diplomcod']
        form.fields["date_of_birth"].widget = widgets.DateInput(attrs={"type": "date"})
        form.fields["others"].widget = widgets.Textarea(attrs={"rows": 2})
        form.fields['passport'].widget = widgets.FileInput()
        form.fields["diplom"].widget = widgets.FileInput()
        form.fields["surname"].label = "Nom"
        form.fields["firstname"].label = "Prénom"
        form.fields["identifiant"].label = "ID"
        form.fields["current_class"].label = "Classe"
        form.fields["gender"].label = "Genre"
        form.fields["mobile_number"].label = "Numéro de téléphone"
        form.fields["address"].label = "Adresse mail"
        form.fields["date_of_birth"].label = "Date de naissance"
        form.fields["others"].label = "Autre"
        form.fields["passport"].label = "Photo de profil"
        form.fields["diplom"].label = "Diplome"
        form.fields["username"].label = "username"
        form.fields["password"].label = "mot de passe"
        
        return form

    
   

class StudentUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Student
    fields = "__all__"
    success_message = "Record successfully updated."

    def get_form(self):
        """add date picker in forms"""
        form = super(StudentUpdateView, self).get_form()
        form.fields["date_of_birth"].widget = widgets.DateInput(attrs={"type": "date"})
        form.fields["others"].widget = widgets.Textarea(attrs={"rows": 2})
        form.fields['passport'].widget = widgets.FileInput()
        form.fields["diplom"].widget = widgets.FileInput()

        form.fields["surname"].label = "Nom"
        form.fields["firstname"].label = "Prénom"
        form.fields["identifiant"].label = "ID"
        form.fields["current_class"].label = "Classe"
        form.fields["gender"].label = "Genre"
        form.fields["mobile_number"].label = "Numéro de téléphone"
        form.fields["address"].label = "Adresse mail"
        form.fields["date_of_birth"].label = "Date de naissance"
        form.fields["others"].label = "Autre"
        form.fields["passport"].label = "Photo de profil"
        form.fields["diplom"].label = "Diplome"
        form.fields["username"].label = "username"
        form.fields["password"].label = "mot de passe"
        return form
    class Meta:
        model = Student
        exclude = ['diplomcod']

class StudentDeleteView(LoginRequiredMixin, DeleteView):
    model = Student
    success_url = reverse_lazy("student-list")


class StudentBulkUploadView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = StudentBulkUpload
    template_name = "students/students_upload.html"
    fields = ["csv_file"]
    success_url = "/student/list"
    success_message = "Successfully uploaded students"


class DownloadCSVViewdownloadcsv(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = 'attachment; filename="student_template.csv"'

        writer = csv.writer(response)
        writer.writerow(
            [
                "identifiant",
                "surname",
                "firstname",
                "gender",
                "mobile_number",
                "address",
                "current_class",
            ]
        )

        return response

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from apps.authentication.forms import SignUpForm
from .models import Student

def register_user(request):
    msg = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username") + '@student.com'
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)
            msg = 'User created successfully.'
            success = True

            # Check if the registered user is also a student
            student_id = form.cleaned_data.get("student_id")
            
            if student_id:
                register_student(username, raw_password, student_id)

            # You can redirect to the login page or another page here
            # return redirect("/login/")

        else:
            msg = 'Form is not valid'
    else:
        form = SignUpForm()

    return render(request, "students/student_form.html", {"form": form, "msg": msg, "success": success})

def register_student(username, password, id):
    # Check if a student with the given identifiant exists
    student = Student.objects.filter(id=id).first()

    if student:
        # Update the student's username and password
        student.username = username
        student.password = password
        student.save()
