#version simple
def conv(heure):
    conversion = heure *60*60

    return conversion

heure=int(input('veuillez entrer une heure: '))

print(conv(heure),'secondes')


#version caractere
def heure_en_secondes(heure):
    heures, minutes, secondes = heure.split(':')
    conversion = int(heures) * 3600 + int(minutes) * 60 + int(secondes)
    return conversion

heure = input('veuillez entrer une heure au format "heure:minutes:secondes": ')
secondes = heure_en_secondes(heure)
print('cela représente : ',secondes)

