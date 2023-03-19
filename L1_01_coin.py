
import random
# 1. Utwórz klase Coin.

class Coin:
    # 2. Bezparametrowy konstruktor
    def __init__(self):
        self.side="Orzeł"

    def __str__(self):
        return f"{self.side}"

    def throw(self):
        temp = random.randint(0, 1)
        if temp == 1:
            self.side = 'Orzeł'
        else:
            self.side = 'Reszka'


c= Coin()
c2=Coin()

print(f"wartość c2={c2}")

print(f"wartość c: {c}")
print("-"*50)
i=0
tab=[]
while i<15 :
    c2.throw()
    tab.append(c2.side)
    i=i+1
print(f"Wylosowane wartości monet w {i} rzutach: {tab}")

print("-"*200,"\n"*3)


lost=0
win=0

def gra():
    # Program powinien tworzyć trzy instancje klasy Coin reprezentujace monety o nominałach 1zł, 2zł i 5 zł.
    m5=Coin()
    m2=Coin()
    m1=Coin()
    # Poczatkowe saldo gry powinno być równe 0 zł
    saldo=0
    # informuje że przyjmuje on globalne wartości ma patzreć na zmienne poza funkcją
    global lost
    global win

    kolejka=True
    while kolejka:

        # W każdej kolejceprogram
        # powinien wykonywać rzut trzema monetami i dodawać do salda ich wartości, jeżeli n danej monecie wypadnie orzeł.
        tab_rzutow=[]
        m1.throw()
        m2.throw()
        m5.throw()

        rzut1=m1.side
        rzut2=m2.side
        rzut3=m5.side

        tab_rzutow.append(rzut1)
        tab_rzutow.append(rzut2)
        tab_rzutow.append(rzut3)
            # print(f"tablica rzutów : {tab_rzutow}")

        if rzut1=='Orzeł':
            saldo+=1
        if rzut2=='Orzeł':
            saldo+=2
        if rzut3=='Orzeł':
            saldo+=5
        print(f"obecne saldo gry: {saldo}")

        if saldo >=20:
            kolejka=False
            if saldo >20:
                print("przegrana")
                print("-"*50)
                lost+=1 
            elif saldo == 20:
                print("wygrana")
                print("-"*50)
                win+=1


i=0
while i<100:
    i+=1
    gra()

print(f"liczba wygrnych rozgrywek: {win}")
print(f"liczba przegranych rozgrywek: {lost}")


