from os import system
system('cls')

class Macskafele():
    def __init__(self, lista):
        self.fajta = lista[0]
        self.sebesseg = lista[1]
        self.tomeg = lista[2]

class FileBeolvas():
    def __init__(self, fileNev):
        self.fileNev = fileNev
    
    def olvas(self):
        f = open(self.fileNev, 'r', encoding='utf8')
        elsoSor = f.readline()
        self.macskaLista = []
        for sor in f:
            lista = sor.split(';')
            macska = Macskafele(lista)
            self.macskaLista.append(macska)
        return self.macskaLista

class FileKiir():
    def __init__(self, fileNev):
        self.fileNev = fileNev
    
    def kiir(self, szoveg):
        f = open(self.fileNev, 'w', encoding='utf8')
        f.write(szoveg)

peldanyOlvas = FileBeolvas('macskafelek.txt')
macskak = peldanyOlvas.olvas()

# Leglassabb macskaféle
leglassabb = 1000
leglasssabbMacskafele = ''

for elem in macskak:
    if int(elem.sebesseg) < leglassabb:
        leglassabb = int(elem.sebesseg) 
        leglassabbMacskafele = elem.fajta

print(leglassabbMacskafele)

# Legnehezebb macskaféle
legnehezebb = 0
legnehezebbMacskafele = ''

for elem in macskak:
    if legnehezebb < int(elem.tomeg):
        legnehezebb = int(elem.tomeg)
        legnehezebbMacskafele = elem.fajta

print(legnehezebbMacskafele)

# 60km/h gyorsabb állatok kiíratása a hatvannalGyorsabb.txt állományba

szoveg = '60 km/h-nál gyorsabb macskafélék sebességgel:\n'

for elem in macskak:
    if 60 < int(elem.sebesseg):
        szoveg = szoveg + '{}, {} km/h\n'.format(elem.fajta, elem.sebesseg)

peldanyKiir = FileKiir('hatvannalGyorsabb.txt')
peldanyKiir.kiir(szoveg)