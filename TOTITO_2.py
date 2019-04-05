import random
vocales = ["a", "e", "i", "o", "u"]
cons = ["b","br","bl","c","cr","cs","d","dr","f","fr","fl","g","h","j","k","l","ll","m","n","p","pr","qu","r","rr","s","t","v","w"]
titl = ["Dr. ","Sr. ", "Srita. ", "Dir. "]
largo = [3,4]
l = random.choice(largo)
nombre_comp = ""
z = 1
while z < l:
    comp = random.choice(cons) + random.choice(vocales)
    nombre_comp = nombre_comp + comp
    z = z + 1

import random
tab = [["      |      |      "],\
           ["  E   |   R  |   T  "],\
           ["______|______|______"],\
           ["      |      |      "],\
           ["  D   |   F  |   G  "],\
           ["______|______|______"],\
           ["      |      |      "],\
           ["  C   |   V  |   B  "],\
           ["      |      |      "]]
var = ["E","R","T","D","F","G","C","V","B"]
def tablero(tab):
    for i in tab:
        print(i)
    return ""
x = "X"
o = "O"
player1 = input("Nombre jugador 1: ")
print("Juegas contra", nombre_comp.upper())
ficha_1 = input("Que ficha desea? (X,O) ")
ficha_2 = ""
if ficha_1 == "X" or ficha_1 == "x":
    ficha_2 = o
    ficha_1 = x
elif ficha_1 == "O" or ficha_1 == "o":
    ficha_2 = x
    ficha_1 = o
else:
    print("Ficha invalida!")
print(tablero(tab))
def win(tab,ficha_1,ficha_2, player1):
    ganador = 0
    e = tab[1][0][2]
    r = tab[1][0][10]
    t = tab[1][0][17]
    d = tab[4][0][2]
    f = tab[4][0][10]
    g = tab[4][0][17]
    c = tab[7][0][2]
    v = tab[7][0][10]
    b = tab[7][0][17]
    if e == r and r == t:
        if e == ficha_1:
            print("Ganador", player1 )
        elif e == ficha_2:
            print("Ganador", nombre_comp)
        ganador = 1
    if d == f and f == g:
        if e == ficha_1:
            print("Ganador", player1 )
        elif e == ficha_2:
            print("Ganador", nombre_comp)
        ganador = 1
    if c == v and v == b:
        if e == ficha_1:
            print("Ganador", player1 )
        elif e == ficha_2:
            print("Ganador", nombre_comp)
        ganador = 1
    if e == d and d == c:
        if e == ficha_1:
            print("Ganador", player1 )
        elif e == ficha_2:
            print("Ganador", nombre_comp)
        ganador = 1
    if r == f and f == v:
        if e == ficha_1:
            print("Ganador", player1 )
        elif e == ficha_2:
            print("Ganador", nombre_comp)
        ganador = 1
    if t == g and g == b:
        if e == ficha_1:
            print("Ganador", player1 )
        elif e == ficha_2:
            print("Ganador", nombre_comp)
        ganador = 1
    if e == f and f == b:
        if e == ficha_1:
            print("Ganador", player1 )
        elif e == ficha_2:
            print("Ganador", nombre_comp)
        ganador = 1
    if t == f and f == c:
        if e == ficha_1:
            print("Ganador", player1 )
        elif e == ficha_2:
            print("Ganador", nombre_comp)
        ganador = 1
    return ganador

ganador = 0
turno = comp
while ganador == 0:
    ganador = win(tab,ficha_1,ficha_2, player1)
    if turno == comp:
        posicion = random.choice(var)
        print("TURNO", nombre_comp.upper() + ":", posicion)
        for i in tab:
            for b in i:
                for a in b:
                    if a == posicion:
                        tab = [[i.replace(a, ficha_2) for i in b] for b in tab]
                        print(tablero(tab))
                        if turno == player1:
                            turno = comp
                        elif turno == comp:
                            turno = player1       
    else:
        print("Tu turno:", player1.upper())
        posicion = input("Posicion: ")
        h = 0
        if posicion not in var:
            print("Ubicacion invalida.")
            print(player1)
            posicion = input("Posicion: ")
        for i in tab:
            for b in i:
                for a in b:
                    if a == posicion:
                        tab = [[i.replace(a, ficha_1) for i in b] for b in tab]
                        print(tablero(tab))
                        if turno == player1:
                            turno = comp
                        elif turno == comp:
                            turno = player1
    ganador = win(tab,ficha_1,ficha_2, player1)