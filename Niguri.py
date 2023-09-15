import random


class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def isAlive(self):
        pass


class Car:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def isAlive(self):
        print("")


class Child:
    def __init__(self, name, age, hp, money, profi, rest, chill):
        self.name = name
        self.age = age
        self.hp = hp
        self.money = money
        self.profi = profi
        self.rest = rest
        self.chill = chill

    def isAlive(self):
        if(self.hp<= 0 and money <=0):
            return false
        else:
            return false

    def work(self):
        self.hp-=2
        self.money+=2

    def rest(self):
        self.hp+=2
        self.money-=2

    def chill(self):
        self.hp += 5
        self.money -= 8


for i in range(4):
    rand_action = random.randint(1, 3)







child1 = Child("ASdsda", 13,100, 500, "gay", "0" )

car1 = Car("Skoda Octavia WRS", 5)

step = Student("Stepan",23)

print("daaaaaaaa")

