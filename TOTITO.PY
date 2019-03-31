#################################3
###########################
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
var = ["E","e","R","r","T","t","D","d","F","f","G","g","C","c","V","v","B","b"]
e = tab[1][0][2]
r = tab[1][0][10]
t = tab[1][0][17]
d = tab[4][0][2]
f = tab[4][0][10]
g = tab[4][0][17]
c = tab[7][0][2]
v = tab[7][0][10]
b = tab[7][0][17]
def tablero(tab):
    for i in tab:
        print(i)
    return ""
x = "X"
o = "O"
player1 = input("Nombre jugador 1: ")
player2 = input("Nombre jugador 2: ")
jugadores =[player1, player2]
jugador = random.choice(jugadores)
print("Inicia", jugador)
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

ganador = 0
turno = jugador
while ganador == 0:
    e = tab[1][0][2]
    r = tab[1][0][10]
    t = tab[1][0][17]
    d = tab[4][0][2]
    f = tab[4][0][10]
    g = tab[4][0][17]
    c = tab[7][0][2]
    v = tab[7][0][10]
    b = tab[7][0][17]
    print(e,r,t,d,f,g,c,v,b)
    if e == r and r == t:
        if e == ficha_1:
            print("Ganador", jugador )
        elif e == ficha_2:
            print("Ganador", e)
        ganador = 1
    elif turno == jugador:
        print(jugador)
        posicion = input("Posicion: ")
        h = 0
        if posicion not in var:
            print("Ubicacion invalida.")
            print(jugador)
            posicion = input("Posicion: ")
        for i in tab:
            for b in i:
                for a in b:
                    if a == posicion:
                        tab = [[i.replace(a, ficha_1) for i in b] for b in tab]
                        print(tablero(tab))
                        if turno == player1:
                            turno = player2
                        elif turno == player2:
                            turno = player1           
    else:
        print(turno)
        posicion = input("Posicion: ")
        j = 0
        if posicion not in var:
            print("Ubicacion invalida.")
            print(jugador)
            posicion = input("Posicion: ")
        for i in tab:
            for b in i:
                for a in b:
                    if a == posicion:
                        print(b.index(a))
                        print("")
                        tab = [[i.replace(a, ficha_2) for i in b] for b in tab]
                        print(tablero(tab))
                        if turno == player1:
                            turno = player2
                        if turno == player2:
                            turno = player1