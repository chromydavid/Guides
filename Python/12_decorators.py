#Dekorátory
#Toto je jednoduchá funkce která jen vypíše že hraje film pro daného user

user = {
    "Name" : "David",
    "Age" : 16
}

def play_film():
    print(f"Playing film for {user['Name']}.")

play_film()

#Ale dejme tomu že chceme kontrolovat zda je uživateli nad 18 let (je dospělí ?)
#můžeme buď použét typickou metodu :

user = {
    "Name" : "David",
    "Age" : 16
}

def play_film():
    print(f"Playing film for {user['Name']}.")

if user["Age"] >= 18 :
    play_film()
else :
    print(f"{user['Name']} is too young!")

#No sice je tato varianta super ale má jeden velký problém dejme tomu že by jsme chtěli kontrolovat věk pro několik funkcí 
#ale vždy odděleně to by jsme se s if/else upsaly k smrti. můžeme tedy použít funkci která má jako vstup funkci a jako výstup funkci (dekorátor).

user = {
    "Name" : "David",
    "Age" : 19
}

def play_film() :
    print(f"Playing for {user['Name']}.")

def check_age(func): #dekorátor který bude kontrolovat věk user
    def wrapper(): #obal do kterého se schová funkce play_film
        if user["Age"] >= 18 :
            func()
        else :
            print(f"{user['Name']} is too young!")
    return wrapper  #vracíme funkci (NEVOLÁME JI)

play_film = check_age(play_film) #přepisujeme proměnou play_film na funkci check_age její vstup je bývalá funkce play_film

play_film() #voláme novou funkci play_film


#tak a teď si trochu poupravíme zápis

user = {
    "Name" : "David",
    "Age" : 19
}

def check_age(func): 
    def wrapper(): 
        if user["Age"] >= 18 :
            func()
        else :
            print(f"{user['Name']} is too young!")
    return wrapper  

@check_age  #tento řádek nahrazuje play_film = check_age(play_film) ale teď musíme definovat check_age dříve než funkci play_film
def play_film() :
    print(f"Playing for {user['Name']}.")

play_film() 

# teď si rozebereme co se vlastně děje
#no vlastně nic extra ve funkci wrapper se func() změní na volání funkce play_film()
def check_age(func): 
    def wrapper(): 
        if user["Age"] >= 18 :
            play_film() # <--------------------------- TADY
        else :
            print(f"{user['Name']} is too young!")
    return wrapper  

#co se pak děje s funkcí check_age(func) no ta přece vrací novou wrapper funkci takže se dá říct že vypadá takto
def wrapper(): 
    if user["Age"] >= 18 :
        play_film() #<zde se volá funkce play_film
    else :
        print(f"{user['Name']} is too young!") 

# a tato funkce se nakonec přepíše do proměné play_film a pro zjednodušení řekneme že místo volání play_film() se přepíše obsah play_film
#takže po dokončení kódu a odekorování funkce (@check_age) play_film vypadá vysledná funkce takto
def play_film() :
    if user["Age"] >= 18 :
        print(f"Playing for {user['Name']}.") #<----- bývalí obsah funkce play_film
    else :
        print(f"{user['Name']} is too young!")

# No a pak už jen zavoláme novou funkci play_film
play_film()
