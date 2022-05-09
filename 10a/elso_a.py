# Három pozitív egész szám számtani közepének meghatározása!
from os import system
system('cls')

elsoSzam = int(input('Kérem az első pozitív egész számot: '))
masodikSzam = int(input('Kérem a második pozitív egész számot: '))
harmadikSzam = int(input('Kérem a harmadik pozitív egész számot: '))

if elsoSzam > 0 and masodikSzam > 0 and harmadikSzam > 0:
    szamtaniKozep = (elsoSzam + masodikSzam + harmadikSzam) / 3

    szoveg = 'A három pozitív egész szám számtani közepe: {}'.format(szamtaniKozep)
    print(szoveg)
else: 
    szoveg = 'Nem megfelelő számokat adtál meg!'
    print(szoveg)