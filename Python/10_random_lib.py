# RANDOM MODUL
# použijeme funkci import a název modulu aby jsme jej vložili do našeho
# kódu a rozšířili si příkazy :
import random

# random.randint(rozsah pole) tato funkce bygeneruje náhodný integer v daném rozsahu
# rozsah není jako u pole indexů ale je od daného čísla 1 po číslo 2 :
print(random.randint(0,5))
# výsldek :
#náhodné číslo (1,2,3,4,5) jedno z nich.

# random.choice vybere náhodnou volbu/element jako v for loopu.
# pro list :
list = ["A", "B", "C", "D"]
print(random.choice(list))
# výsldek :
#náhodné písmeno (A,B,C,D) jedno z nich.

# pro string :
name = "tom"
print(random.choice(name))
# výsledek :
#náhodné písmeno (t,o,m) jedno z nich.