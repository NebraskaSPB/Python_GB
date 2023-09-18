# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)
import random
def InitializationMinMax():
    max = int(input("Введите максимальное число массива: ")) 
    min = int(input("Введите минимальное число массива: "))
    mas=[random.randint(0, 50) for i in range(random.randint(10,20))]
    print(*mas)
    return max, min, mas

def FindingTheRange(max, min, mas):
    arr = []
    for i in range(len(mas)):
        if mas[i] >= min and mas[i] <= max:
            arr.append(i)
    return arr


findingTheRange=FindingTheRange(*InitializationMinMax())
print(findingTheRange)