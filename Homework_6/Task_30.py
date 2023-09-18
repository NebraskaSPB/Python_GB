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
