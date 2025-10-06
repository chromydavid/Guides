# WHILE LOOP
# while loop funguje skoro jako for loop. (dokud není podmínka splněna opakuje se).
# dokud není count 5 nebo více bude se loop opakovat :
count = 1
while count < 5 :
    print(count)
    count += 1
# výsledek :
#1
#2
#3
#4

# nekonečný cyklus (zastaví se pouze funkcí break)
# break ukončí daný cyklus (while nebo for) ve kterém se nachází :
counter = 1
while True :
    print(counter)
    if counter >= 5 :
        break
    else :
        counter += 1
# výsledek :
#1
#2
#3
#4
#5

# funkce continue přeskočí zbytek cyklu ale dál pokračuje :
# když dosáhneme i=3 tak přeskočíme print() :
for i in range(0, 5):
    if i == 3:
        continue
    print(i)

# výsledek :
#0
#1
#2
#4

# funkce break a continue se dají použít jak ve for tak ve while loopu.

# funkce pass vyignoruje danou podmínku/cyklus :
# normálně dá prázdná podmínka error ale s pass se nepoužije (jak kdyby tam nebyla).

if i == 5 :
    pass
# výsledek :
#žádný výsledek není