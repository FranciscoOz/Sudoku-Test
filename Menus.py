matriz_nombres_guardados =["PEPE"]
matriz_tableros_guardados=[["pepito"]]
matriz = [["j"],["an"]]
#Guardar partida
def guardaPartida(matriz):
    nombre_jugador=input("Ingrese nombre de la partida/jugador").upper()
    matriz_tableros_guardados.append([matriz])
    matriz_nombres_guardados.append(nombre_jugador)

guardaPartida(matriz)

print(matriz_nombres_guardados)
print(matriz_tableros_guardados)

#Carga partida
def cargaPartida():
    nombre_jugador = input("Ingresa nombre de tablero/jugador: ").upper()
    posicion = int(matriz_nombres_guardados.index(nombre_jugador))
    matriz_resultado = matriz_tableros_guardados[posicion]
    return matriz_resultado
cargaPartida()
print(matriz_tableros_guardados)
print(matriz_nombres_guardados)
