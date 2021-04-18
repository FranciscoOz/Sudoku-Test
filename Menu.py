import json
from Reglas import *
import random


class Clr:
    PP = '\033[95m'
    CN = '\033[96m'
    DC = '\033[36m'
    BL = '\033[94m'
    GR = '\033[92m'
    GR2 = '\033[34m'
    YW = '\033[93m'
    RD = '\033[91m'
    BD = '\033[1m'
    UL = '\033[4m'
    END = '\033[0m'
    WH = '\033[97m'

    def colorAlAzar(self):
        index = random.randint(0, 10)
        listaColors = ['\033[31m', '\033[32m', '\033[33m', '\033[34m', '\033[35m', '\033[36m', '\033[91m', '\033[92m',
                       '\033[93m', '\033[94m', '\033[95m', '\033[96m', ]
        return print(listaColors[index], end="")


matriz_nombres_guardados = list()
matriz_tableros_guardados = list()

# JSON
if not VerificaExistencia("sudoku.json"):
    DBsudoku = open("sudoku.json", "w+")
    dicNuevo = dict()
    json.dump(dicNuevo, DBsudoku)
    DBsudoku.close()


def leeSudokus():
    global matriz_tableros_guardados, matriz_nombres_guardados
    matriz_nombres_guardados = []
    matriz_tableros_guardados = []
    archi = open("sudoku.json", "r")
    jSud = json.load(archi)
    archi.close()
    jSudNom = jSud.keys()
    jSudTab = jSud.values()
    for i in jSudNom:
        matriz_nombres_guardados.append(i)
    for i in jSudTab:
        matriz_tableros_guardados.append(i)


def IntroduceJSON():
    DICtemp = dict()
    archi = open("sudoku.json", "w")
    for i in range(len(matriz_tableros_guardados)):
        DICtemp[matriz_nombres_guardados[i]] = matriz_tableros_guardados[i]
        if matriz_tableros_guardados[i] == "vacío":
            del DICtemp[matriz_nombres_guardados[i]]
    json.dump(DICtemp, archi)
    archi.close()


# Menus
def MenuPrincipal():
    print()
    print(Clr.WH + "🎅♥☻♠☻♣☻♦☻ - - SUDOKU 2.0 - - ☻♦☻♣☻♠☻♥🎅" + Clr.END)
    print(Clr.CN + "🎅                                          🎅" + Clr.END)
    print(Clr.CN + "🎅    " + Clr.END, Clr.YW + "🏆🏆🏆" + Clr.END,
          Clr.BL + Clr.BD + " MENÚ PRINCIPAL" + Clr.END + Clr.END, Clr.YW + " 🏆🏆          " + Clr.END,
          Clr.CN + f"🎅" + Clr.END)
    print(Clr.CN + "🎅                                          🎅" + Clr.END)
    print(Clr.CN + "🎅    " + Clr.END, Clr.WH + "❄❄" + Clr.END,
          Clr.GR2 + Clr.BD + "(1) Jugar tablero nuevo" + Clr.END + Clr.END, "        ", Clr.CN + "🎅" + Clr.END)
    print(Clr.CN + "🎅    " + Clr.END, Clr.WH + "❄❄" + Clr.END,
          Clr.GR2 + Clr.BD + "(2) Ver/Jugar tablero guardado" + Clr.END + Clr.END, " ", Clr.CN + "🎅" + Clr.END)
    print(Clr.CN + "🎅    " + Clr.END, Clr.WH + "❄❄" + Clr.END, Clr.GR2 + Clr.BD + "(3) Finalizar" + Clr.END + Clr.END,
          "                  ", Clr.CN + "🎅" + Clr.END)
    print(Clr.CN + "🎅                                          🎅" + Clr.END)
    print(Clr.DC + "🎅♥☻♠☻♣☻♦☻ ------------------ ☻♦☻♣☻♠☻♥🎅" + Clr.END)
    opcion = input()
    return menuOpciones(opcion)


