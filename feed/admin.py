from django.contrib import admin
from .models import Publicacion, Especialista, PublicacionEfimero

# Register your models here.
class PublicacionAdmin(admin.ModelAdmin):
    exclude = ('fecha_creacion',)
    list_display = ('usuario', 'publicacion', 'fecha_creacion')
class PublicacionEfimeraAdmin(admin.ModelAdmin):
    exclude = ('fecha_creacion',)
    list_display = ('usuario', 'publicacion', 'fecha_creacion')
class EspecialistaAdmin(admin.ModelAdmin):
    exclude = ('fecha_creacion',)
    list_display = ('nombre','apellido', 'celular', 'email', 'fecha_creacion')

admin.site.register(Publicacion, PublicacionAdmin)
admin.site.register(PublicacionEfimero, PublicacionEfimeraAdmin)
admin.site.register(Especialista, EspecialistaAdmin)