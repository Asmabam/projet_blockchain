from django.urls import path
from .views import (
    nStudentDetailView,

)

urlpatterns = [
    path("<int:pk>", nStudentDetailView.as_view(), name="student-detail"),
    path("<int:pk>", nStudentDetailView.as_view(), name="student-detailstud"),
]
