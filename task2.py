# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

X = int(input('Введите любое число X: '))
Y = int(input('Введите любое число Y: '))
Z = int(input('Введите любое число Z: '))

rightSide = not (X or Y or Z)
leftSide = not X and not Y and not Z
result = rightSide == leftSide

if result == True:
    print(f'Утверждение ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z является истинным (Результат проверки: {result}).')
else:
    print(f'Утверждение ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z является ложным (Результат проверки: {result}).')




