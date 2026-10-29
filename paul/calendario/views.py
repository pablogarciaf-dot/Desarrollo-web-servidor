from datetime import date, datetime

from django.shortcuts import redirect, render

MESES = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio',
         'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre']
DIAS_SEMANA = ['lunes', 'martes', 'miércoles', 'jueves', 'viernes', 'sábado', 'domingo']


def hoy(request):
    '''
    Si se entra en /calendario/ sin fecha, redirigimos a la fecha de hoy.
    '''
    fecha_hoy = date.today().strftime('%d-%m-%Y')
    return redirect('calendario:calendario', fecha=fecha_hoy)


def calendario(request, fecha):
    '''
    Recibe una fecha con el formato "DD-MM-AAAA" y muestra algunos datos sobre ella.
    Si la fecha no tiene ese formato o no existe (por ejemplo 31-02-2026),
    se muestra la página de error.
    '''
    try:
        # strptime convierte el texto en fecha y lanza ValueError si no encaja
        fecha_obj = datetime.strptime(fecha, '%d-%m-%Y').date()
    except ValueError:
        return render(request, 'calendario/error.html', {'fecha': fecha}, status=400)

    mi_dia = fecha_obj.day
    mi_mes = MESES[fecha_obj.month - 1]
    mi_ano = fecha_obj.year

    dia_semana = DIAS_SEMANA[fecha_obj.weekday()]
    diferencia = (fecha_obj - date.today()).days

    if diferencia == 0:
        cuando = 'Es hoy'
    elif diferencia == 1:
        cuando = 'Es mañana'
    elif diferencia == -1:
        cuando = 'Fue ayer'
    elif diferencia > 0:
        cuando = f'Faltan {diferencia} días'
    else:
        cuando = f'Fue hace {-diferencia} días'

    mensaje = f'Cae en {dia_semana}. {cuando}'

    return render(request, 'calendario/fecha.html',
                  {'dia': mi_dia, 'mes': mi_mes, 'ano': mi_ano, 'mensaje': mensaje})
