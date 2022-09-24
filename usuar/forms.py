from django import forms
from django.forms import ModelForm
from usuar.models import *

class PostulanteForm(ModelForm):
    class Meta:
        model = Postulante
        fields = '__all__'

        widgets = {
            'nombres': forms.TextInput(attrs={'class': 'form-control','placeholder':'Ingrese Nombres'}),
            'apellidos':forms.TextInput(attrs={'class': 'form-control','placeholder':'Ingrese Apellidos'}),
            'email':forms.TextInput(attrs={'class': 'form-control','placeholder':'Ingrese correo'}),
            'telefonos':forms.TextInput(attrs={'class': 'form-control','placeholder':'Ingrese de telefono'}),
            
             }


       

