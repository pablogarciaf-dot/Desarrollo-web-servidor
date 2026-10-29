from django.shortcuts import render

# Combinaciones de casillas que hacen tres en raya
#  0 | 1 | 2
#  3 | 4 | 5
#  6 | 7 | 8
LINEAS = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),  # filas
    (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columnas
    (0, 4, 8), (2, 4, 6),             # diagonales
]


def comprobar_ganador(tablero):
    '''Devuelve 'X' u 'O' si alguien ha hecho tres en raya, o None si no.'''
    for a, b, c in LINEAS:
        if tablero[a] != '-' and tablero[a] == tablero[b] == tablero[c]:
            return tablero[a]
    return None


def tablero_valido(tablero):
    '''Comprueba que el tablero tiene 9 casillas y solo contiene X, O o -.'''
    return len(tablero) == 9 and all(casilla in 'XO-' for casilla in tablero)


def tres_en_raya(request):
    if request.method == 'POST':
        # El tablero llega como texto, por ejemplo "O-X-X----",
        # y lo convertimos en una lista de 9 casillas
        tablero = list(request.POST.get('tablero', ''))
        turno = request.POST.get('turno', 'X')
        posicion = request.POST.get('posicion', '')

        # Si alguien ha manipulado el formulario, empezamos de cero
        if not tablero_valido(tablero) or turno not in ('X', 'O'):
            tablero = ['-'] * 9
            turno = 'X'

        mensaje = f'Turno de {turno}'

        if posicion.isdigit() and 0 <= int(posicion) <= 8:
            posicion = int(posicion)
            if tablero[posicion] == '-':
                tablero[posicion] = turno
                # Cambiamos de jugador
                turno = 'O' if turno == 'X' else 'X'
                mensaje = f'Turno de {turno}'
            else:
                mensaje = f'Esa casilla ya está ocupada. Sigue siendo el turno de {turno}'

        ganador = comprobar_ganador(tablero)
        if ganador:
            mensaje = f'Ha ganado {ganador}'
            terminado = True
        elif '-' not in tablero:
            mensaje = 'Empate'
            terminado = True
        else:
            terminado = False

    else:
        tablero = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
        turno = 'X'
        mensaje = 'Turno de X'
        terminado = False

    contexto = {
        'tablero': tablero,
        # Versión en texto del tablero para el campo oculto del formulario
        'tablero_texto': ''.join(tablero),
        'turno': turno,
        'mensaje': mensaje,
        'terminado': terminado,
    }
    return render(request, 'tres_en_raya/tres_en_raya.html', contexto)
