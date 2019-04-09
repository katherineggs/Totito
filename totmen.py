def tottito_1():
    print("OPCION 1")
    print("Totito Normal")
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
    def tablero(tab):
        for i in tab:
            print(i)
        return ""
    x = "X"
    o = "O"
    player1 = input("Nombre jugador 1: ")
    player2 = input("Nombre jugador 2: ")
    print(tablero(tab))
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
    def win(tab,ficha_1,ficha_2, jugador):
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
                print("ganador", jugador )
            elif e == ficha_2:
                print("ganador", e)
            ganador = 1
        if d == f and f == g:
            if d == ficha_1:
                print("ganador", jugador )
            elif d == ficha_2:
                print("ganador", d)
            ganador = 1
        if c == v and v == b:
            if c == ficha_1:
                print("ganador", jugador )
            elif c == ficha_2:
                print("ganador", c)
            ganador = 1
        if e == d and d == c:
            if e == ficha_1:
                print("ganador", jugador )
            elif e == ficha_2:
                print("ganador", e)
            ganador = 1
        if r == f and f == v:
            if r == ficha_1:
                print("ganador", jugador )
            elif r == ficha_2:
                print("ganador", r)
            ganador = 1
        if t == g and g == b:
            if t == ficha_1:
                print("ganador", jugador )
            elif t == ficha_2:
                print("ganador", t)
            ganador = 1
        if e == f and f == b:
            if e == ficha_1:
                print("ganador", jugador )
            elif e == ficha_2:
                print("ganador", e)
            ganador = 1
        if t == f and f == c:
            if t == ficha_1:
                print("ganador", jugador )
            elif t == ficha_2:
                print("ganador", t)
            ganador = 1
        return ganador
    ganador = 0
    turno = jugador
    while ganador == 0:
        ganador = win(tab,ficha_1,ficha_2, jugador)
        if turno == jugador:
            print(jugador)
            posicion = input("Posicion: ")
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
            if posicion not in var:
                print("Ubicacion invalida.")
                print(jugador)
                posicion = input("Posicion: ")
            for i in tab:
                for b in i:
                    for a in b:
                        if a == posicion:
                            tab = [[i.replace(a, ficha_2) for i in b] for b in tab]
                            print(tablero(tab))
                            if turno == player1:
                                turno = player2
                            elif turno == player2:
                                turno = player1
        ganador = win(tab,ficha_1,ficha_2, jugador)
    return ""

def totitofuncion2():
    import random
    vocales = ["a", "e", "i", "o", "u"]
    cons = ["b","br","bl","c","cr","cs","d","dr","f","fr","fl","g","h","j","k","l","ll","m","n","p","pr","qu","r","rr","s","t","v","w"]
    largo = [3,4]
    l = random.choice(largo)
    nombre_comp = ""
    z = 1
    while z < l:
        comp = random.choice(cons) + random.choice(vocales)
        nombre_comp = nombre_comp + comp
        z = z + 1
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
    print("OPCION 2")
    print("Usuario vs. Computadora")
    player1 = input("Nombre jugador: ")
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
    def win(tab,ficha_1,ficha_2, jugador):
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
                print("ganador", jugador )
            elif e == ficha_2:
                print("ganador", e)
            ganador = 1
        if d == f and f == g:
            if d == ficha_1:
                print("ganador", jugador )
            elif d == ficha_2:
                print("ganador", d)
            ganador = 1
        if c == v and v == b:
            if c == ficha_1:
                print("ganador", jugador )
            elif c == ficha_2:
                print("ganador", c)
            ganador = 1
        if e == d and d == c:
            if e == ficha_1:
                print("ganador", jugador )
            elif e == ficha_2:
                print("ganador", e)
            ganador = 1
        if r == f and f == v:
            if r == ficha_1:
                print("ganador", jugador )
            elif r == ficha_2:
                print("ganador", r)
            ganador = 1
        if t == g and g == b:
            if t == ficha_1:
                print("ganador", jugador )
            elif t == ficha_2:
                print("ganador", t)
            ganador = 1
        if e == f and f == b:
            if e == ficha_1:
                print("ganador", jugador )
            elif e == ficha_2:
                print("ganador", e)
            ganador = 1
        if t == f and f == c:
            if t == ficha_1:
                print("ganador", jugador )
            elif t == ficha_2:
                print("ganador", t)
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
    return ""

def totitofuncion3():
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
    print("OPCION 3")
    print("Pierde quien haga totito")
    print("")
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
    def loser(tab,ficha_1,ficha_2, jugador):
        perdedor = 0
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
                print("Perdedor", jugador )
            elif e == ficha_2:
                print("Perdedor", e)
            perdedor = 1
        if d == f and f == g:
            if d == ficha_1:
                print("Perdedor", jugador )
            elif d == ficha_2:
                print("Perdedor", d)
            perdedor = 1
        if c == v and v == b:
            if c == ficha_1:
                print("Perdedor", jugador )
            elif c == ficha_2:
                print("Perdedor", c)
            perdedor = 1
        if e == d and d == c:
            if e == ficha_1:
                print("Perdedor", jugador )
            elif e == ficha_2:
                print("Perdedor", e)
            perdedor = 1
        if r == f and f == v:
            if r == ficha_1:
                print("Perdedor", jugador )
            elif r == ficha_2:
                print("Perdedor", r)
            perdedor = 1
        if t == g and g == b:
            if t == ficha_1:
                print("Perdedor", jugador )
            elif t == ficha_2:
                print("Perdedor", t)
            perdedor = 1
        if e == f and f == b:
            if e == ficha_1:
                print("Perdedor", jugador )
            elif e == ficha_2:
                print("Perdedor", e)
            perdedor = 1
        if t == f and f == c:
            if t == ficha_1:
                print("Perdedor", jugador )
            elif t == ficha_2:
                print("Perdedor", t)
            perdedor = 1
        return perdedor
    perdedor = 0
    turno = jugador
    while perdedor == 0:
        perdedor = loser(tab,ficha_1,ficha_2, jugador)
        if turno == jugador:
            print(jugador)
            posicion = input("Posicion: ")
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
            if posicion not in var:
                print("Ubicacion invalida.")
                print(jugador)
                posicion = input("Posicion: ")
            for i in tab:
                for b in i:
                    for a in b:
                        if a == posicion:
                            tab = [[i.replace(a, ficha_2) for i in b] for b in tab]
                            print(tablero(tab))
                            if turno == player1:
                                turno = player2
                            elif turno == player2:
                                turno = player1
        perdedor = loser(tab,ficha_1,ficha_2, jugador)
    return ""

print("___ TOTITO ___")
print("")
print("1. Jugador vs Jugador")
print("2. Jugador vs PC")
print("3. Totito Inverso")
opcion = int(input("Que version desea jugar? "))
if opcion == 1:
    tottito_1()
elif opcion == 2:
    totitofuncion2()
elif opcion == 3:
    totitofuncion3()
