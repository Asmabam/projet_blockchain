from django.core.validators import RegexValidator
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from apps.corecode.models import StudentClass
from django.conf import settings
import base64
import hashlib
import os
from pathlib import Path

def covdip(file_path):
    try:
        with open(file_path, "rb") as imageFile:
            encoded_data = base64.b64encode(imageFile.read())
            return encoded_data.decode("utf-8")
    except FileNotFoundError:
        print(f"Le fichier spécifié '{file_path}' est introuvable.")
        return None
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")
        return None

class Student(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    GENDER_CHOICES = [("homme", "Homme"), ("femme", "Femme")]
    surname = models.CharField(max_length=200)
    firstname = models.CharField(max_length=200)
    identifiant = models.CharField(max_length=200, unique=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default="male")
    date_of_birth = models.DateField(default=timezone.now)
    current_class = models.ForeignKey(
        StudentClass, on_delete=models.SET_NULL, blank=True, null=True
    )
    mobile_num_regex = RegexValidator(
        regex="^[0-9]{10,15}$", message="Entered mobile number isn't in a right format!"
    )
    mobile_number = models.CharField(
        validators=[mobile_num_regex], max_length=13, blank=True
    )

    address = models.CharField(max_length=30,blank=True)
    others = models.TextField(blank=True)
    username=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    passport = models.ImageField(blank=True, upload_to="students/passports/")
    diplom = models.FileField(blank=True, upload_to="students/diploms/")
    diplomcod=models.TextField(blank=True,null=True)

    
    def get_diplomcod(self):
        # Read the contents of the 'diplom' file and encode it into a string
        if self.diplom:
            try:
               # with open("C:/Users/PC/Desktop/project-info/media/students/diploms/Planning_S5_2023-2024_7N4mGAe.pdf", "rb") as imageFile:
                    #absolute_path =Path(str(self.diplom)).resolve()
                    #absolute_path = os.path.abspath(str(self.diplom))
                    relative_file_path = "C:/Users/PC/Desktop/project-info/media/students/diploms/"
                    relpath=Path(str(self.diplom))
                    absolute_path = os.path.join( relative_file_path, relpath)
                    print(self.diplom)
                    with open(absolute_path) as imageFile:
                      fic = base64.b64encode(imageFile.read())
                      return fic
            except Exception as e:
                print(f"Error reading 'diplom' file: {e}")
        return None

    def save(self, *args, **kwargs):
        # Mettez à jour le champ 'diplomcod' avant d'enregistrer l'instance
        if not self.diplomcod: 
            self.diplomcod = self.get_diplomcod()
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.surname} {self.firstname} ({self.identifiant})"

    def get_absolute_url(self):
        return reverse("student-detail", kwargs={"pk": self.pk})
    
    
#class Diplomecode(models.Model):
    
class studeblock(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    hashcode=models.TextField(null=True,db_column='hashcode')
    previoushash=models.TextField(null=True,db_column='previoushash')
    def calc_hash(self):
        sha = hashlib.sha256()
        data = f"{self.student.id}{self.student.surname}{self.student.firstname}{self.student.gender}{self.student.date_of_birth}{self.student.diplom}"
        sha.update(data.encode('utf-8'))  # Encoding the data (hexadecimal format) before hashing
        return sha.hexdigest()
    @receiver(post_save, sender=Student)
    def create_student_block(sender, instance, created, **kwargs):
        if created:
            studeblock.objects.create(student=instance)

    @receiver(post_save, sender=Student)
    def save_student_block(sender, instance, **kwargs):
        instance.studeblock.save()
   
    
    
class StudentBulkUpload(models.Model):
    date_uploaded = models.DateTimeField(auto_now=True)
    csv_file = models.FileField(upload_to="students/bulkupload/")
