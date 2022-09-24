from unicodedata import name
from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import CreateView, TemplateView
from usuar.forms import *
from usuar.models import *

# Create your views here.

class Postulante(CreateView):
    model = Postulante
    template_name = "form.html"
    success_url = reverse_lazy('Principal')
    form_class = PostulanteForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'TRABAJA CON NOSOTROS'
        context['action'] = 'add'
        return context

class Inicio(TemplateView):
    model = Empresa
    template_name = "inicio.html"
    success_url = reverse_lazy('Inicio')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Inicio'
        context['url_anterior'] = 'Trabajaconnosotros/'
        context['nombre'] = Empresa.objects.values("nombre")
        context['contacto'] = Empresa.objects.values("contacto")
        context['correo'] = Empresa.objects.values("correo")
        return context