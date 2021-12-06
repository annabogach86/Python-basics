def int_func(text):
    word = text[0].upper() + text[1:].lower()
    return word
stroka = input('Введите строку: ')
for word in stroka.split(' '):
    print(f'{int_func(word)}', end=' ')
