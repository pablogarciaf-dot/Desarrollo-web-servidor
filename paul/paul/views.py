from django.shortcuts import render


def homepage(request):
    return render(request, 'home.html')


def contacto(request):
    # Si se ha enviado el formulario (POST), mostramos un mensaje de agradecimiento
    if request.method == 'POST':
        nombre = request.POST.get('nombre', '')
        return render(request, 'contacto.html', {'enviado': True, 'nombre': nombre})
    # Si solo se visita la página (GET), mostramos el formulario vacío
    return render(request, 'contacto.html')
