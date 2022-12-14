# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
# в которой находится эта точка (или на какой оси она находится).

coordinateX = float(input('Введите значение координаты X: '))
while coordinateX == 0:
    coordinateX = float(input('Введите значение координаты X, которое НЕ РАВНО нулю : '))

coordinateY = float(input('Введите значение координаты Y: '))
while coordinateY == 0:
    coordinateY = float(input('Введите значение координаты Y, которое НЕ РАВНО нулю : '))

if coordinateX > 0 and coordinateY > 0:
    print('Заданная точка находится в I-ой координатной четверти.')
elif coordinateX < 0 and coordinateY > 0:
    print('Заданная точка находится во II-ой координатной четверти.')
elif coordinateX < 0 and coordinateY < 0:
    print('Заданная точка находится в III-ей координатной четверти.')
elif coordinateX > 0 and coordinateY < 0:
    print('Заданная точка находится в IV-ой координатной четверти.')
