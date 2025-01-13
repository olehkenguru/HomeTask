import string, keyword

possible_name = input('Enter the name of variable: ')

prohibited_characters = set(string.punctuation.replace('_', ' '))
prohibited_words = keyword.kwlist

if len(possible_name) == 0:
    print(f'FALSE: The empty is not allowed.')
    exit()

if possible_name[0].isdigit():
    print(f'FALSE: First symbol "{possible_name[0]}" is not allowed.')
    exit()

for i in possible_name:
   if i in prohibited_characters:
       print(f'FALSE: The symbol "{i}" is not allowed.')
       exit()
   elif i.isupper():
       print(f'FALSE: The symbol "{i}" is in uppercase. It is not allowed.')
       exit()

for i in prohibited_words:
    if i.lower() == possible_name.lower():
        print(f'FALSE: The word "{i}" is not allowed.')
        exit()

for i in range(len(possible_name) - 1):
    if (i > 0 and possible_name[i] == '_' and possible_name[i + 1] == '_') or possible_name == '__':
        print(f'FALSE: The symbol "_" repeated.')
        exit()

print(f'TRUE: The word "{possible_name}" is allowed. Congratulations!')