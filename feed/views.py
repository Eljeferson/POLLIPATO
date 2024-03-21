from django.shortcuts import render, redirect
from django import forms
from inicio.models import Usuario, UsuarioEfimero
from .models import Publicacion, PublicacionEfimero, Especialista
from itertools import chain
# Create your views here.
def feed(request):
    nombre = request.session.get('nombre')
    apellido = request.session.get('apellido')
    especialistas = Especialista.objects.order_by('-fecha_creacion').all()

    if request.method == 'POST':
        contenido = request.POST.get('contenido')
        foto = request.FILES.get('foto')

        if nombre and apellido and foto:  # Verificar si se está actualizando la foto de perfil
            usuario, _ = Usuario.objects.get_or_create(nombre=nombre, apellido=apellido)
            usuario.foto_perfil = foto  # Actualiza la foto de perfil
            usuario.save()

        else:  # Si no se está actualizando la foto de perfil, es una publicación normal
            if nombre and apellido and contenido:
                usuario = Usuario.objects.get(nombre=nombre, apellido=apellido)
                publicacion = Publicacion(usuario=usuario, publicacion=contenido)
                publicacion.save()

        return redirect('feed')

    publicaciones = Publicacion.objects.all().order_by('-fecha_creacion')
    publicaciones_efimeras = PublicacionEfimero.objects.all().order_by('-fecha_creacion')
    publicaciones_combinadas = sorted(
        chain(publicaciones, publicaciones_efimeras),
        key=lambda x: x.fecha_creacion,
        reverse=True
    )
    class PublicacionForm(forms.ModelForm):
        class Meta:
            model = Publicacion
            fields = ['publicacion']
    
    usuario = Usuario.objects.get(nombre=nombre, apellido=apellido)
    if usuario.foto_perfil:
        foto_perfil = usuario.foto_perfil.url
    else:
        foto_perfil = None

    return render(request, 'feed.html', {'nombre': nombre, 'apellido': apellido, "usuario":usuario, 'publicaciones_combinadas': publicaciones_combinadas, 'form': PublicacionForm(), 'foto_perfil': foto_perfil, 'especialistas': especialistas})


def feedIncognito(request):
    nombre_incognito = request.session.get('nombre_incognito')
    apellido_incognito = request.session.get('apellido_incognito')
    especialistas = Especialista.objects.order_by('-fecha_creacion').all()

    if request.method == 'POST':
        contenido = request.POST.get('contenido')

        if nombre_incognito and apellido_incognito:
            usuario_efimero, _ = UsuarioEfimero.objects.get_or_create(nombre=nombre_incognito, apellido=apellido_incognito)
            
            publicacion_efimero = PublicacionEfimero(usuario=usuario_efimero, publicacion=contenido)
            publicacion_efimero.save()
            return redirect('feedIncognito') 

    publicaciones = Publicacion.objects.all().order_by('-fecha_creacion')
    publicaciones_efimeras = PublicacionEfimero.objects.all().order_by('-fecha_creacion')
    publicaciones_combinadas = sorted(
        chain(publicaciones, publicaciones_efimeras),
        key=lambda x: x.fecha_creacion,
        reverse=True
    )
    class PublicacionIncognitoForm(forms.ModelForm):
        class Meta:
            model = PublicacionEfimero
            fields = ['publicacion']

    if nombre_incognito and apellido_incognito:
        form = PublicacionIncognitoForm()
    else:
        form = None

    return render(request, 'feed_Incg.html', {'nombre_incognito': nombre_incognito, 'apellido_incognito': apellido_incognito, 'publicaciones_combinadas': publicaciones_combinadas, 'form': PublicacionIncognitoForm(), 'especialistas': especialistas})



    
