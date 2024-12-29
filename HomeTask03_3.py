main_list = [1,2,3]

if len(main_list) % 2 == 0:
    half_list = len(main_list) // 2
else:
    half_list = len(main_list) // 2 + 1

first_list = main_list[:half_list]
second_list = main_list[half_list:]

result_list = [first_list, second_list]

print( f"{main_list} => {result_list}")
