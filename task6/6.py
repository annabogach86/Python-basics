a, b = int(input('Введите км: ')), int(input('Введите км: '))
counter = 0
while a < b:
    counter += 1
    print(f'{counter}' + '-й день:', f'{a:.2f}')
    a = (a * 0.1) + a
print('На', f'{counter}' + '-й день спортсмен достиг результата, не менее', f'{a:.0f}', 'км')
