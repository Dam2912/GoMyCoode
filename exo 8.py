rangecible = [2,8]
targerNumber = 4
print(rangecible)
print(targerNumber)

def intervalcheck(rangecible, targerNumber):
    if targerNumber >= min(rangecible) and targerNumber <= max(rangecible):
        print('le target number', targerNumber, ' est bien dans le range: ', rangecible)
    else:
        print('le target number', targerNumber, ' n\'est pas dans le range: ', rangecible)


intervalcheck(rangecible, targerNumber)




