seconds = int(input('Будь ласка, введіть число від 0 до 8640000: '))

if 0 <= seconds < 8640000:
    days, seconds = divmod(seconds, (24 * 60 * 60))
    hours, seconds = divmod(seconds, (60 * 60))
    minutes, seconds = divmod(seconds, 60)

    if 11 <= days % 100 <= 19:
        day_word = "днів"
    elif days % 10 == 1:
        day_word = "день"
    elif 2 <= days % 10 <= 4:
        day_word = "дні"
    else:
        day_word = "днів"

    print(f'{days} {day_word}, {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}')
else:
    print('Щось пішло не так...')