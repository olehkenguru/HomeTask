import string, keyword

possible_name = input('Enter the name of variable: ')

prohibited_characters = set(string.punctuation.replace('_', ' '))
prohibited_words = keyword.kwlist

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
    if possible_name[i] == possible_name[i + 1] and possible_name[i] == '_':
        print(f'FALSE: The symbol "_" repeated.')
        exit()

print(f'TRUE: The word "{possible_name}" is allowed. Congratulations!')