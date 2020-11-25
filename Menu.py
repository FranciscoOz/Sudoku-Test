from Reglas import *

matriz_nombres_guardados = ["PEPE: tablero1"]
matriz_tableros_guardados = [[[1, 3, 0, 5, 7, 0, 4, 0, 8], [4, 0, 0, 2, 6, 1, 0, 7, 5],[7, 0, 6, 0, 8, 0, 2, 0, 9],[6, 4, 3, 0, 0, 0, 7, 9, 0],[0, 2, 1, 0, 9, 0, 8, 4, 6],[9, 0, 0, 0, 0, 0, 5, 3, 1],[2, 1, 4, 9, 0, 0, 0, 8, 7],[3, 0, 0, 0, 0, 7, 0, 0, 4],[8, 0, 9, 0, 0, 2, 1, 0, 0]]]

def MenuPrincipal():
    print()
    print("☺☻♥☻♠☻♣☻♦☻ - - SUDOKU - - ☻♦☻♣☻♠☻♥☻☺")
    print("☺                                         ☺")
    print("☺    ", "Ingrese opción: ", "                  ", "☺")
    print("☺    ", "(1) Jugar tablero nuevo", "           ", "☺")
    print("☺    ", "(2) Ver/Jugar tablero guardado", "    ", "☺")
    print("☺    ", "(3) Finalizar", "                     ", "☺")
    print("☺                                         ☺")
    print("☺☻♥☻♠☻♣☻♦☻ -------------- ☻♦☻♣☻♠☻♥☻☺")
    opcion = input()
    return menuOpciones(opcion)

def menuOpciones(opcion):
    if opcion == "1":
        print(" --------------------")
        print("|", " 👇 Dificultad",end="")
        print("     |")
        print("|", "(0)  Fácil   (🤡) ","|")
        print("|", "(1)  Medio   (😈) ","|")
        print("|", "(2)  Difícil (💀) ","|")
        print(" --------------------")
        dificultad = input()
        sudoku = CreaMatrizInicial()
        RellenaCuadrante(sudoku, 1)
        RellenaCuadrante(sudoku, 5)
        RellenaCuadrante(sudoku, 9)
        RellenaPosibilidades(sudoku)
        if int(dificultad) >=0 and int(dificultad) <= 3:
            RellenaCeros(sudoku, dificultad)
        else:
            print("Escoge una dificultad válida >:)")
            return menuOpciones(opcion)
        continuaTablero(sudoku)
        print()
        print()
        return sudoku

    elif opcion=="2":
        print()
        print()
        print(" ________________________")
        print("|", "VER TABLEROS GUARDADOS", "|")
        print(" ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")
        print()
        print("Nombre: tablero guardado ")
        print("➖➖➖➖➖➖➖➖➖➖➖➖")
        for i in range (len(matriz_nombres_guardados)):
            print("✔ ", matriz_nombres_guardados[i])
            print("➖➖➖➖➖➖➖➖➖➖➖➖")
        Menu1()

    elif opcion == "3":
        print("- - Fin de juego - -")
        return 0
    else:
        print("Ingresa una opción válida entre 1 y 3 ☻\n")
        print()
        return MenuPrincipal()

def CreaMatrizInicial():
    tablero= []
    for i in range(9):
        tablero.append([])
        for j in range(9):
            tablero[i].append(0)
    return tablero

def RellenaCuadrante(tabla, cuadrante=1):
    disponibles = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    minifilas = filaCuadrante(cuadrante)
    minicolumnas = columnaCuadrante(cuadrante)
    for i in minifilas:
        for j in minicolumnas:
            longitud = len(disponibles)
            aleatorio = random.randint(0, longitud - 1)
            tabla[i][j] = disponibles[aleatorio]
            disponibles.remove(disponibles[aleatorio])

