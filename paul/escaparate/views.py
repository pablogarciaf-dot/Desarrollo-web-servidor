from django.shortcuts import render

def inicio(request):
    # Apuntamos a la carpeta 'escaparate' dentro de templates
    return render(request, 'escaparate/inicio_escaparate.html')