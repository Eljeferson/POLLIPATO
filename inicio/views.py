from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Usuario, UsuarioEfimero

# Create your views here.
def inicio(request):
    return render(request, 'inicio.html')

def crear_cuenta(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        usuario = request.POST.get('usuario')
        contraseña = request.POST.get('contraseña')
        usuario_existente = Usuario.objects.filter(usuario=usuario).first()
        if not usuario_existente:
            nuevo_usuario = Usuario(nombre=nombre, apellido=apellido, usuario=usuario, contraseña=contraseña)
            nuevo_usuario.save()
            request.session['nombre'] = nombre
            request.session['apellido'] = apellido
            return redirect('feed')
        else:
            return HttpResponse("El usuario ya existe.")
    else:
        return render(request, 'crear_cuenta.html')
    
def ingresar(request):
    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        contraseña = request.POST.get('contraseña')
        if not usuario or not contraseña:
            return HttpResponse("Usuario y contraseña son requeridos.")
        else:
            user = Usuario.objects.filter(usuario=usuario, contraseña=contraseña).first()
            if user:
                request.session['nombre'] = user.nombre
                request.session['apellido'] = user.apellido
                return redirect('feed')
            else:
                return HttpResponse("Usuario o contraseña incorrectos.")
    else:
        return render(request, 'ingresar.html')

def modo_incognito(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        if not nombre or not apellido:
            return HttpResponse("Ingresar ambos")
        else:
            request.session['nombre_incognito'] = nombre
            request.session['apellido_incognito'] = apellido
            usuario_efimero = UsuarioEfimero(nombre=nombre, apellido=apellido)
            usuario_efimero.save()
            return redirect('feedIncognito')
    else:
        return render(request, 'modo_incognito.html')