def DisponiblesCuadrante(tabla, cuadrante=1):
    disponibles = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    minifilas = filaCuadrante(cuadrante)
    minicolumnas = columnaCuadrante(cuadrante)
    for i in minifilas:
        for j in minicolumnas:
            longitud = len(disponibles)
            aleatorio = random.randint(0, longitud - 1)
            tabla[i][j] = disponibles[aleatorio]
            disponibles.remove(disponibles[aleatorio])
    return disponibles

def CuentaCeros(tabla):
    filas = len(tabla)
    columnas = len(tabla[0])
    ceros = 0
    for i in range(filas):
        for j in range(columnas):
            if tabla[i][j] == 0:
                ceros += 1
    return ceros

def RellenaPosibilidades(tabla):
    contador = 0
    while CuentaCeros(tabla) != 0 and contador <= 200:
        contador += 1
        while RellenaInmediatos(tabla) == 1:
           """ print("rellenada inmediatos")"""
        if RellenaUnaCasillaCon2Posibles(tabla):
            """print("rellenada 2 posibles")"""
        elif RellenaUnaCasillaCon3Posibles(tabla):
           """ print("rellenada 3 posibles")"""
        elif RellenaUnaCasillaCon4Posibles(tabla):
            """print("rellenada 4 posibles")"""
        elif RellenaUnaCasillaCon5Posibles(tabla):
           """ print("rellenada 5 posibles")"""
        elif RellenaUnaCasillaCon6Posibles(tabla):
            """print("rellenada 6 posibles")"""
        elif RellenaUnaCasillaCon7Posibles(tabla):
            """print("rellenada 7 posibles")"""

def MuestraTablero(tablero_principal):
    print("  | 1  2  3  | 4  5  6  | 7  8  9 |")
    for i in range(9):
        if i % 3 == 0:
            print("➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")
        print(i + 1, end=" ")
        for j in range(9):
            if j % 3 == 0:
                print("| ", end="")
            if j == 8:
                print(tablero_principal[i][j], "|")
            else:
                print(str(tablero_principal[i][j]) + "  ", end="")
        if i == 8:
            print("➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")

def RellenaCeros(tabla, nivel):
    if nivel == "0":
        maxceros = 34
    elif nivel == "1":
        maxceros = 40
    elif nivel == "2":
        maxceros = 52
    for i in range(maxceros):
        n = random.randint(0, 8)
        m = random.randint(0, 8)
        tabla[n][m] = 0

def guardaPartida(matriz,matriz_nombres_guardados, matriz_tableros_guardados):
    nombre_jugador=input("Ingrese nombre del jugador: ").upper()
    nombre_tablero=input("Ingrese nombre de la partida: ").lower()
    nombre_total=nombre_jugador+": "+nombre_tablero
    matriz_tableros_guardados.append(matriz)
    matriz_nombres_guardados.append(nombre_total)
    return continuaTablero(matriz)

def cargaPartida():
    nombre_jugador = input("Ingresa nombre de jugador: ").upper()
    nombre_partida = input("ingresa nombre de partida: ").lower()
    nombreTotal = nombre_jugador+": "+nombre_partida
    if nombreTotal in matriz_nombres_guardados:
        posicion = int(matriz_nombres_guardados.index(nombreTotal))
        matriz_resultado = matriz_tableros_guardados[posicion]
        return continuaTablero(matriz_resultado)
    else:
        print(f"No se encontró la partida {nombre_partida} del jugador {nombre_jugador}")
        return MenuPrincipal()

def borraPartida(nombre):
    IndexM = matriz_nombres_guardados.index(nombre)
    matrizBorrar = matriz_tableros_guardados[IndexM]
    matriz_nombres_guardados.remove(nombre)
    matriz_tableros_guardados.remove(matrizBorrar)
    return Menu1()

