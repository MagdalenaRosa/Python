import re
class Pet:
    def __init__(self,name,hunger=0,tiredness=0):
        self.name=name
        self.hunger=hunger
        self.tiredness=tiredness

    def __str__(self):
        return f"Imie zwierzaka: {self.name}\n poziom glodu: {self.hunger} \n poziom zmeczenia: {self.tiredness}"

    @property
    def name(self):
        return self.__dict__["name"]
    @name.setter
    def name(self,name):
        n = re.sub(r'[^a-zA-Z]', '', name)
        if len(n)<3:
            print("Imie musi być dłuższa niż 3")
            main()
        else:
            self.__dict__["name"]=n
            print(f"imie zwierzaka to {self.__dict__['name']}")

    def _passage_of_time(self):
        self.hunger+=1
        self.tiredness+=1

    @property
    def mood(self):
        mood=self.hunger+self.tiredness
        return mood


    def talk(self):
        self._passage_of_time()
        suma =self.mood
        if suma<5:
            print("Zwierzak jest szczęśliwy")
        elif 5<=suma<=10:
            print("Zwierzak zadowolony")
        elif 11<=suma<=15:
            print("Zwierzak podenerwowony")
        elif suma>15:
            print("Zwierzak wściekły")
        # print(suma)

    def eat(self,portion=4):
        self._passage_of_time()
        self.hunger-=portion
        # print(self.hunger)
    def play(self,fun=4):
        self._passage_of_time()
        self.tiredness-=fun

def main():
        pet_name= input("Podaj imię zwierzaka: ")
        hung=input("chcesz podać jak bardzo głodny i zmęczony jest zwierzak T/N ?")
        p1 = Pet(pet_name)
        if hung=='T':
            pet_hunger=int(input("Podaj jak bardzo głodny jest zwierzak: "))
            pet_tiredness=int(input("Podaj jak bardzo zmęczony jest zwierzak: "))
            p1.hunger=pet_hunger
            p1.tiredness=pet_tiredness


        def option_fun():
            option: int= int(input("Wybier jedną z opcji:\n"
                            "1- samopoczucie zwierzaka\n"
                            "2- nakarm zwierzka\n"
                            "3- pobaw się ze zwierzkiem\n"
                            "4- kończymy na dziś \n"
                            "5- wyświetl dane o zwierzaku\n"
                                   ))
            match option:
                case 1:
                    p1.talk()
                    print('-'*50)
                    option_fun()
                case 2:
                    var= input("chcesz podać ile ciasteczek dasz zwierzakowi T/N ?")
                    if var =="T":
                        wartosc = int(input("Podaj ile chcesz dać smakołyków zwierzakowi? 1 smakołyk = zmniejsza głód o 1"))
                        p1.eat(wartosc)
                    p1.eat()
                    option_fun()
                case 3:
                    var = input("chcesz podać ile czasu będziesz bawić się z zwierzakiem T/N ?")
                    if var=="T":
                        time_of_play=int(input("Ile minut będiesz się bawić ze zwierzakiem?"))
                        p1.play(time_of_play)
                    p1.play()
                    option_fun()
                case 4:
                    return
                case 5:
                    kod_dostepu=input("Podaj kod dostępu")
                    if kod_dostepu=="xy":
                        print(p1.__str__())
                    else:
                        print("Błędna wartość")
                        option_fun()
                case _:
                    print("Podaną będną wartość")
                    option_fun()

        option_fun()



if __name__ == "__main__":
    main()






