#################################3
###########################
import random
e = "E"
r = "R"
t = "T"
d = "D"
f = "F"
g = "G"
c = "C"
v = "V"
b = "B"
tab = [["      |      |      "],\
       ["  "+e+"   |  "+r+"   |  "+t+"   "],\
       ["______|______|______"],\
       ["      |      |      "],\
       ["  "+d+"   |  "+f+"   |  "+g+"   "],\
       ["______|______|______"],\
       ["      |      |      "],\
       ["  "+c+"   |  "+v+"   |   "+b+"  "],\
       ["      |      |      "]]
var = ["E","e","R","r","T","t","D","d","F","f","G","g","C","c","V","v","B","b"]
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
    if turno == jugador:
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
                    if a == x:
                        h = h + 1
                        print (h)
                        if h == 3:
                            print("Ganador", jugador)
                            ganador = 1
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
                    if a == o:
                        j = j + 1
                        print (jugador,j)
                        if j == 3:
                            print("Ganador", jugador)
                            ganador = 1
                    if a == posicion:
                        tab = [[i.replace(a, ficha_2) for i in b] for b in tab]
                        print(tablero(tab))
                        if turno == player1:
                            turno = player2
                        if turno == player2:
                            turno = player1
                    
                        
    #                     
    # for i in tab:
    #     for b in i:
    #         for c in var:
    #             if c not in var:
    #                 print("Nadie gano")
