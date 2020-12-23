def Regla_1(valor):
    Cumple = False
    if valor=="1" or valor=="2" or valor=="3" or valor=="4" or valor=="5" or valor=="6" or valor=="7" or valor=="8" or valor=="9":
        Cumple = True
    return Cumple

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

def filaCuadrante(cuadrante):
    filai = (cuadrante - 1) // 3
    listaFila = []
    for i in range(filai * 3, filai * 3 + 3):
        listaFila.append(i)
    return listaFila

def columnaCuadrante(cuadrante):
    columnai = (cuadrante - 1) // 3
    columnaFila = []
    for i in range(columnai * 3, columnai * 3 + 3):
        columnaFila.append(i)
    return columnaFila

def RetornaPosiblesVertical(tabla, fila, columna):
    disponibles = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    filas = len(tabla)
    for i in range(filas):
        if i != fila:
            valor = tabla[i][columna]
            if valor in disponibles:
                disponibles.remove(valor)
    return disponibles

def RetornaPosiblesHorizontal(tabla, fila, columna):
    disponibles = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    columnas = len(tabla[0])
    for i in range(columnas):
        if i != columna:
            valor = tabla[fila][i]  # valor que hay asignado
            if valor in disponibles:  # si el valor que hemos leido esta en la lista
                disponibles.remove(valor)  # lo borramos de la lista ya que no disponible
    return disponibles

def RetornaPosiblesCuadrante(tabla, fila, columna):
    disponibles = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
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

# Actualizacion_1.5

def VerificaExistencia(archivo):
    try:
        with open(archivo, 'r') as f:
            return True
    except FileNotFoundError as e:
        return False
    except IOError as e:
        return False

def Resolver_cifra(sudoku):
    encontrar = Encontrar_vacio(sudoku)
    if not encontrar:
        return True
    else:
        fila, col = encontrar
    listNumeros=["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    for num in listNumeros:
        if validar_cifra(sudoku, num, fila, col):
            sudoku[fila][col] = num
            if Resolver_cifra(sudoku):
                return True
            sudoku[fila][col] = "0"
    return False

def Encontrar_vacio(sudoku):
    for i in range(len(sudoku)):
        for j in range(len(sudoku[0])):
            if sudoku[i][j] == "0":
                return i, j  # fila, columna
    return False

def validar_cifra(sudoku, num, fila, col):
    #Comprobar fila y col
    for i in range(9):
        if sudoku[fila][i] == num and col != i:
            return False
        if sudoku[i][col] == num and fila != i:
            return False

    # Casilla de verificación
    casilla_x = col // 3
    casilla_y = fila // 3
    for i in range(casilla_y*3, casilla_y*3 + 3):
        for j in range(casilla_x * 3, casilla_x*3 + 3):
            if sudoku[i][j] == num and (i, j) != (fila, col):
                return False

    return True



