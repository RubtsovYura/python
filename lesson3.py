from random import randint , choice

a = randint(1, 100)
print(a)
cities = ["Moscow", "Ecb" , "Spb"]
print(choice(cities))

surnames = ["Ivanov", "Petrov", "Sdidorov"]
names = ["Oleg", "Petr", "Igor"]
secondnames = ["Ivanovich", "Petrovich", "Sidorovich"]

for surname, name , middle_name in zip(surnames, names, secondnames):
    print(surname,name,middle_name)



"""Функции и словари"""

#Пример функции
#map

spisok_input = list(map(int,input().split()))
print(sum(spisok_input))

def sum_digits(number):
    """
    Функция вычисляет сумму цифр числа
    """
    sum_num = 0
    while number > 0:
        sum_num += number % 10
        number //= 10
    return sum_num

print(sum_digits(1234))

def say_hello(hello, name = "Noname"):
    print(hello , name)
say_hello("hello")

def summa(a,b, *args):
    return  a + b + sum(args)

print(summa(5,10,15,20))

def print_sum(a, b =10):
    print(a +b)

print_sum(5)

print("hello", "piter", "moscow", sep="/", end = "")
print("hello", "piter", "moscow", sep="/")

def my_func(a , b , *args, name ="Igor", age = 29,**kwargs):
    res = a+b
    print(args)
    print(kwargs)

my_func(5,10,150,350, name= "Pavel", city = "Moscow")


#Словари

personal = {
    "name" : "Иван",
    "age" : 29 ,
    "hobby" : {
        "footbal" : "С 9 лет",
        "hockey" : "1 год"
    }
}
#Способоы пробежаться по словарю
for key in personal:
    print(key)

for key in personal:
    print(key, personal[key])

for key, value in personal.items():
    print(key, "->", value)

personal["name"] = ["Pavel","Pasha"]
personal["sername"] = "Ivanov"

print(personal["name"][1])