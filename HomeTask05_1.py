import string, keyword

possible_name = 'assert_exception' # input('Enter the name of variable: ')

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

if len(possible_name.replace("_", "")) == 0 and len(possible_name) > 1:
    print(f'FALSE: The word "{possible_name}" is not allowed.')
    exit()

print(f'TRUE: The word "{possible_name}" is allowed. Congratulations!')