def menuOpciones(opcion):
    if opcion == "1":
        print(Clr.DC + " --------------------" + Clr.END)
        print(Clr.DC + "|" + Clr.END, " 👇", Clr.BD + Clr.WH + " Dificultad" + Clr.END + Clr.END, end="")
        print(Clr.DC + "    |" + Clr.END)
        print(Clr.DC + "|" + Clr.END, Clr.BD + "(1)", Clr.GR + " Fácil   (🤡) " + Clr.END + Clr.END,
              Clr.DC + "|" + Clr.END)
        print(Clr.DC + "|" + Clr.END, Clr.BD + "(2)", Clr.YW + " Medio   (😈) " + Clr.END + Clr.END,
              Clr.DC + "|" + Clr.END)
        print(Clr.DC + "|" + Clr.END, Clr.BD + "(3)", Clr.RD + " Difícil (💀) " + Clr.END + Clr.END,
              Clr.DC + "|" + Clr.END)
        print(Clr.DC + " --------------------" + Clr.END)
        dificultad = input()
        sudoku = CreaMatrizInicial()
        RellenaCuadrante(sudoku)
        ResuelveCifra(sudoku)
        mode = ["1", "2", "3"]
        if dificultad in mode:
            RellenaCeros(sudoku, dificultad)
        else:
            print("Escoge una dificultad válida >:)")
            return menuOpciones(opcion)
        continuaTablero(sudoku)
        print()
        print()
        return sudoku

    elif opcion == "2":
        print()
        print("Cargando tableros...", end="")
        Menu1()

    elif opcion == "3":
        print(Clr.WH + Clr.BD + "- - Fin de juego - -")
        return IntroduceJSON()
    else:
        print("Ingresa una opción válida entre 1 y 3 ☻\n")
        print()
        return MenuPrincipal()


def Menu1():
    leeSudokus()
    print()
    print()
    print(Clr.BD + " ____________________" + Clr.END)
    print(Clr.BD + "|" + Clr.END, "\033[03m" + Clr.BD + "\033[93m" + "TABLEROS GUARDADOS" + Clr.END,
          Clr.BD + "|" + Clr.END)
    print("➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")
    c = 0
    for i in matriz_nombres_guardados:
        if matriz_tableros_guardados[c] != "vacío":
            Clr().colorAlAzar()
            print("\033[03m" + i + Clr.END)
            print("➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")
        c += 1

    # Comprobar si no hay matrices
    EstaVacio = True
    for i in matriz_tableros_guardados:
        if i != "vacío":
            EstaVacio = False

    if EstaVacio:
        print("No hay tableros guardados")
        print("• (0) Desea volver al menú principal")
        print("• (1) Desea salir del juego?")
        opcion = input()
        if opcion == "0":
            return MenuPrincipal()
        elif opcion == "1":
            print("- - Fin de juego - -")
            return IntroduceJSON()
        else:
            print("Ingresa una opción válida :)")
            return Menu1()

    else:
        print("Desea ver detalles del tablero? ")
        print("♦ (1) Sí")
        print("♦ (2) No y volver al menú principal")
        opcion = input("")

        if opcion == "1":
            cargaPartida()

        elif opcion == "2":
            print()
            print("Volviendo al menú principal...")
            print()
            print()
            return MenuPrincipal()

        else:
            print("Elije una opción válida")
            return Menu1()


def Menu2(NameTotal, tab):
    print()
    print("|", "👉 (1) Cargar partida", Clr.CN + "🔻" + Clr.END)
    print("|", "👉 (2) Borrar Partida", "\033[31m" + "❌" + Clr.END)
    print("|", "👉 (3) Regresar a las partidas guardadas", Clr.BD + "↩" + Clr.END)
    opcion = input("")
    if opcion == "1":
        return continuaTablero(tab)
    elif opcion == "2":
        return borraPartida(NameTotal)
    elif opcion == "3":
        print()
        return Menu1()
    else:
        print()
        print("Elige una opción válida")
        print()
        return Menu2(NameTotal, tab)


def continuaTablero(sudoku):
    MuestraTablero(sudoku)
    print()
    print(Clr.YW + "◤--", "                 ", "--◥")
    print(Clr.YW + "|", Clr.WH + "(0) Seguir jugando" + Clr.END, "   ", Clr.YW + "|")
    print(Clr.YW + "|", Clr.WH + "(1) Solucionar tablero" + Clr.END, Clr.YW + "|")
    print(Clr.YW + "|", Clr.WH + "(2) Guardar partida" + Clr.END, "  ", Clr.YW + "|")
    print(Clr.YW + "|", Clr.WH + "(3) Volver al menu" + Clr.END, "   ", Clr.YW + "|")
    print(Clr.YW + "◣--", "                 ", "--◢")
    opcion = input()
    if opcion == "0":
        return modValor(sudoku)
    elif opcion == "1":
        if BuscaVacio(sudoku):
            ResuelveCifra(sudoku)
            if BuscaVacio(sudoku):
                print("No hay solución :c")
        else:
            print("Ya está resuelto :)")
        return continuaTablero(sudoku)
    elif opcion == "2":
        return guardaPartida(sudoku)
    elif opcion == "3":
        print()
        print("Volviendo al menú principal...")
        print()
        print()
        return MenuPrincipal()
    else:
        print("Ingresa una opción válida entre 1 y 3 ☻")
        return continuaTablero(sudoku)


