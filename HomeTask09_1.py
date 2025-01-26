import string

def popular_words (text: str, words: list):
    words_from_text = [word.strip(string.punctuation) for word in text.lower().split()]

    return  {word: words_from_text.count(word) for word in words}

print(popular_words('When I was One I had just begun When I was Two I was nearly new    ', ['i', 'was', 'three', 'near']))