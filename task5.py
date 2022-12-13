# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

from math import *

coordinateX1 = float(input('Введите значение координаты X (для первой точки): '))
while coordinateX1 == 0:
    coordinateX1 = float(input('Введите значение координаты X, которое НЕ РАВНО нулю (для первой точки): '))

coordinateY1 = float(input('Введите значение координаты Y (для первой точки): '))
while coordinateY1 == 0:
    coordinateY1 = float(input('Введите значение координаты Y, которое НЕ РАВНО нулю (для первой точки): '))

coordinateX2 = float(input('Введите значение координаты X (для второй точки): '))
while coordinateX2 == 0:
    coordinateX2 = float(input('Введите значение координаты X, которое НЕ РАВНО нулю (для второй точки): '))

coordinateY2 = float(input('Введите значение координаты Y (для второй точки): '))
while coordinateY2 == 0:
    coordinateY2 = float(input('Введите значение координаты Y, которое НЕ РАВНО нулю (для второй точки): '))

distance = sqrt((coordinateX2 - coordinateX1)**2 + (coordinateY2 - coordinateY1)**2)

print(f'Расстояние между указанными точками составляет: {round(distance, 3)}.')