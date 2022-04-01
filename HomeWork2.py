"""Задание 1 """
a = 15 * 3
b = 15 / 3
c = 15 // 2
d = 15 ** 2
print(f"type(15 * 3) является: {type(a)}"
      f"\ntype(15 / 3)является: {type(b)},"
      f"\ntype(15 // 2)является:{type(c)}"
      f"\ntype(15 ** 2)является:{type(d)}")#симвло \n переводит на след строку

"""Задание 2"""
print('Задание 2')
my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
len_list = int(len(my_list))
for i in range(len_list):
    elem = my_list.pop()
    if elem.isdigit() and elem.isalnum():
        my_list.append(f'{int(elem):02d}')
    elif elem[0] == "+" and elem[1].isdigit():
        my_list.append(f'{int(elem):02d}')
    else:
        my_list.append(elem)
print(" ".join(my_list))

"""Задание 4"""
print('Задание 4')
list_professional = ['инженер-конструктор Игорь',
                     'главный бухгалтер МАРИНА',
                     'токарь высшего разряда нИКОЛАй',
                     'директор аэлита']
welcome = {}
for element in list_professional:
    name_register = element.split()[-1].capitalize()
    print(f"Привет, {name_register}! ")

"""Задание 5"""
print('Задание 5')
price_list = [57.8, 46.51, 97,47.6,87.93,100,3.93,0.16,83.56, 11,5]
for i, num in enumerate(price_list):
    end_word = str(",")
    fix_price = str(f"{float(num):.2f}").split(".")
    print(f"{fix_price[0]}руб {fix_price[1]}коп", end=end_word)
#Надеюсь тут не надо было работать с отформатированым списком
id_list = id(price_list)
price_list.sort()
print(f"\n{price_list}")
if id_list == id(price_list):
    print("Один и тот же объект")
else:
    print("Разные")

new_list = list(reversed(price_list))
print(new_list)
#Проверим что разные списки
id_new_list = id(new_list)
if id_new_list == id(price_list):
    print("Один и тот же объект")
else:
    print("Разные")

#Обратимся к сортированому списку по возрастанию
print(f"Топ 5 дорогих товаров:{price_list[-5:len(price_list)]}")

