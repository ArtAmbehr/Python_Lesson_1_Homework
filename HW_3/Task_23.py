# 23. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, 
# второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

from random import randint

n = int(input('Введите кол-во элементов для списка: '))
initial_list = []
final_list = []

for i in range(n):
    initial_list.append(randint(0, 9))

for i in range(len(initial_list)):
    while i < len(initial_list)/2 and n > len(initial_list)/2:
        n = n - 1
        a = initial_list[i] * initial_list[n]
        final_list.append(a)
        i += 1

print(initial_list)
print(final_list)  

