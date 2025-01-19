def common_elements_one_row():
    return set([i for i in range(100) if (i % 3 == 0) & (i % 5 == 0)])


def common_elements():
    first = list(i for i in range(100) if i % 3 == 0)
    second = list(i for i in range(100) if i % 5 == 0)

    return set(first) & set(second)


print(common_elements())
print(common_elements_one_row())