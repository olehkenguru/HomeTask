def is_even(number):
    list_even = (0, 2, 4, 6, 8)
    last_num = int(str(number)[-1:])
    return last_num in list_even


print(is_even(2494563894038))