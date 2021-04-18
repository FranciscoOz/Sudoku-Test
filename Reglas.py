def VerificaExistencia(archivo):
    try:
        with open(archivo, 'r') as f:
            return True
    except FileNotFoundError as e:
        return False
    except IOError as e:
        return False

def EntreUnoNueve(valor):
    listNumeros = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    Cumple = False
    if valor in listNumeros:
        Cumple = True
    return Cumple

def BuscaVacio(sudoku):
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == "0":
                return i, j
    return False

def ValidaCifra(sudoku, num, fila, col):
    for i in range(9):
        if sudoku[fila][i] == num and col != i:
            return False
        if sudoku[i][col] == num and fila != i:
            return False

    casilla_x = col // 3
    casilla_y = fila // 3
    for i in range(casilla_y*3, casilla_y*3 + 3):
        for j in range(casilla_x * 3, casilla_x*3 + 3):
            if sudoku[i][j] == num and (i, j) != (fila, col):
                return False

    return True


#BackTracking
def ResuelveCifra(sudoku):
    encontrar = BuscaVacio(sudoku)
    if not encontrar:
        return True
    else:
        fila, col = encontrar
    listNumeros=["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    for num in listNumeros:
        if ValidaCifra(sudoku, num, fila, col):
            sudoku[fila][col] = num
            if ResuelveCifra(sudoku):
                return True
            sudoku[fila][col] = "0"
    return False



