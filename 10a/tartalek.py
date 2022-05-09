# Három pozitív szám számtani közepe:
from os import system
system('cls')

elsoSzam = int(input('Kérem az első egész számot: '))
masodikSzam = int(input('Kérem a második számot: '))
harmadikSzam = int(input('Kérem a harmadik egész számot: '))

if elsoSzam > 0 and masodikSzam > 0 and harmadikSzam > 0:
    szamtaniKozep = (elsoSzam + masodikSzam + harmadikSzam) / 3

    szoveg = 'A három szám számtani közepe: {}'.format(szamtaniKozep)

    print(szoveg)
else: 
    szoveg = 'Nem megfelelő számokat adtál meg!'
    print(szoveg)


# Két pozitív szám mértani közepe:

from os import system
import math
system('cls')

elsoSzam = int(input('Kérem az első pozitív egész számot: '))
masodikSzam = int(input('Kérem a második pozitív egész számot: '))

mertaniKozep = math.sqrt(elsoSzam * masodikSzam) 

szoveg = 'A két pozitív egész szám mértani közepe: {}'.format(mertaniKozep)

print(szoveg)