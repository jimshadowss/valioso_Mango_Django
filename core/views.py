
from django.shortcuts import render, redirect
from .models import Usuario  
from django.contrib import messages




def inicio(request):
    return render(request, "core/pages/get_size.html")


def como_funciona(request):
    return render(request, "core/pages/como_funciona.html")


def ingreso(request):
    
    if request.method == 'POST':
        nombre_usuario = request.POST.get('nombreusuario')
        contraseña = request.POST.get('contraseña')
        usuario = Usuario.objects.filter(nombre_usuario=nombre_usuario, contraseña=contraseña).first()

        if usuario:
            return redirect('mi_tienda')
        else:
            mensaje_error = "Nombre de usuario o contraseña incorrectos."
            return render(request, 'core/pages/form_ingreso.html', {'mensaje_error': mensaje_error})

    return render(request, 'core/pages/form_ingreso.html')



def registro(request):
    if request.method == 'POST':
        # datos del formulario
        nombre_usuario = request.POST.get('nombreusuario')
        contraseña = request.POST.get('pass')

        
        if Usuario.objects.filter(nombre_usuario=nombre_usuario).exists():
            messages.error(request, 'El nombre de usuario ya está en uso. Por favor, elige otro.')
            return redirect('registro')

        
        nuevo_usuario = Usuario(
            nombre_usuario=nombre_usuario,
            contraseña=contraseña,
            apellido=request.POST.get('apellido'),
            nombre=request.POST.get('nombres'),
            fnac=request.POST.get('fecha-de-nacimiento'),
            mail=request.POST.get('correo'),
        )
        nuevo_usuario.save()

        messages.success(request, '¡Registro exitoso!')
        return redirect('registro')

    return render(request, "core/pages/form_registro_usuario.html")




def video(request, size):
    context = {"small": 768, "med": 1024, "size": size}
    return render(request, "core/pages/template_video_index.html", context)


def mi_tienda(request):
    return render(request, "core/pages/mi_tienda.html")


