import random

def Regla_1(valor):
    Cumple = False
    if 0<valor and valor<=9:
        Cumple = True
    return Cumple

def filaCuadrante(cuadrante):
    if cuadrante == 1 or cuadrante == 2 or cuadrante == 3:
        return [0, 1, 2]
    elif cuadrante == 4 or cuadrante == 5 or cuadrante == 6:
        return [3, 4, 5]
    elif cuadrante == 7 or cuadrante == 8 or cuadrante == 9:
        return [6, 7, 8]

def columnaCuadrante(cuadrante):
    if cuadrante == 1 or cuadrante == 4 or cuadrante == 7:
        return [0, 1, 2]
    elif cuadrante == 2 or cuadrante == 5 or cuadrante == 8:
        return [3, 4, 5]
    elif cuadrante == 3 or cuadrante == 6 or cuadrante == 9:
        return [6, 7, 8]

def RetornaInvertidos(posibles):
    imposibles = []
    if not (1 in posibles):
        imposibles.append(1)
    if not (2 in posibles):
        imposibles.append(2)
    if not (3 in posibles):
        imposibles.append(3)
    if not (4 in posibles):
        imposibles.append(4)
    if not (5 in posibles):
        imposibles.append(5)
    if not (6 in posibles):
        imposibles.append(6)
    if not (7 in posibles):
        imposibles.append(7)
    if not (8 in posibles):
        imposibles.append(8)
    if not (9 in posibles):
        imposibles.append(9)
    return imposibles

def RetornaPosiblesVertical(tabla, fila, columna):
    disponibles = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    filas = len(tabla)
    for i in range(filas):
        if i != fila:
            valor = tabla[i][columna]
            if valor in disponibles:
                disponibles.remove(valor)
    return disponibles

def RetornaPosiblesHorizontal(tabla, fila, columna):
    disponibles = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    columnas = len(tabla[0])
    for i in range(columnas):
        if i != columna:
            valor = tabla[fila][i]  # valor que hay asignado
            if valor in disponibles:  # si el valor que hemos leido esta en la lista
                disponibles.remove(valor)  # lo borramos de la lista ya que no disponible
    return disponibles

def RetornaCuadrante(fila, columna):
    if fila <= 2 and columna <= 2:
        return 1
    elif fila <= 5 and columna <= 2:
        return 4
    elif fila <= 8 and columna <= 2:
        return 7
    elif fila <= 2 and columna <= 5:
        return 2
    elif fila <= 5 and columna <= 5:
        return 5
    elif fila <= 8 and columna <= 5:
        return 8
    elif fila <= 2 and columna <= 8:
        return 3
    elif fila <= 5 and columna <= 8:
        return 6
    elif fila <= 8 and columna <= 8:
        return 9

def RetornaPosiblesCuadrante(tabla, fila, columna):
    disponibles = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    cuadrante = RetornaCuadrante(fila, columna)
    minifilas = filaCuadrante(cuadrante)
    minicolumnas = columnaCuadrante(cuadrante)
    valorinicialenpuntoestudio = tabla[fila][columna]
    tabla[fila][columna] = ''
    for i in minifilas:
        for j in minicolumnas:
            if tabla[i][j] != '':
                valor = tabla[i][j]
                if valor in disponibles:
                    disponibles.remove(valor)
    tabla[fila][columna] = valorinicialenpuntoestudio  # volvemos a poner el valor inicial
    return disponibles

def RetornaTotalPosibles(tabla, fila, columna):
    lista1 = RetornaPosiblesVertical(tabla, fila, columna)
    lista2 = RetornaPosiblesHorizontal(tabla, fila, columna)
    lista3 = RetornaPosiblesCuadrante(tabla, fila, columna)
    lista1 = RetornaInvertidos(lista1)
    lista2 = RetornaInvertidos(lista2)
    lista3 = RetornaInvertidos(lista3)
    listatotal = lista1 + lista2 + lista3
    listaimposibles = []
    if 1 in listatotal:
        listaimposibles.append(1)
    if 2 in listatotal:
        listaimposibles.append(2)
    if 3 in listatotal:
        listaimposibles.append(3)
    if 4 in listatotal:
        listaimposibles.append(4)
    if 5 in listatotal:
        listaimposibles.append(5)
    if 6 in listatotal:
        listaimposibles.append(6)
    if 7 in listatotal:
        listaimposibles.append(7)
    if 8 in listatotal:
        listaimposibles.append(8)
    if 9 in listatotal:
        listaimposibles.append(9)
    listaposibles = RetornaInvertidos(listaimposibles)
    return listaposibles

