import random

job_list = {
 "JS": {"salary": 100, "gladness_less": 10},
 "Python": {"salary": 80, "gladness_less": 3},
 "C++": {"salary": 90, "gladness_less": 1}
}

brand_of_car = {
    "Volkwagen":{"fuel":100, "strenght":90, "conpsomption":4},
    "Lexus":{"fuel":100, "strenght":100, "conpsomption":6},
    "Bmw":{"fuel":100, "strenght":60, "conpsomption":9},
    "Mersedes-Benz":{"fuel":60, "strenght":10, "conpsomption":12}
}


class Human:
    def __init__(self, name, car=None, job=None, home=None):
        self.name = name
        self.money = 100
        self.gladness = 100
        self.satiety = 100
        self.job = job
        self.car = car
        self.home = home

    def get_home(self):
        self.home = House()

    def get_car(self):
        self.car = Auto(brand_of_car)

    def get_job(self):
        if self.car.drive():
            pass
        else:
            self.repair()
            return

        self.job = Job(job_list)

    def eat(self):
        if self.home.food <= 0:
            self.shopping("food")
        else:
            if self.satiety >= 100:
               self.satiety = 100
            return
        self.satiety += 5
        self.home.food -= 5


    def work(self):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                self.shopping("fuel")
                return
            else:
                self.repair()
                return
        self.money += self.job.salary
        self.gladness += self.job.glandess_less
        self.satiety -= 4

    def shopping(self, manage):
        if self.car.drive():
            manage("fuel")
        else:
            self.repair()
            return
        if manage == "food":
            print("i bought fuel")
            self.home.food += 50
        elif manage == "Sweets":
            print("nsssssssm")
            self.gladness += 10
            self.satiety += 4
            self.money -= 10

    def chill(self):
        self.gladness += 10
        self.home.food += 5
        self.money -= 5

    def clean_home(self):
        self.gladness -=5
        self.home.mess = 0

    def repair(self):
        self.car.strenght += 100
        self.money -= 40

    def days_indexes(self, day):
        day = f"Today the {day} of {self.name}'s life'"
        print(f"{day:=^50}", "\n")
        human_index = self.name + "'s index'"
        print(f"{human_index}:^50", "\n")
        print(f"Money - {self.money}")
        print(f"Satiety - {self.satiety}")
        print(f"Gladness - {self.gladness}")
        home_index = "Home index"
        print(f"{home_index}:^50", "\n")
        print(f"Food - {self.home.food}")
        print(f"Mess - {self.home.mess}")
        car_index = f"{self.car.brand} car index"
        print(f"{car_index}:^50", "\n")
        print(f"Fuel - {self.car.fuel}")
        print(f"Strength - {self.car.strength}")

    def is_alive(self):
        pass



class Auto:
    def __init__(self,brand_list):
        self.brand = random.choice(list(brand_list))
        self.fuel = brand_list[self.brand]["fuel"]
        self.strenght = brand_list[self.brand]["strength"]
        self.conpsumption = brand_list[self.brand]["consumption"]

    def drive(self):
        if self.strenght > 0 and self.fuel >= self.conpsumption:
            self.fuel -= self.conpsumption
            self.strenght -= 1
            return True
        else:
            print("car cannot move")


class House:
    def __init__(self):
        self.mess = 0
        self.food = 0


class Job:
    def __init__(self):
        self.job = random.choice(list(job_list))
        self.salary = job_list[self.job]["salary"]
        self.glandess_less = job_list[self.job]["glandess_less"]

