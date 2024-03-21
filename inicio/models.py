from django.utils import timezone
from django.db import models


# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=50, default='')
    apellido = models.CharField(max_length=50, default='')
    usuario =  models.CharField(max_length=50, default='')
    contraseña = models.CharField(max_length=50, default='')
    foto_perfil = models.ImageField(upload_to='perfil/', null=True, blank=True)
    fecha_creacion = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return f"{self.nombre} {self.apellido} {self.usuario}"

class UsuarioEfimero(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    foto = models.ImageField(upload_to='fotos_incognito/', default='incognito.jpg')
    fecha_creacion = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return f"{self.nombre} {self.apellido}"