def RellenaInmediatos(tabla):
    actuado = 0
    filas = len(tabla)
    columnas = len(tabla[0])
    for i in range(filas):
        for j in range(columnas):
            if tabla[i][j] == 0:
                posibles = RetornaTotalPosibles(tabla, i, j)
                if len(posibles) == 1:
                    tabla[i][j] = posibles[0]
                    actuado = 1
    return actuado

def RetornaUnoDeLaLista(lista):
    longitud = len(lista)
    return lista[random.randint(0, longitud - 1)]

def RellenaUnaCasillaCon2Posibles(tabla):
    filas = len(tabla)
    columnas = len(tabla[0])
    for i in range(filas):
        for j in range(columnas):
            if tabla[i][j] == 0:  # casilla vacia
                posibles = RetornaTotalPosibles(tabla, i, j)
                if len(posibles) == 2:
                    tabla[i][j] = RetornaUnoDeLaLista(posibles)
                    return True
    return False

def RellenaUnaCasillaCon3Posibles(tabla):
    filas = len(tabla)
    columnas = len(tabla[0])
    for i in range(filas):
        for j in range(columnas):
            if tabla[i][j] == 0:  # casilla vacia
                posibles = RetornaTotalPosibles(tabla, i, j)
                if len(posibles) == 3:
                    tabla[i][j] = RetornaUnoDeLaLista(posibles)
                    return True
    return False

def RellenaUnaCasillaCon4Posibles(tabla):
    filas = len(tabla)
    columnas = len(tabla[0])
    for i in range(filas):
        for j in range(columnas):
            if tabla[i][j] == 0:  # casilla vacia
                posibles = RetornaTotalPosibles(tabla, i, j)
                if len(posibles) == 4:
                    tabla[i][j] = RetornaUnoDeLaLista(posibles)
                    return True
    return False

def RellenaUnaCasillaCon5Posibles(tabla):
    filas = len(tabla)
    columnas = len(tabla[0])
    for i in range(filas):
        for j in range(columnas):
            if tabla[i][j] == 0:  # casilla vacia
                posibles = RetornaTotalPosibles(tabla, i, j)
                if len(posibles) == 5:
                    tabla[i][j] = RetornaUnoDeLaLista(posibles)
                    return True
    return False

def RellenaUnaCasillaCon6Posibles(tabla):
    filas = len(tabla)
    columnas = len(tabla[0])
    for i in range(filas):
        for j in range(columnas):
            if tabla[i][j] == 0:  # casilla vacia
                posibles = RetornaTotalPosibles(tabla, i, j)
                if len(posibles) == 6:
                    tabla[i][j] = RetornaUnoDeLaLista(posibles)
                    return True
    return False

def RellenaUnaCasillaCon7Posibles(tabla):
    filas = len(tabla)
    columnas = len(tabla[0])
    for i in range(filas):
        for j in range(columnas):
            if tabla[i][j] == 0:  # casilla vacia
                posibles = RetornaTotalPosibles(tabla, i, j)
                if len(posibles) == 7:
                    tabla[i][j] = RetornaUnoDeLaLista(posibles)
                    return True
    return False


# def RellenaUnaCasillaX(tabla):
#     filas = len(tabla)
#     columnas = len(tabla[0])
#     for i in range(filas):
#         for j in range(columnas):
#             if tabla[i][j] == 0:  # casilla vacia
#                 posibles = RetornaTotalPosibles(tabla, i, j)
#                 if len(posibles) == 2 or len(posibles) == 3 or len(posibles) == 4 or len(posibles) == 5 or len(posibles) == 6 or len(posibles) == 7:
#                     tabla[i][j] = RetornaUnoDeLaLista(posibles)
#                     return 1
#     return 0
