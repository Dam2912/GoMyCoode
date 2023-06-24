#vérifier si une liste est un palindrome

def is_pala(liste):
    if liste==liste[::-1]:
        outpout = True
    else:
        outpout = False

    return outpout


#list1 = [1,2,3,2,1]
list1 = input('input :  ')
list1 = list(list1)
print(is_pala(list1))