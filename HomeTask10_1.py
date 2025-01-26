def pow(x):
    return x ** 2

def some_gen(begin, end, func):
    i = 0
    while True:
        i += 1
        if i > end:
            return
        yield begin
        begin = func(begin)


gen = some_gen(2, 4, pow)


from inspect import isgenerator
print(list(gen))
print(isgenerator(gen))
