my_list = [1, 2, "three"]
if len(my_list) > 0:
    my_list = [my_list[-1]] + my_list[:-1]

print(my_list)
