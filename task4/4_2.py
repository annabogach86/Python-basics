def exp_numbers(x, y):
    total = 1
    for i in range(abs(y)):
        total *= x
    return 1 / total
x = float(input('Введите действительное положительное число: '))
y = int(input('Введите целое отрицательное число: '))
print(exp_numbers(x, y))
