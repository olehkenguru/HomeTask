import string

user_letters = input('Enter two letters with a motto between them: ')

all_letters = string.ascii_letters

d1 = user_letters[0]
d2 = user_letters[2]

index_d1 = all_letters.index(d1)
index_d2 = all_letters.index(d2)

print(all_letters[index_d1:index_d2 + 1])
