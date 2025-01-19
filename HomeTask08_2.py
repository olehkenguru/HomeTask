def is_palindrome(text):
    clear_text = ''.join(char for char in text if char.isalpha()).lower()
    return clear_text == clear_text[::-1]

print(is_palindrome('A man, a plan, a canal: Panama'))

