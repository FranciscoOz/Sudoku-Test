import random
tablero_principal = [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]
contador = 19
for i in range (9):
  for j in range (9):
    if contador!=0:
      tablero_principal[random.randrange(1,9)][random.randrange(1,9)]=random.randrange(1,9)
      contador-=1

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
#asasa
######qwqwqwqwqwqwqwqwqw
