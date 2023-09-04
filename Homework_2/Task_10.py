# Задача 10: 
# На столе лежат n монеток. 
# Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть


import random

def min_numb_of_coins(total_coins):
    eagle = 0
    tails = 1
    count_eagles = count_tails = 0
    for i in range(total_coins):
        mass = random.randint(eagle, tails)
        print(mass, end = " ")
        if mass == eagle:
            count_eagles +=1
        elif mass == tails:
            count_tails +=1
        else:
            print("Что-то пошло не так!")
    if count_eagles <= count_tails:
        return count_eagles
    else:
        return count_tails

            


n = int(input("Введите кол-во монет -> "))

print(f"Минимально количество монет, чтобы все монетки были повернуты одной стороной равно:  {min_numb_of_coins(n)}")