"""Задание 1"""
from time import  sleep
class TrafficLight:
    __color = ["Красный", "Желтый" , "Зеленный"]

    def running (self):
        i = 0
        while i != 3:
            print(TrafficLight.__color[i])
            if i ==0:
                sleep(7)
            elif i == 1:
                sleep(2)
            else:
                sleep(5)
            i += 1
t =TrafficLight()
t.running()
"""Задание 2"""

class Road:
    def __init__(self, length, width):
        self.__lenght = length
        self.__width = width
        self.lenght = 5
        self.width = 25


    def calculation(self):
        cal = self.__lenght * self.__width * self.lenght * self.width
        print(f"При расчет получилось {cal}")

r = Road(5, 2000)
r.calculation()

"""Задание 3"""
class Worker():

    def __init__(self,name , surname, position , wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus" : bonus}

class Position(Worker):
    def get_full_name(self):
        return self.name + " " + self.surname

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]

p = Position("Misha" , "Rubtsov" , "QA" , 10000 , 20000)
print(p.get_total_income(), p.get_full_name())

"""Задание 4"""

class Car():
    def __init__(self, speed, color, name, is_police = True):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go (self):
        return f"Машина {self.name} тронулаьс с места"
    def stop(self):
        return f"Машина {self.name} остановилась"
    def turn(self, direction):
        return f"Машина {self.name} повернула {direction}"
    def show_speed (self):
        return f"Машина движется со скоростью {self.speed}"

class TownCar(Car):
    def show_speed (self):
        if self.speed > 60:
            return f"Ты двигаешь слишком быстро. На данном участке скорость должна быть меньше {self.speed}"
        else:
            return f"Твоя скорость машины {self.speed}. Что в пределах нормы"
class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f"Ты что гонщик? Это рабочая машина, едь со скоростью  быть меньше {self.speed}"
        else:
            return f"Твоя скорость машины {self.speed}. Что в пределах нормы."
class PoliceCar(Car):
    pass

town = TownCar('Audi', 45, 'blue', False)
print('1:\n' + town.go(), town.show_speed(), town.turn('left'), town.turn('right'), town.stop())

sport = SportCar('AudiRS', 170, 'red', False)
print('2:\n' + sport.go(), sport.show_speed(), sport.turn('left'), sport.stop())

work = WorkCar('WAZ', 50, 'red', False)
print('3:\n' + work.go(), work.show_speed(), work.turn('right'), work.stop())

police = PoliceCar('Kia', 100, 'yellow', True)
print('4:\n' + work.go(), work.show_speed(), work.turn('right'), work.stop())


"""Задание 5"""

class Stationery():
    def __init__(self, title):
        self.title = title
    def draw(self):
        return "отрисовка"


class Pen(Stationery):
    def draw(self):
        return f"Начинаем отрисовку {self.title}"

class Pencil(Stationery):
    def draw(self):
        return f"Начинаем отрисовку {self.title}"

class Handle(Stationery):
    def draw(self):
        return f"Начинаем отрисовку {self.title}"

pen = Pen("Ручкой")
print(pen.draw())
pencil = Pencil("Карандашем")
print(pencil.draw())
handel = Handle("маркером")
print(handel.draw())
