""""" version 1 simple
for i in range(1, 6):
    print((str(i) + ' ') * i)
"""

#version avec l'intruction qui va a la ligne des que null est detecté
for i in range(1, 6):
    for j in range(i):
        print(i, end=' ')
    print()

