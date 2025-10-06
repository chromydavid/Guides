# FOR CYKLUS

# for cyklus projde daný kód tolikrát kolik je elementů v jeho vstupu
# např v listu je element oddělen ,
# zapíšeme jako for (název proměnné pro daný element) in range/název vstupu :
numbers = [5, 8, 6, [7,2]]
for number in numbers :
    print(number)
# tento kód projde funkci print() pro každý element listu numbers a nastaví
# jej jako hodnotu number
# v prvním cylku se number = 5 a poté se napíše print(number) kdy number je 5
# v druhém cylku se number = 8 a poté se napíše print(number) kdy number je 8
# atd. až do konce listu
# výsledek :
#5
#8
#6
#[7, 2]

# ve stringu jsou elementy každé písmeno i mezera :
name = "David Chromý"
for letter in name :
    print(letter)
# výsledek :
#D
#a
#v
#i
#d
#
#C
#h
#r
#o
#m
#ý

# funkce range() místo inputu jako proměnné použijeme interval (od do) :
for number in range(0, 2) :
    print(number)
# výsledek :
#0
#1

# range() můžeme doplnit o třetí hodnotu která určuje velikost kroku
# bez třetí hodnoty se jde základně po 1
# interval od 0 do 20(19) ale jdeme po 10 takže 0 a 10 :
for number in range(0, 20, 10) :
    print(number)
# výsledek :
#0
#10

# můžeme jít i po záporných krocích :
for number in range(6, 0, -2) :
    print(number)
# výsledek :
#6
#4
#2

# pozor na nekonečné pole (nebude fungovat) :
for number in range(0, 10, -2) :
    print(number)
#výsledek :
#žádný výsledek nevznikne

# range() lze použít jako samostatnou funkci
# list() vytvoří list ze zadaného inputu :
list = list(range(1,154, 50))
print(list)
# výsldek :
#[1, 51, 101, 151]

# můžeme skládat s podmínkama atd. :
names = ["David", "Lukáš"]
for name in names :
    if name == "Lukáš" :
        print(name,"is lukáš")
    else :
        print(name,"is not lukáš")
# výsledek :
#David is not lukáš
#Lukáš is lukáš
