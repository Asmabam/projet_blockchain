from django import forms
from models import *

class CustomerForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Student
        fields = '__all__'
        exclude = ['diplomcod']
       # fields = ('id', 'surname', 'firstname', 'identifiant', 'gender', 'date_of_birth', 'current_class', 'mobile_number', 'address', 'others', 'username','password','passport','diplom')