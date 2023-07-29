# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику.
# Она растёт на круглой грядке, причём кусты высажены только по окружности.
# Таким образом, у каждого куста есть ровно два соседних.
# Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора
# на них выросло различное число ягод — на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом,
# собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать
# за один заход собирающий модуль, находясь перед некоторым кустом заданной
# во входном файле грядки.
#
# 3 1 2 4
from random import randrange

# Количество кустов:
bushes = 10
# Случайная урожайность на каждый куст:
berries = []
for bush in range(bushes):
    berries.append(randrange(0,20))
print(f'Ягоды на кустах: {berries}')

sum = int()
best_position = int()
for bush in range(len(berries)):
    if bush == 0:
        max = berries[-1] + berries[bush] + berries[bush+1]
        sum = max
    elif bush == len(berries) - 1:
        sum = berries[-2]+berries[-1]+berries[1]
    else:
        sum = berries[bush-1]+berries[bush]+berries[bush+1]
    if sum > max:
        max = sum
        best_position = bush+1
    print(f'Робот на позиции №{bush+1} соберет {sum} шт. ')
    sum = 0
print(f'Робот может собрать за один заход максимум {max} шт. на позиции №{best_position}')