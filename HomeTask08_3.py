def find_unique_value(some_list):
   some_set = set(some_list)
   count_digits = {num: some_list.count(num) for num in some_set}

   result = [k for k, v in count_digits.items() if v == 1]
   if result:
       return result[0]
   else:
       return None


print(find_unique_value([5, 5, 5, 2, 2, 0.5]))