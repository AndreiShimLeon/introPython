#==================================================================================================================================
# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой,
# а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть
#
# promptMessage = 'Введите количество монет на столе: \n'
# inputErrorMessage = 'Вы ввели неверное число.'
# sideEnterMessage = 'Введите верхнюю сторону (1 для решки, 0 для герба) для монетки #'
# flipOverMessage = 'Для того, чтобы все монетки лежали одной стороной вверх, нужно перевернуть'
# flag = True
# coinsNumber = 0
# while flag:
#     try:
#         coinsNumber = int(input(promptMessage))
#         if coinsNumber > 0:
#             flag = False
#         else:
#             print(inputErrorMessage)
#
#     except ValueError:
#         print(inputErrorMessage)
#
# coinsList = []
# counter = 1;
# upperSides = 0
# lowerSides = 0
# while coinsNumber > 0:
#     side = int(input(f"{sideEnterMessage}{counter}: \n"))
#     if side != 1 and side != 0:
#         print(inputErrorMessage)
#     else:
#         coinsList.append(side)
#         counter += 1
#         coinsNumber -= 1
#         if side == 1:
#             upperSides+=1
#         else:
#             lowerSides+=1
#
# print(f'На столе лежит {counter-1} монеток следующими сторонами вверх: {coinsList}')
# if upperSides > lowerSides:
#     print(f'{flipOverMessage} {lowerSides} из них.')
# else:
#     print(f'{flipOverMessage} {upperSides} из них.')
#==================================================================================================================================


#==================================================================================================================================
# Задача 12: Петя и Катя – брат и сестра. Петя – студент,
# а Катя – школьница. Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000),
# а Катя должна их отгадать. Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.
#
# limit = 1000
# introductionMessage = f'Петя должен загадать два натуральных числа до {limit} включительно.'
# sumMessage = 'Петя говорит, что сумма чисел равна:\n'
# multMessage = 'Петя говорит, что произведение чисел равно:\n'
# endMessage = 'Кате следует назвать пару чисел:'
# errorMessage = 'Кате следует сказать, что Петя ошибся, когда загадывал числа или когда называл их сумму и произведение.'
#
# print(introductionMessage)
# S = int(input(sumMessage))
# P = int(input(multMessage))
# firstNumber = 1
# secondNumber = 1
# flag = True
# while flag:
#     if secondNumber > limit:
#         flag = False
#         print(errorMessage)
#     else:
#         for i in range(limit):
#             if firstNumber + secondNumber == S and firstNumber*secondNumber == P:
#                 flag = False
#                 print(f'{endMessage} {firstNumber}, {secondNumber}')
#             firstNumber+=1
#         firstNumber = 1
#         secondNumber += 1
#==================================================================================================================================



# Задача 14: Требуется вывести все целые степени двойки
# (т.е. числа вида 2^k), не превосходящие числа N.

# N = int(input('Введите число : \n'))
# numbers = []
# i = 0
# while 2**i <= N:
#     str = f"2^{i}"
#     numbers.append(str)
#     print(f'2^{i} = {2 ** i}')
#     i+=1
# print(f'степени двойки, которые меньше введенного числа {N}: {numbers}')
#==================================================================================================================================