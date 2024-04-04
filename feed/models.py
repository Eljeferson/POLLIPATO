from django.db import models
from django.utils import timezone
from inicio.models import Usuario, UsuarioEfimero

# Create your models here.
class Publicacion(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True, blank=True)
    publicacion = models.CharField(max_length=500)
    fecha_creacion = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return f"{self.usuario} {self.publicacion}"
    
class PublicacionEfimero(models.Model):
    usuario = models.ForeignKey(UsuarioEfimero, on_delete=models.CASCADE, null=True, blank=True)
    publicacion = models.CharField(max_length=500)
    fecha_creacion = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return f"{self.usuario} {self.publicacion}"
    
class Especialista(models.Model):
    foto = models.ImageField(upload_to='especialista/')
    publicacion = models.CharField(max_length=400, default='')
    nombre = models.CharField(max_length=50, default='')
    apellido = models.CharField(max_length=50, default='')
    celular = models.CharField(max_length=50, default='')
    email = models.EmailField(blank=True)
    nombre_linkedin = models.CharField(max_length=50, default='')
    nombre_instagram = models.CharField(max_length=50, default='')
    nombre_facebook = models.CharField(max_length=50, default='')
    nombre_tiktok = models.CharField(max_length=50, default='')
    orden = models.IntegerField(default=0)
    fecha_creacion = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return f"{self.nombre} {self.apellido} {self.celular} {self.email}"