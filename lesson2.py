from math import sqrt , sin , cos  #можно импортировать определенную функциб
from sys import  getsizeof #высчитывает сколько занимает байт
my_list_to_buy = ['абрикосы', 'вода', 'горох','зелень','мука','яблоко']
"""Функции методов:"""
print(getsizeof(my_list_to_buy))
#my_list_to_buy.append("Другой фрукт") #добавление элемента в список
    #clear очищает список
print(getsizeof(my_list_to_buy))
dop_list = ['apple', 'carrot']
"""my_tuple = ('абрикосы', 'вода', 'горох','зелень','мука','яблоко')# кортеж ,но он не изменяем
print(getsizeof(my_tuple))
my_list_to_buy.extend(dop_list) #метод extend добавляет к списку элементы другого списока
my_list_to_buy.append(dop_list) #метод append добавит элементы списка dop_list как один элемент
print(my_list_to_buy[7][0])
    Метод pop удаляет последний эл в списке плюс выводит элемент который удалил , но также можно и удалить определенный элемент через индекс
lust_item = my_list_to_buy.pop()
print(lust_item)
print(my_list_to_buy)
    Метод coun выводит количество искомого элемента
print(my_list_to_buy.count("яблоко"))
    Метод index позваляет найти позицию элемента (но только там где он встречется в-певый раз
print(my_list_to_buy.index("яблоко"))
    Метод insert добавляет элемент в ту позицию какую мы укажем
my_list_to_buy.insert(3, 'mask')
print(my_list_to_buy)
    Метод remove удаляет указанный элемент
my_list_to_buy.remove("яблоко")
print(my_list_to_buy)
    Метод copy если списки копировать просто приравниванием то у них будет один id и меняя один список будет меняться и другой
    , но если в списке находится список то меняться он будет в двух местах ,если такое имеется то лучше подключить другую библиотеку
     и использовать deepcopy
my_list2 = my_list_to_buy.copy()
my_list2.pop()
print(my_list_to_buy)
print(my_list2)
    Метод reverse() сортирует в обратно направление,если хотим работать с другим списком можно использовать команду reversed
my_list_to_buy.reverse()
print(my_list_to_buy)
    Срез списка
print(my_list_to_buy[0:4])
    """
list2 = my_list_to_buy[:]
list2.sort()
print(list2)
list2.sort(reverse=True)
print(list2)
"""if isinstance(my_list_to_buy, list):
    print('list') проверка типа перменной
print(dir(my_list_to_buy)) выводит методы применяемы к данной перемене"""