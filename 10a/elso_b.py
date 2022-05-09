# Két pozitív egész szám mértani közepének meghatározása!
from os import system
import math
system('cls')

elsoSzam = int(input('Kérem az első pozitív egész számot: '))
masodikSzam = int(input('Kérem a második pozitív egész számot: '))

if elsoSzam > 0 and masodikSzam > 0:
    mertaniKozep = math.sqrt(elsoSzam * masodikSzam) 

    szoveg = 'A két pozitív egész szám mértani közepe: {}'.format(mertaniKozep)
    print(szoveg)
else:
    szoveg = 'Nem megfelelő számokat adtál meg!'
    print(szoveg)