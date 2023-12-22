import csv
import hashlib
import base64
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView
from django.views.generic import DetailView

from apps.students.views import StudentCreateView
from django.forms import widgets
#from .models import pagestudent
from .models import diplomaver

#
class verifiview(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model= diplomaver
    template_name = "verif.html"
    fields = "__all__"
    success_message = "le diplome est deposé"
    def get_form(self):
        form = super(verifiview, self).get_form()
        form.fields['diplom'].widget = widgets.FileInput()
        form.fields['diplom'].label = "Déposez le diplome à verifier ici"
        return form   
    with open(r"C:\Users\PC\Desktop\project-info\media\students\diploms\Boussif.pdf", "rb") as imageFile:
        data1=base64.b64encode(imageFile.read())
    with open(r"C:\Users\PC\Desktop\project-info\media\students\diploms\Boussif.pdf", "rb") as imageFile:
        data2= base64.b64encode(imageFile.read())
    def calculate_hash(data):
        sha = hashlib.sha256()
        sha.update(str(data).encode('utf-8'))
        return sha.hexdigest()
    def verification(str1,str2):
        sha1 = hashlib.sha256()
        sha1.update(str(str1).encode('utf-8'))
        hash1 = sha1.hexdigest()
        sha2 = hashlib.sha256()
        sha2.update(str(str2).encode('utf-8'))
        hash2 = sha2.hexdigest()
        if (str1==str2) and (hash1==hash2) :
            return "le certificat est effectivement fourni par notre institution"
        else:
            return "le certificat est falsifié"