#Nombre Parfait

#version avec un package

from sympy import divisors

nombre = input('entrez un nombre svp : ')
nombre = int(nombre)
diviseurs = divisors(nombre)
print("Les diviseurs de", nombre, "sont", (diviseurs))

#test si lui meme est dans la liste
if nombre in diviseurs:
    diviseurs.pop()

print('nouvelle liste : ', diviseurs)

#verification si nombre perfect
if sum(diviseurs) == nombre:
    print('Nombre perfect')
else:
    print('Pas Nombre perfect')




#version avec calcul des diviseurs à la main

print('Version 2 avec une fonction perso pour trouver la liste de diviseurs')

def liste_diviseurs(nombre):
    diviseurs = []
    for i in range(1, nombre + 1):
        if nombre % i == 0:
            diviseurs.append(i)
    return diviseurs

nombre = nombre
diviseurs = liste_diviseurs(nombre)
print("Les diviseurs de", nombre, "sont", diviseurs)

#test si lui meme est dans la liste
if nombre in diviseurs:
    diviseurs.pop()

print('nouvelle liste : ', diviseurs)

#verification si nombre perfect
if sum(diviseurs) == nombre:
    print('Nombre perfect')
else:
    print('Pas Nombre perfect')