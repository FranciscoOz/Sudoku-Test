import random
matriz_nombres_guardados =["PEPE"]
matriz_tableros_guardados=[["pepito"]]
matriz = [["j"],["an"]]

#Genera Matriz Inicial
def CreaMatrizInicial():
    tablero_principal = []  #CREA TABLERO DE JUEGO 9X9 CON 0's
    for i in range (9):
        tablero_principal.append([])
        for j in range (9):
            tablero_principal[i].append(0)
    contador = 19   #RELLENAMOS CON NUMEROS ALEATORIOS ALGUNAS CASILLAS SEGÚN CONTADOR Y CUMPLIENDO LAS REGLAS
    for i in range (9):
        for j in range (9):
            if contador!=0:
                tablero_principal[random.randrange(1,9)][random.randrange(1,9)]=random.randrange(1,9)
            contador-=1

    return tablero_principal

#Genera Tablero visible
def CreaTablero (tablero_principal):
    print("  | 1 2 3  | 4 5 6  | 7 8 9 |")
    for i in range(9):  #CREA TABLERO VACIO
        if i%3==0:
            print("---------------------------")
        print(i, end="")
        for j in range(9):
            if j%3==0:
                print(" | ", end="")
            if j== 8:
                print(tablero_principal[i][j], "|")
            else:
                print(str(tablero_principal[i][j]) + " ", end="")
        if i==8:
            print("-----------------------------")

#Nueva partida
def nuevaPartida():
    nombre_jugador = input("Ingresa tu nombre: ").upper()
    nombre_tablero = input("Ingresa nombre para el tablero: ").upper()
    matriz = CreaMatrizInicial()
    matriz_tableros_guardados.append([matriz])
    matriz_nombres_guardados.append(nombre_jugador)
    CreaTablero(matriz)


#Guardar partida
def guardaPartida(matriz):
    nombre_jugador=input("Ingrese nombre de la partida/jugador").upper()
    matriz_tableros_guardados.append([matriz])
    matriz_nombres_guardados.append(nombre_jugador)

nuevaPartida()

print(matriz_nombres_guardados)
print(matriz_tableros_guardados)

#Carga partida
def cargaPartida():
    nombre_jugador = input("Ingresa nombre de tablero/jugador: ").upper()
    posicion = int(matriz_nombres_guardados.index(nombre_jugador))
    matriz_resultado = matriz_tableros_guardados[posicion][0]
    CreaTablero(matriz_resultado)
print(matriz_tableros_guardados)
print(matriz_nombres_guardados)
cargaPartida()
