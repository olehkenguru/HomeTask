def first_word(text):
    """ Пошук першого слова """
    text = text.replace('.', ' ')

    for word in text.split():
        check_word = ''.join(c for c in word if c.isalnum() or c == "'")

        if check_word:
            return check_word


print(first_word("don't.touch it"))