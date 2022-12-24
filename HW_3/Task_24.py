# 24. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным 
# и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

list = [1.1, 1.2, 3.1, 5, 10.01]
final_list = [round(i%1,2) for i in list if i%1 != 0]
difference = (max(final_list)) - (min(final_list))

print(list)
print(final_list)
print(difference)