#using lambda pour square et cube a partir d'une liste


#sans Lambda pour tests
liste = [1, 2, 3, 4, 5]

resultats = [x**2 for x in liste]

print(resultats)  # Affiche [1, 4, 9, 16, 25]


#avec Lambda et for
numbers = [1, 2, 3, 4, 5]

squared_and_cubed = lambda lst: [(x ** 2, x ** 3) for x in lst]

result = squared_and_cubed(numbers)
print(result)


#Avec Lambda et map
numbers = [1, 2, 3, 4, 5]

squared_and_cubed = list(map(lambda x: (x ** 2, x ** 3), numbers))

print(squared_and_cubed)



""""
Dans cet exemple, la fonction carre() est appliquée à chaque élément de la liste nums à l'aide de map(), ce qui renvoie un objet map contenant les résultats. En convertissant cet objet en liste à l'aide de list(), nous obtenons [1, 4, 9, 16, 25], qui est le carré de chaque élément de la liste d'origine.

La fonction map() est souvent utilisée en combinaison avec des fonctions lambda (fonctions anonymes) pour des opérations simples et rapides.
"""