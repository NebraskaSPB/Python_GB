# 123456 -> sum цифр
from fractions import Fraction

numb = Fraction(input("Введите число: "))

while numb % 10 > 0:
    numb = numb * 10
sum = 0

while numb > 0:
    sum = sum + numb % 10
    numb = numb // 10

print(sum)
