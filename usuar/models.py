from django.db import models
from usuario import settings


# Create your models here.

class Postulante(models.Model):
    nombres = models.CharField(max_length=200, unique=True)
    apellidos = models.CharField(max_length=200, unique=True)
    email = models.CharField(max_length=100,unique=True)
    telefonos = models.CharField(max_length=50, blank=True, null=True)
    archivo = models.FileField(upload_to='usuar/media', blank=True, null=True)

    def __str__(self):
        return "{}".format(self.nombres)

    class Meta:
        verbose_name = "Postulante"
        verbose_name_plural = "Postulante"
        ordering = ('nombres',)

    def get_archivo(self):
        if self.archivo:
            return '{}{}'.format(settings.MEDIA_URL, self.archivo)
        return '{}{}'.format(settings.STATIC_URL, 'usuar/media')


class Empresa(models.Model):
    nombre = models.CharField(max_length=50,verbose_name='Empresa',unique=True)
    contacto=models.CharField(max_length=50, blank=True, null=True)
    correo =  models.EmailField(max_length=100, blank=True, null=True)


    def __str__(self):
        return "{}".format(self.nombre)
    class Meta:
        verbose_name = 'Empresa'
        ordering = ('nombre',)
