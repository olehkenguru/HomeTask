def difference(*args):
    if len(args) == 0:
        return 0

    return round(max(args) - min(args), 2)


print(difference(10.2, -2.2, 0, 1.1, 0.5))