import string

user_input = input('Enter something: ').title().replace(' ', '')

user_input = ''.join(_ for _ in user_input if _ not in string.punctuation)[:140]

print(f'#{user_input}')