from django.contrib import admin
from .models import Usuario, UsuarioEfimero
# Register your models here.

class UsuariAdmin(admin.ModelAdmin):
    exclude = ('fecha_creacion',)
    list_display = ('nombre','apellido', 'usuario', 'fecha_creacion')

class UsuarioEfiemroAdmin(admin.ModelAdmin):
    exclude = ('fecha_creacion',)
    list_display = ('nombre','apellido', 'fecha_creacion')

admin.site.register(Usuario,UsuariAdmin )
admin.site.register(UsuarioEfimero, UsuarioEfiemroAdmin)