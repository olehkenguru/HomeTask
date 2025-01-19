def correct_sentence(text):
    sentences = text.split('.')
    text = ''.join(
        sentence.strip()[0].upper() + sentence.strip()[1:] + '. '
        for sentence in sentences
        if sentence
    )
    return text.strip()

print(correct_sentence("hello, world. bye"))
