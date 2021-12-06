def sum_numbers(numbers_str, stop):
    numbers_list = numbers_str.split(' ')
    sum_list = 0
    for i in numbers_list:
        if i == stop:
            break
        sum_list += int(i)
    return sum_list
stopper = '@'
finish = False
summa = 0
while not finish:
    numbers_str_user = input('Введите строку чисел через прбел: ')
    summa += sum_numbers(numbers_str_user, stopper)
    finish = stopper in numbers_str_user
    print(f'Summa = {summa}')
