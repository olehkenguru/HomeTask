first_list = [1, 0, 13, 0, 0, 0, 5]
zero_numbers = []
other_numbers = []


for i in first_list:
    if i == 0:
        zero_numbers.append(i)
    else:
        other_numbers.append(i)

print(other_numbers + zero_numbers)

