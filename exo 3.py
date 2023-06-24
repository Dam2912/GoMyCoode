
#avec la methode index
string=input('entre une chaine de caractère: ')
for i in string:
    if (string.index(i)) % 2 == 0:
        print(i,end='')

#aveec la notion de [debut:fi:pas]
string=input('entre une chaine de caractère: ')
print(*string[::2])

#aveec la notion de [debut:fi:pas] et loop
string=input('entre une chaine de caractère: ')
for i in string[::2]:
    print(i,end='')