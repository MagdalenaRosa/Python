# Zadanie 3
# Utwórz moduł zawieraj ˛acy klas ˛e Account. Konstruktor klasy powinien tworzyć prywatny atrybut balance, który jest inicjalizowany wartości ˛a parametru konstruktora. Zdefiniuj w klasie metody: pay() - zwi ˛eksza saldo konta o podan ˛a wartość,
# take() - zmniejsza saldo konta o podana wartość lub informuje o braku środków. Napisz metode specjalna __str__(), która wyświetla m.in wartość prywatnego atrybutu
# blance.
# Przetestuj moduł w prostym programie.


class Account:
    def __init__(self,balance):
        self._balance=balance

    def pay(self,amount):
        self._balance+=amount
        return f"wplacono {amount} zł "
    #     jak nie dawałam tego to kwota
    def take(self,amount):
        if self._balance < amount:
            print("Brak srodków na koncie")
        else:
            self._balance = self._balance-amount
            print(f"wyplacono {amount} zł ")

    def __str__(self):
        return (f"kwota na twoim koncie wynosi: {self._balance}")

acount1=Account(1000)
print(acount1)
acount1.take(300)
print(acount1)
acount1.pay(400)
print(acount1)

