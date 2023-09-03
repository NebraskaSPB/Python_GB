'''
Задача №11.
Дано натуральное число A > 1. Определите, каким по 
счету числом Фибоначчи оно является, то есть 
выведите такое число n, что φ(n)=A. Если А не 
является числом Фибоначчи, выведите число -1.
Input: 5
Output: 6
'''
def fibonachi(numb):
    n1 = 0
    n2 = 1
    res = 0
    count = 2

    while res < A:
        res = n1 + n2
        n1 = n2
        n2 = res
        count+=1
    if res == numb:
        return count
    else:
        return (f"Вы ввели число не из ряда фибоначи, ближайшее число {n1}")

try:
    A = int(input("Введите число Фибоначи: "))
    print(fibonachi(A))
except:
    print("Ввели неверные данные")