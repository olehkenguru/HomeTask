def is_even(digit: int):
    """ Перевірка чи є парним число """
    if digit % 2 == 0:
        return True
    else:
        return False

print(is_even(5))