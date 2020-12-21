# import json
# matriz_nombres_guardados = []
# matriz_tableros_guardados = []
# archi=open("sodoko.json","r")
# jSud=json.load(archi)
# archi.close()
# jSudNom = jSud.keys()
# jSudTab = jSud.values()
# for i in jSudNom:
#     matriz_nombres_guardados.append(i)
# for i in jSudTab:
#     matriz_tableros_guardados.append(i)
#
#
#
#
#
#
import random
# #Guardar
# DICtemp = dict()
# archi = open("sodoko.json","w")
# for i in range (len(matriz_tableros_guardados)):
#     DICtemp[matriz_nombres_guardados[i]]=matriz_tableros_guardados[i]
# #print(jSud)
# json.dump(DICtemp, archi)
# #print(type(jSud))
# archi.close()




class Clr:
   PP = '\033[95m'
   CN = '\033[96m'
   DC = '\033[36m'
   BL = '\033[94m'
   GR = '\033[92m'
   YW = '\033[93m'
   RD = '\033[91m'
   BD = '\033[1m'
   UL = '\033[4m'
   END = '\033[0m'


print()
print("🎅♥☻♠☻♣☻♦☻ - SUDOKU 2.0 - ☻♦☻♣☻♠☻♥💔")
print("🎅                                      💔")
print('\033[34m',end="")
print("🎅    ", "🏆🏆🏆"," MENÚ PRINCIPAL", " 🏆🏆       💔")
print(Clr.END,end="")
print('\033[94m',end="")
print("🎅                                      💔")
print("🎅    ", "❄","(1) Jugar tablero nuevo", "           ")
print("🎅    ", "❄","(2) Ver/Jugar tablero guardado", "    ")
print("🎅    ", "❄","(3) Finalizar", "                     ")
print("🎅                                         💔")
print("🎅♥☻♠☻♣☻♦☻ -------------- ☻♦☻♣☻♠☻♥💔" + Clr.END)