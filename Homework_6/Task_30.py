'''
Задача 30: Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество
элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: a
n = a1 + (n-1) * d.
Каждое число вводится с новой строки.
Ввод: 7 2 5
Вывод: 7 9 11 13 15
'''

def InitializationOfVariables():
    a1 = int(input("введите первый элемент прогрессии -> "))
    d = int(input("введите разность прогрессии -> "))
    n = int(input("введите кол-во элемнтов прогрессии -> "))
    return a1, d, n


def FindTheProgression(a1, d, n):
    progression = []
    for i in range(n):
        an = a1 + i * d
        progression.append(an)
    for element in progression:
        print(element)
        



FindTheProgression(*InitializationOfVariables())
