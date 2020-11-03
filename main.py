import random as random
#Hola carebola

#CREA TABLERO DE JUEGO 9X9 CON 0's
tablero_principal = []
for i in range (9):
    tablero_principal.append([])
    for j in range (9):
        tablero_principal[i].append(0)

#RELLENAMOS CON NUMEROS ALEATORIOS ALGUNAS CASILLAS SEGÚN CONTADOR Y CUMPLIENDO LAS REGLAS
contador = 19
Cumple = True
for i in range (9):
  for j in range (9):
    if tablero_principal[i][j]==tablero_principal[i+1][j+1] Cumpe
    if contador!=0 and Cumple:
      tablero_principal[random.randrange(1,9)][random.randrange(1,9)]=random.randrange(1,9)
      contador-=1


#CREA TABLERO VACIO
for i in range(9):
        if i%3==0:
            print("- - - - - - - - - - - - - ")
        for j in range(9):
            if j%3==0:
                print(" | ", end="")
            if j== 8:
                print(tablero_principal[i][j])
            else:
                print(str(tablero_principal[i][j]) + " ", end="")
