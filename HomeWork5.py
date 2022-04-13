from sys import getsizeof
import time
import sys
"""Задание 1 Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield, например"""
def odd_num(to):
    """ task 1 """
    for i in range(1, to + 1, 2):
        yield i
if __name__ == "__main__":
    a_gen = odd_num(15)

    print("a_gen type", type(a_gen))

    for elem in a_gen:
        print(elem)

    print(f"empty {list(a_gen)}")

"""Задание 3 Есть два списка:"""


tutors = [

    'Иван', 'Анастасия', 'Петр', 'Сергей',

    'Дмитрий', 'Борис', 'Елена'

]
klasses = [

    '9А', '7В', '9Б', '9В', '8Б',  # '10А', '10Б', '9А'

]

def generator():

    len_klasses = len(klasses)

    return ((tut, klasses[i]) if i < len_klasses else (tut, None)
            for i, tut in enumerate(tutors))


if __name__ == '__main__':

    gen = generator()
    print(type(gen))
    print(getsizeof(gen))
    print(*gen)

"""Задание 4 Представлен список чисел. Необходимо вывести те его элементы, значения которых больше предыдущего, например:"""


def my_filter(*argv):
    return (argv[i] for i in range(1, len(argv)) if argv[i] > argv[i - 1])


if __name__ == "__main__":

    src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
    result = [12, 44, 4, 10, 78, 123]

    t = time.perf_counter()
    answ = my_filter(*src)
    print(time.perf_counter() - t)
    print(sys.getsizeof(answ))
    print(list(answ) == result)

"""Задание 5Представлен список чисел. Определить элементы списка, не имеющие повторений. Сформировать из этих элементов список с сохранением порядка их следования в исходном списке, например:"""
import time  # use for test
import sys  # use for test


def my_set(*argv):
    """ return unique elemts of argv """
    answ = set()

    for elem in argv:
        if not elem in answ:
            answ.add(elem)
        else:
            answ.remove(elem)

    return [x for x in argv if x in answ]

if __name__ == "__main__":

    src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
    result = [23, 1, 3, 10, 4, 11]

    t = time.perf_counter()
    r = my_set(*src)

    print("mem: ", sys.getsizeof(r))
    print("time: ", time.perf_counter() - t)

    print(r == result)
    print(r)

    print(test_set(*src))