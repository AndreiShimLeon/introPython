# Задача 30:
# Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

def arith_progression(first_number = 1, size = 10, diff = 1):
    progression = [first_number]
    for i in range(0, size-1):
        progression.append(progression[i]+diff)
    print(f'Progression: {progression}')
    # return progression


first_number = int(input('Enter first number: \n >>> '))
size = int(input('Enter size: \n >>> '))
diff = int(input('Enter difference: \n >>> '))

arith_progression(first_number, size, diff)
