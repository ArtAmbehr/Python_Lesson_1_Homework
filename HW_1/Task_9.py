# 9.	Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

n = int(input('Введите номер четверти от 1 до 4: '))
if n == 1:
    print('Точка находится в диапазоне \nX: от 0 до +∞ \nY: от 0 до +∞')
if n == 2:
    print('Точка находится в диапазоне \nX: от 0 до -∞ \nY: от 0 до +∞')
if n == 3:
    print('Точка находится в диапазоне \nX: от 0 до -∞ \nY: от 0 до -∞')
if n == 4:
    print('Точка находится в диапазоне \nX: от 0 до +∞ \nY: от 0 до -∞')      
else:
    print ('Введенная цифра не является номером четверти. Введите цифру от 1 до 4')         