#test si nombre en utilisant Lambda

string = input("input : ")
is_digit = lambda char: char.isdigit()
result = [(char, "est un chiffre") if is_digit(char) else (char, "n'est pas un chiffre") for char in string]

for char, message in result:
    print(char, message)

""""
Note à moi meme, j'ai galérer pour faire un code court. 

Cette partie du code utilise une boucle for pour itérer sur chaque élément de la liste result. Chaque élément de la liste result est un tuple contenant deux éléments : char (le caractère de la chaîne) et message (le message indiquant si le caractère est un chiffre ou non).

L'instruction for char, message in result: décompose chaque tuple de la liste result en ses deux éléments, char et message. Cela signifie que pour chaque itération de la boucle, les variables char et message prendront les valeurs correspondantes du tuple actuel.

Ensuite, l'instruction print(char, message) est utilisée pour afficher le caractère char suivi du message message. Cela affiche le caractère de la chaîne et indique si le caractère est un chiffre ou non, selon les résultats obtenus à l'aide de l'expression lambda.

Ainsi, cette partie du code permet d'afficher chaque caractère de la chaîne string avec un message correspondant indiquant s'il s'agit d'un chiffre ou non.
"""