def guardaPartida(matriz):
    leeSudokus()
    nombre_jugador = input("Ingrese nombre del jugador: ").upper()
    nombre_tablero = input("Ingrese nombre de la partida: ").lower()
    nombre_total = nombre_jugador + ": " + nombre_tablero
    if nombre_total not in matriz_nombres_guardados:
        matriz_tableros_guardados.append(matriz)
        matriz_nombres_guardados.append(nombre_total)
        IntroduceJSON()
    else:
        print("Ya existe esa partida. Desea sobreescribir?: ")
        print("(1) Sí")
        print("(2) No")
        opcion = input()
        if opcion == "1":
            index = int()
            for i in matriz_nombres_guardados:
                if i == nombre_total:
                    index = matriz_nombres_guardados.index(i)
            matriz_tableros_guardados[index] = matriz
            IntroduceJSON()
        elif opcion == "2":
            guardaPartida(matriz)
        else:
            print("Ingrese una opción válida")

    return continuaTablero(matriz)


def cargaPartida():
    nombre_jugador = input("Ingresa nombre de jugador: ").upper()
    nombre_partida = input("ingresa nombre de partida: ").lower()
    nombreTotal = nombre_jugador + ": " + nombre_partida
    if nombreTotal in matriz_nombres_guardados:
        posicion = int(matriz_nombres_guardados.index(nombreTotal))
        matriz_resultado = matriz_tableros_guardados[posicion]
        print()
        MuestraTablero(matriz_resultado)
        return Menu2(nombreTotal, matriz_resultado)
    else:
        print(f"No se encontró la partida {nombre_partida} del jugador {nombre_jugador}")
        return Menu1()


def borraPartida(nombre):
    IndexM = matriz_nombres_guardados.index(nombre)
    matriz_tableros_guardados[IndexM] = "vacío"
    IntroduceJSON()
    return Menu1()


def MuestraTablero(tablero_principal):
    print(Clr.WH + Clr.BD + "  | 1  2  3  | 4  5  6  | 7  8  9 |" + Clr.END + Clr.END)
    for i in range(9):
        if i % 3 == 0:
            print(Clr.WH + "➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖" + Clr.END)
            print(Clr.WH + "------------------------------------" + Clr.END)
        print(Clr.WH + Clr.BD + f"{i + 1}" + Clr.END + Clr.END, end=" ")
        for j in range(9):
            if j % 3 == 0:
                print(Clr.WH + Clr.BD + "| " + Clr.END + Clr.END, end="")
            if j == 8:
                if tablero_principal[i][j] == "0":
                    print(Clr.WH + Clr.BD + str(tablero_principal[i][j]) + Clr.END + Clr.END,
                          Clr.WH + Clr.BD + "|" + Clr.END + Clr.END)
                else:
                    print(Clr.PP + tablero_principal[i][j] + Clr.END, Clr.WH + Clr.BD + "|" + Clr.END + Clr.END)
            else:
                if tablero_principal[i][j] == "0":
                    print(Clr.WH + Clr.BD + str(tablero_principal[i][j]) + Clr.END + Clr.END + "  ", end="")
                else:
                    print(Clr.PP + str(tablero_principal[i][j]) + Clr.END + "  ", end="")
        if i == 8:
            print(Clr.WH + "➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖" + Clr.END)


# Funcionalidades
def CreaMatrizInicial():
    tablero = []
    for i in range(9):
        tablero.append([])
        for j in range(9):
            tablero[i].append("0")
    return tablero


def RellenaCuadrante(tabla):
    for n in range(3):
        disponibles = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        for i in range(n * 3, (n * 3) + 3):
            for j in range(n * 3, (n * 3) + 3):
                tabla[i][j] = random.choice(disponibles)
                disponibles.remove(tabla[i][j])


def RellenaCeros(tabla, nivel):
    maxceros = 0
    if nivel == "1":
        maxceros = 0
    elif nivel == "2":
        maxceros = 40
    elif nivel == "3":
        maxceros = 60
    for i in range(maxceros):
        n = random.randint(0, 8)
        m = random.randint(0, 8)
        tabla[n][m] = "0"


def modValor(matriz):
    fila = input("👉 Ingrese fila    : ")
    columna = input("👉 Ingrese columna : ")
    valor = input("👉 Ingrese valor   : ")
    print()
    filaB = EntreUnoNueve(fila)
    columnaB = EntreUnoNueve(columna)
    valorB = EntreUnoNueve(valor)

    if filaB and columnaB and valorB:
        if ValidaCifra(matriz, valor, int(fila), int(columna)):
            matriz[int(fila) - 1][int(columna) - 1] = valor
        else:
            print("El valor de la cifra no debe repetirse en fila, columna o cuadrante :) \n")
    else:
        if filaB:
            print("El valor de la fila debe estar entre 1 y 9 :) \n")
        if columnaB:
            print("El valor de la columna debe estar entre 1 y 9 :) \n")
        if valorB:
            print("El valor de la casilla debe estar entre 1 y 9 :) \n")

    return continuaTablero(matriz)
