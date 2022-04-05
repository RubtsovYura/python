from random import choice
"""Задание 1 """

direct_number = {
    "one": "один",
    "two": "два",
    "three": "три",
    "four": "четыре",
    "five": "пять",
    "six": "шесть",
    "seven": "семь",
    "eight": "восемь",
    "nine": "девять",
    "ten": "десять"
}

def num_translate(number):
    """
    Функция переводит слова
    :return:
    """
    key = direct_number.get(number)
    if key:
        return  direct_number.get(number)
    else:
        return None
number = str(input("Введите цифру словом на английском: "))
print(num_translate(number))

"""Задание 2 """
def num_translate_adv(number):
    key = direct_number.get(number.lower())  #Приводим вводимое в нижний регистр
    if key:
        return key.capitalize() if number[0].isupper() else key  #Если буква в верхнем регистре то пользуемся методом который приводит 1 букву в верх регистр
    return None

number = str(input("Введите цифру словом на английском: "))
print(num_translate_adv(number))

"""Задание 3"""

def thesaurus(args):
    name_dict = {}
    for name in args:

        if name_dict.get(name[0]):
            name_dict[name[0]].append(name)
        else:
            name_dict[name[0]] = [name]
    return  name_dict

"""Задание 5"""

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

def generator(froms,use, unique):
    while True:
        n_nounse = choice(froms)

        if not (unique and n_nounse in use):
            use.append(n_nounse)
            break

    return (n_nounse, use)

def get_jokes(count, unique=False):
    """ gen count jokes """
    used = []
    answer = []

    if unique and count < len([*nouns, *adverbs, *adjectives]):
        return []
    for _ in range(count):
        nons, used_ = generator(nouns, used, unique)
        used.append(used_)

        adv, used_ = generator(adverbs, used, unique)
        used.append(used_)

        adj, used_ = generator(adjectives, used, unique)
        used.append(used_)

        answer.append(f"{nons} {adv} {adj}")

    return answer







