from os import system
system('cls')

class Vitamin():
    def __init__(self, lista):
        self.fajta = lista[0]
        self.noiMinimum = lista[1]
        self.ferfiMinimum = lista[2]

class FileBeolvas():
    def __init__(self, fileNev):
        self.fileNev = fileNev
    
    def olvas(self):
        f = open(self.fileNev, 'r', encoding='utf8')
        elsoSor = f.readline()
        self.vitaminLista = []
        for sor in f:
            lista = sor.split(';')
            vitamin = Vitamin(lista)
            self.vitaminLista.append(vitamin)
        return self.vitaminLista

class FileKiir():
    def __init__(self, fileNev):
        self.fileNev = fileNev
    
    def kiir(self, szoveg):
        f = open(self.fileNev, 'w', encoding='utf8')
        f.write(szoveg)

peldanyOlvas = FileBeolvas('vitaminok.txt')
vitaminok = peldanyOlvas.olvas()

# Legkevesebb női minimum
legkevesebb = 10000
legkevesebbNoiMinimum = ''

for elem in vitaminok:
    if float(elem.noiMinimum) < legkevesebb:
        legkevesebb = float(elem.noiMinimum) 
        legkevesebbNoiMinimum = elem.fajta

print(legkevesebbNoiMinimum + ' ' + str(legkevesebb) +  'mg')

# Összes napi férfi minimum
osszes = 0

for elem in vitaminok:
    osszes = osszes + float(elem.ferfiMinimum)

print(str(osszes))

# 1 milligramm-nál kevesebb minimumú női vitaminok kiíratása a egynelKevesebb.txt állományba

szoveg = '1 milligramm-nál kevesebb minimumú női vitamin:\n'

for elem in vitaminok:
    if float(elem.noiMinimum) < 1:
        szoveg = szoveg + '{}, {} milligramm\n'.format(elem.fajta, elem.noiMinimum)

peldanyKiir = FileKiir('egynelKevesebb.txt')
peldanyKiir.kiir(szoveg)