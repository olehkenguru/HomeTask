def correct_sentence(text):
    sentences = text.split('.')
    text = ''.join(
        sentence.strip()[0].upper() + sentence.strip()[1:] + '. '
        for sentence in sentences
        if sentence.strip()
    )
    return text.strip()

print(correct_sentence("greetings, friends. Blablabla. hello, world"))
