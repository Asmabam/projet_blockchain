from django.core.validators import RegexValidator
from django.db import models
from django.urls import reverse
from django.utils import timezone


class Staff(models.Model):
    GENDER = [("homme", "Homme"), ("femme", "Femme")]
    surname = models.CharField(max_length=200)
    firstname = models.CharField(max_length=200)
    identifiant=models.CharField(max_length=15,unique=True)
    gender = models.CharField(max_length=10, choices=GENDER, default="male")
    date_of_birth = models.DateField(default=timezone.now)
    current_status = models.CharField(max_length=30)
    mobile_num_regex = RegexValidator(
        regex="^[0-9]{10,15}$", message="Entered mobile number isn't in a right format!"
    )
    mobile_number = models.CharField(
        validators=[mobile_num_regex], max_length=13, blank=True
    )

    address = models.CharField(max_length=30,blank=True)
    others = models.TextField(blank=True)

    def __str__(self):
        return f"{self.surname} {self.firstname}"

    def get_absolute_url(self):
        return reverse("staff-detail", kwargs={"pk": self.pk})
