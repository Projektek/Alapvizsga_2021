# Felhasználó által megadott pozitív egész számok mértani közepének meghatározása metódusok segítségével két tizedes jegyre kerekítve.
from os import system
import math
system('cls')

def szamBekeres():
    szam = int(input('Kérek egy pozitív egész számot: '))

    while szam < 0:
        print('Negatív számot adtál meg!')
        szam = int(input('Kérek egy pozitív egész számot: '))
    
    return szam
        
def mertaniKozepSzamol(lista):
    szorzat = 1
    for x in lista:
        szorzat = szorzat * x
    mertaniKozep = math.pow(szorzat, 1 / len(lista))

    szoveg = 'A számok mértani közepe: {:.2f}'.format(mertaniKozep)
    print(szoveg)  

meddig = int(input('Hány számmal számoljak: '))

szamLista = []

for i in range(meddig):
    szam = szamBekeres()
    szamLista.append(szam)

mertaniKozepSzamol(szamLista)