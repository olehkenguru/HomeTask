def add_one(some_list):
    num = int(''.join(str(i) for i in some_list)) + 1

    return [int(i) for i in str(num)]


print(add_one([9]))