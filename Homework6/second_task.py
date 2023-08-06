
# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

# Ввод: [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]
def find_indexes(array, lower_limit, upper_limit):
    result = list()
    for i in range(len(array)):
        if array[i] >= lower_limit and array[i] <= upper_limit:
            result.append(i)
    return result


list1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
min_limit = 7
max_limit = 10


print(find_indexes(list1, min_limit, max_limit))
