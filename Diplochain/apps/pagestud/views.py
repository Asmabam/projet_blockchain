import csv

from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import DetailView

#from .models import pagestudent
from apps.students.models import Student

#
class nStudentDetailView(LoginRequiredMixin,DetailView):
    model = Student
    template_name = "student_detailstud.html"

    def get_context_data(self, **kwargs):
        context = super(nStudentDetailView, self).get_context_data(**kwargs)
        return context
       
 