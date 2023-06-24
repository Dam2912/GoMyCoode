#A faire pas compris la consigne : Write a Python function to find the k.th smallest element in a list semble etreun n.min

def nmin(liste, n):
    liste_sorted = sorted(liste)


    if n > len(liste_sorted):
        return "Erreur: n est supérieur à la taille de la liste."

    # Utilisation d'une liste pour stocker les n éléments minimums
    if n==0:
        n=1
    result = (liste_sorted[n-1])

    return result


Liste = [9, 8, 4, 6]
print(sorted(Liste))
print(nmin(Liste, 3))
