# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

dayNumber = int(input('Введите число от 1 до 7: '))

while dayNumber > 7 or dayNumber < 1:
    dayNumber = int(input('Введите число от 1 до 7: '))

if dayNumber == 6 or dayNumber == 7:
    print('Это выходной день.')
else:
    print('Это рабочий день.')