def sum_numbers(num_1, num_2, num_3):
    return (num_1 + num_2 + num_3) - min(num_1, num_2, num_3)
num_1 = int(input('Введите первое число: '))
num_2 = int(input('Введите второе число: '))
num_3 = int(input('Введите третье число: '))
print(sum_numbers(num_1, num_2, num_3))

