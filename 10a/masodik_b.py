# Felhasználó által megadott pozitív egész számok számtani közepének meghatározása metódusok segítségével két tizedes jegyre kerekítve.
from os import system
system('cls')

def szamBekeres():
    szam = int(input('Kérek egy pozitív egész számot: '))

    while szam < 0:
        print('Negatív számot adtál meg!')
        szam = int(input('Kérek egy pozitív egész számot: '))
    
    return szam
        
def szamtaniKozepSzamol(lista):
    osszeg = 0
    for x in lista:
        osszeg = osszeg + x
    szamtaniKozep = osszeg / len(lista)

    szoveg = 'A számok számtani közepe: {:.2f}'.format(szamtaniKozep)
    print(szoveg)  

meddig = int(input('Hány számmal számoljak: '))

szamLista = []

for i in range(meddig):
    szam = szamBekeres()
    szamLista.append(szam)

szamtaniKozepSzamol(szamLista)