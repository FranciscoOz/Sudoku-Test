#Mismos números en fila o columna
def Regla_1(matriz):
    Cumple = False
    for i in range (9):
        for j in range(9):
            matriz[i][j]
    return Cumple
def borraRepetidos(lista):
    nueva=[]
    for elemento in lista:
        if not elemento in nueva:
            nueva.append(elemento)
        else:
            nueva.append(0)
    return nueva


#Si ingresa letra vuelve a pedir dato o da error
