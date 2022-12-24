# 25. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

binary = ""
decimal = int(input("Введите число: "))
while decimal != 0:
    binary = str(decimal%2) + binary
    decimal //=2
print(binary)
