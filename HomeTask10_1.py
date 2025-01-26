from inspect import isgenerator

def pow(x):
    return x ** 2

def some_gen(begin, end, func):
    """
        Генератор чисел.

        :param begin: перший елемент послідовності.
        :param end: кількість елементів у послідовності.
        :param func: функція, яка формує значення для послідовності.
    """
    i = 0
    while True:
        i += 1
        if i > end:
            return
        yield begin
        begin = func(begin)


gen = some_gen(2, 4, pow)


print(list(gen))
print(isgenerator(gen))
