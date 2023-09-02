'''
Задача №3. Решение в группах
В некоторой школе решили набрать три новых 
математических класса и оборудовать кабинеты для 
них новыми партами. За каждой партой может сидеть 
два учащихся. Известно количество учащихся в 
каждом из трех классов. Выведите наименьшее 
число парт, которое нужно приобрести для них.
Input: 20 21 22(ввод чисел НЕ в одну строку)
Output: 32
'''
NewMathClasses = 3
NewMathClassNumb1 = int(input('В 1 математичесокм классе: '))
NewMathClassNumb2 = int(input('В 2 математичесокм классе: '))
NewMathClassNumb3 = int(input('В 3 математичесокм классе: '))
NumberOfPeopleAt1Desk = 2

sum = 0
for NumberOfPeopleAt1Desk in (NewMathClassNumb1, NewMathClassNumb2, NewMathClassNumb3):
    sum += NumberOfPeopleAt1Desk // 2 + NumberOfPeopleAt1Desk % 2
print(sum)

'''
NewMathClasses = 3
NewMathClassNumb1 = int(input('В 1 математичесокм классе: '))
NewMathClassNumb2 = int(input('В 2 математичесокм классе: '))
NewMathClassNumb3 = int(input('В 3 математичесокм классе: '))
NumberOfPeopleAt1Desk = 2
NumberOfDesks1 = (NewMathClassNumb1 // NumberOfPeopleAt1Desk + NewMathClassNumb1 % NumberOfPeopleAt1Desk)
NumberOfDesks2 = (NewMathClassNumb2 // NumberOfPeopleAt1Desk + NewMathClassNumb2 % NumberOfPeopleAt1Desk)
NumberOfDesks3 = (NewMathClassNumb3 // NumberOfPeopleAt1Desk + NewMathClassNumb3 % NumberOfPeopleAt1Desk)
NumberOfDesks = NumberOfDesks1 + NumberOfDesks2 + NumberOfDesks3
print(NumberOfDesks)
'''