from django.contrib import admin
from django.contrib.admin import AdminSite
from usuar.models import *


admin.site.register(Postulante)
admin.site.register(Empresa)

