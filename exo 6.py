for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()



''''
Dans l'appel range(start, stop, step) :

start représente la valeur de départ de la séquence.
stop représente la valeur à laquelle la séquence s'arrête avant de l'atteindre.
step représente le pas ou l'incrément entre les nombres successifs de la séquence.
Dans le cas de range(5, 0, -1), la séquence générée sera décroissante, commençant par 5 et diminuant de 1 à chaque itération, jusqu'à ce qu'elle atteigne la valeur 0 (qui est exclue).

La séquence générée sera donc : 5, 4, 3, 2, 1.

Vous pouvez utiliser cette séquence dans une boucle for pour itérer sur les nombres de manière décroissante. Par exemple :
'''

