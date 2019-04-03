import random
vocales = ["a", "e", "i", "o", "u"]
cons = ["b","br","bl","c","cr","cs","d","dr","f","fr","fl","g","h","j","k","l","ll","m","n","p","pr","qu","r","rr","s","t","v","w"]
largo = [2,3,4]
l = random.choice(largo)
nombre_comp = ""
z = 1
while z < 2:
    comp = random.choice(cons) + random.choice(vocales)
    nombre_comp = nombre_comp + comp
    z = z + 1
print(nombre_comp)