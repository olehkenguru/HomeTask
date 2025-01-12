user_number = input('Enter the number: ')

list_number = list()

for i in user_number:
    list_number.append(int(i))

while len(list_number) > 1:
    result = 1
    for i in list_number:
        result *= i

    list_number = [int(_) for _ in str(result)]

print(f'{user_number} -> {list_number[0]}')