def Menu1():
    if len(matriz_tableros_guardados)==0:
        print("No hay tableros guardados")
        print("• (0) Desea volver al menú principal")
        print("• (1) Desea salir del juego?")
        opcion = input()
        if opcion == "0":
            return MenuPrincipal()
        elif opcion == "1":
            return 0
        else:
            print("Ingrese opción válida")
            return Menu1()

    else:
        print("Desea ver detalles del tablero? ")
        print("♦ (1) Sí")
        print("♦ (2) No y volver al menú principal")
        opcion = input("")

        if opcion == "1":
            print("Elija nombre: ")
            nombrecito = input().upper()
            print("Elija tablero: ")
            tablerito=input().lower()
            NomTab = nombrecito+": "+tablerito
            if NomTab in matriz_nombres_guardados:
                IndiceMostrar = matriz_nombres_guardados.index(NomTab)
                MuestraTablero(matriz_tableros_guardados[IndiceMostrar])
                Menu2(NomTab, matriz_tableros_guardados[IndiceMostrar])
            else:
                print(f"No se encontró la partida {tablerito} del jugador {nombrecito}")
                return Menu1()

        elif opcion=="2":
            print()
            print("Volviendo al menú principal...")
            print()
            print()
            return MenuPrincipal()

        else:
            print("Elije una opción válida")
            return Menu1()

def Menu2(NameTotal,tab):
    print("(1) Cargar partida")
    print("(2) Borrar Partida")
    print("(3) Regresar al menú principal")
    opcion = input("")
    if opcion == "1":
        return continuaTablero(tab)
    elif opcion == "2":
        return borraPartida(NameTotal)
    elif opcion == "3":
        print("Volviendo al menú principal...")
        print()
        print()
        return MenuPrincipal()
    else:
        print()
        print("Elige una opción válida")
        print()
        return Menu2(NameTotal, tab)

def modValor(matriz):
    filita = int(input("👉 Ingrese fila    : "))
    columnita = int(input("👉 Ingrese columna : "))
    valor = int(input("👉 Ingrese valor   : "))
    print()
    if Regla_1(filita) and Regla_1(columnita) and Regla_1(valor):
        PosiblesHorizontales = RetornaPosiblesHorizontal(matriz,filita-1,columnita-1)#
        PosiblesVerticales = RetornaPosiblesVertical(matriz,filita-1,columnita-1)#
        PosibleCuadricula = RetornaPosiblesCuadrante(matriz,filita-1,columnita-1)#
        PosiblesNetos = []
    else:
        print()
        print("Ingresa un valor entre 1 y 9 :D")
        print()
        print()
        return continuaTablero(matriz)

    Cumplimiento =False

    if (valor in PosiblesHorizontales) and (valor in PosiblesVerticales) and (valor in PosibleCuadricula):
        PosiblesNetos.append(valor)
        Cumplimiento = True

    if Regla_1(valor) and (valor in PosiblesNetos) and Cumplimiento:
        matriz[filita-1][columnita-1] = valor
    else:
        print()
        print("Ingresa un valor que cumpla las reglas :D")
        print("*Recuerda que los números no se deben repetir")
        print("en las filas, columnas ni cuadrantes de 3x3*")
        print()
        print()

    return continuaTablero(matriz)

def continuaTablero(sudoku):
    MuestraTablero(sudoku)
    print()
    print("◤--", "                 ", "--◥")
    print("|", "(1) Seguir jugando", "   ", "|")
    print("|", "(2) Guardar partida", "  ", "|")
    print("|", "(3) Volver al menu", "   ", "|")
    print("◣--", "                 ", "--◢")
    opcion = input()
    if opcion == "1":
        return modValor(sudoku)
    elif opcion == "2":
        return guardaPartida(sudoku, matriz_nombres_guardados, matriz_tableros_guardados)
    elif opcion == "3":
        print()
        print("Volviendo al menú principal...")
        print()
        print()
        return MenuPrincipal()
    else:
        print("Ingresa una opción válida entre 1 y 3 ☻")
        return continuaTablero(sudoku)

