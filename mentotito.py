import totitofuncion1
import TOTITO_2
import TOTITO_3
print("___ TOTITO ___")
print("")
print("1. Jugador vs Jugador")
print("2. Jugador vs PC")
print("3. Totito Inverso")
opcion = int(input("Que version desea jugar? "))
if opcion == 1:
    print(totitofuncion1.tottito_1())
if opcion == 2:
    print(TOTITO_2.totitofuncion2())
if opcion == 3:
    print(TOTITO_3.totitofuncion3())
