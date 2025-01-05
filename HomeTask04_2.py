first_list = [1, 3, 0]

sum_numbers = 0
last_number = 0

i = 0
while i < len(first_list):
    if i % 2 == 0:
        sum_numbers += first_list[i]

    last_number = first_list[i]
    i += 1

print(sum_numbers * last_number)