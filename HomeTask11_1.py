def is_prime(num):
    for i in range(2, int(num/2) + 1):
        if num % i == 0:
            return False

    return True



def prime_generator(end):
    """
        Генератор простих чисел чисел.

        :param end: верхня межа діапазону
    """
    begin = 2
    i = 0
    while True:
        i += 1
        if i == end:
            return

        if (is_prime(begin)):
            yield begin
        begin = begin + 1

from inspect import isgenerator

gen = prime_generator(1)
print(isgenerator(gen))

print(list(prime_generator(29)))
