from django.db import models
from django.urls import reverse
from apps.students.models import Student


class diplomaver(models.Model):
    diplom = models.FileField(blank=True, upload_to="students/diplomaver/")
    def get_absolute_url(self):
        return reverse("veri_fication", kwargs={"pk": self.pk})
    
   


