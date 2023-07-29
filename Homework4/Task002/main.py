# Задача 22: Даны два неупорядоченных набора целых чисел
# (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа,
# которые встречаются в обоих наборах.
# Пользователь вводит 2 числа.
# n — кол-во элементов первого множества.
# m — кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.

from random import randrange


def create_random_number_list(size, limit):
    number_list = []
    for i in range(size):
        number_list.append(randrange(-limit, limit))
    return number_list


def print_list(number_list,message = ''):
    print(message, end = ' ')
    for i in number_list:
        print(i, end=' ')
    print('\n')


def fill_in_empty_list(number_list, size):
    for i in range(size):
        print(f'Введите {i+1}-й элемент списка >>> ', end = '')
        number_list.append(int(input()))


def common_numbers_in_two_lists(number_list1, number_list2):
    common_numbers = set(number_list1).intersection(set(number_list2))
    return list(common_numbers)


def qsort(number_list):
    left = []
    equal = []
    right = []
    if len(number_list) > 1:
        pivot = number_list[(len(number_list)-1)//2]
        for i in number_list:
            if i < pivot:
                left.append(i)
            elif i == pivot:
                equal.append(i)
            elif i > pivot:
                right.append(i)
        return qsort(left)+equal+qsort(right)
    else:
        return number_list



# valueLimit = 10
# lowerLimit = 100
# upperLimit = 200
# n = randrange(lowerLimit, upperLimit)
# m = randrange(lowerLimit, upperLimit)
# list1 = create_random_number_list(n, valueLimit)
# list2 = create_random_number_list(m, valueLimit)

n = int(input('Введите количество элементов 1-го списка: \n >>> '))
list1 = []
fill_in_empty_list(list1, n)
m = int(input('Введите количество элементов 2-го списка: \n >>> '))
list2 = []
fill_in_empty_list(list2, m)

print_list(list1, 'Первый список:')
print_list(list2, 'Второй список:')
print_list(qsort(common_numbers_in_two_lists(list1,list2)),f'Числа,которые встречаются в обоих наборах: ')

