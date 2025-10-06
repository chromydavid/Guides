# FUNKCE
# vyvolatelný modul obsahující funkci, vstupní hodnoty a hodnotu návratu.
# vytvoříme příkazem def poté název funkce a poté do () názvy vstupních hodnot.
# poté vytvoříme operaci ve funkci s proměnnými kteŕe jsem nastavyli do ().
# funkce umí provádět i jiné funkce třeba print().
# poté můžeme tuto funkci kdykoli vyvolat pomocí názvu a do () vstupní hodnoty.
def sum (number1, number2) :
    result = number1 + number2
    print(result)

sum(5, 8)
# výsledek :
#13

# aby funkce vrátila hodnotu využijeme příkaz return .
# return nastavaví název funkce jako proměnnou s výsledkem.
def adition (a, b) :
    result = a + b
    return result

print(adition(5, 2))
# výseldek :
#7

# funkce můžeme i řetězit :
print(adition(adition(8, 7),adition(5, 8)))
# výsledek :
#28

# dobrovolný parametr (pokud nepošleme všechny vstupní hodnoty,
# pak se nastaví na přednastavenou hodnotu).
# tohoto dosáhneme přidáním = hodnota.
# dobrovolný parametr musí být vždý na konci (až po normal parametrech).
def hello (name,  dif = " ", greet = "Hello") :
    result =  greet + dif + name
    print(result)

hello("David"," ", "Sup")
hello("Tom")
# výsledek :
#Sup David
#Hello Tom

# takto můžeme třeba udělat mocnění.
# _ je příkaz pythonu který se používá na zahození hodnoty (aby jsme si nezabrali proměnnou).
def power (number, mocnitel) :
    result = 1
    for _ in range (0, mocnitel) :
        result = result * number
    return result

print(power(2,4))
# výsledek :
#16