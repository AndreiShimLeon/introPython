# Задача 26: Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8
# def power_recursion(number, power):
#     if power == 0:
#         return 1
#     elif power > 0:
#         if power == 1:
#             return number
#         else:
#             return number*power_recursion(number, power-1)
#     elif power < 0:
#         if power == -1:
#             return 1/number
#         else:
#             return 1/number*power_recursion(number, power+1)
#
# A = int(input('Enter number: \n >>>'))
# B = int(input('Enter power: \n >>>'))
# print(round(power_recursion(A,B),6))

# ===================================================================================================
# Задача 28: Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел. Из
# всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.
# 2 2
# >>> 4

# def sum(numberA, numberB):
#     if numberA == 0:
#         return numberB
#     elif numberB == 0:
#         return numberA
#     else:
#         return 1+sum(numberA, numberB-1)
#
# A = int(input('Enter number A: \n >>>'))
# B = int(input('Enter number B: \n >>>'))
# print(f'Sum of {A} and {B} equals: \n >>> {sum(A,B)}')

# ===================================================================================================
# Задача №39. Решение в группах
# Даны два массива чисел. Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит
# число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество
# элементов во втором массиве. Затем элементы второго массива
# Ввод:
# 7 - размер первого массива
# 3 1 3 4 2 4 12
# 6 - размер второго массива
# 4 15 43 1 15 1 (каждое число вводится с новой строки)
# Вывод:
# 3 3 2 12

# def create_array():
#     size = int(input('Enter size of array: \n  >>>'))
#     array = list()
#     for i in range(size):
#         array.append(int(input(f'Enter element #{i+1}: \n >>>')))
#     return array
#
# def print_originals(list_1, list_2):
#         for item in list_1:
#             i = int()
#             flag = True
#             while flag:
#                 if item == list_2[i]:
#                     flag = False
#                 i+= 1
#                 if i == len(list_2):
#                     flag = False
#                     print(f'{item}', end = ' ')
#
#
# list_1 = (3, 1, 3, 4, 2, 4, 12)
# list_2 = (4, 15, 43, 1, 15, 1)
# print_originals(list_1, list_2)
#

# #===================================================================================================
#
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая в данном массиве определит
# количество элементов, у которых два соседних и, при
# этом, оба соседних элемента меньше данного. Сначала
# вводится число N — количество элементов в массиве
# Далее записаны N чисел — элементы массива. Массив
# состоит из целых чисел.
# >>> 5
# >>> 1 2 3 4 5
# print 0
# >>> 5
# >>> 1 5 1 5 1
# print 2

# def create_array():
#     size = int(input('Enter size of array: \n  >>>'))
#     array = list()
#     for i in range(size):
#         array.append(int(input(f'Enter element #{i+1}: \n >>>')))
#     return array
#
#
# def find_elements_with_two_little_neighbors(list_1):
#     counter = int()
#     for i in range(1,len(list_1) -1):
#         if list_1[i-1] < list_1[i] and list_1[i+1] < list_1[i]:
#             counter += 1
#     print(counter)
#
# find_elements_with_two_little_neighbors(create_array())
# #===================================================================================================
# Задача №43. Решение в группах
# Дан список чисел. Посчитайте, сколько в нем пар
# элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список
# чисел. Все числа списка находятся на разных
# строках.
# Ввод:
# 1 2 3 2 3
# Вывод: 2

# def create_array():
#     size = int(input('Enter size of array: \n  >>>'))
#     array = list()
#     for i in range(size):
#         array.append(int(input(f'Enter element #{i+1}: \n >>>')))
#     return array
#
#
# def pairs_of_equals(list_1):
#     counter = int()
#     while len(list_1) != 1:
#         flag1, i = True, 1
#         while flag1:
#             # print(f'{list_1[0]} >>> {list_1[i]}')
#             if list_1[0] == list_1[i]:
#                 flag1 = False
#                 counter += 1
#                 del list_1[i], list_1[0]
#             i+=1
#             if i == len(list_1):
#                 flag1 = False
#                 del list_1[0]
#         # print(list_1)
#     return counter
#
# # list_new = create_array()
# list_new = [1,2,3,4,5,6,6,7,8,1,2,3,4] #
# print(pairs_of_equals(list_new))
# #===================================================================================================
# Задача №45. Решение в группах
# Два различных натуральных числа n и m называются
# дружественными, если сумма делителей числа n
# (включая 1, но исключая само n) равна числу m и
# наоборот. Например, 220 и 284 – дружественные числа.
# По данному числу k выведите все пары дружественных
# чисел, каждое из которых не превосходит k. Программа
# получает на вход одно натуральное число k, не
# превосходящее 10**5
# . Программа должна вывести все
# пары дружественных чисел, каждое из которых не
# превосходит k. Пары необходимо выводить по одной в
# строке, разделяя пробелами. Каждая пара должна быть
# выведена только один раз (перестановка чисел новую
# пару не дает).
# Ввод:
# 300
# Вывод:
# 220 284

def dividers_sum(number):
    sum = int()
    for i in range(1,number):
        if number%i == 0:
            sum += i
    return sum

def friendly_pairs(limit_number):
    list_of_friendly_pairs = list()
    exceptions = set()
    dividers_sum_dict = dict()
    for i in range(limit_number):
        for k in range(limit_number):
            if i == 0:
                dividers_sum_dict[k] = dividers_sum(k)
            if k%1000 ==0: print(k)
            if dividers_sum_dict[i] == k and dividers_sum_dict[k] == i and i != k and k not in exceptions and i not in exceptions:
                list_of_friendly_pairs.append(sorted([i,k]))
                exceptions.add(i), exceptions.add(k)
                # list_of_friendly_pairs.append(i)®
        print(i)
    print(exceptions)
    print(dividers_sum_dict)
    return list_of_friendly_pairs


print(friendly_pairs(100000))