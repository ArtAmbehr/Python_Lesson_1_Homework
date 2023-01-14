# # 39(1). Реализовать игру игрока против игрока # в терминале. 
# # Игроки ходят друг за другом, вписывая желаемое количество конфет. 
# # Первый ход определяется жеребьёвкой. В конце вывести игрока, который победил
# # Условие задачи: На столе лежит 221 конфета. Играют два игрока делая ход друг после друга. 
# # Первый ход определяется жеребьёвкой. 
# # За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. 

import random
player1 = input ('Первый игрок, как Вас зовут? ')
player2 = input ('Второй игрок, как Вас зовут? ')
whoIsTheFirst = random.randrange(1,3)
a = int(input('Введите количество конфет: '))
if whoIsTheFirst==1:
    print ('Первый ход делает', player1)
else:
    print ('Первый ход делает', player2)

while a>0:
    if a>28:
        firstPlayer = int(input('Возьми, максимум, 28 конфет: '))    
        a = a - firstPlayer
        if a>28:
            secondPlayer = int(input('Теперь ты возьми не более 28 конфет: '))    
            a = a - secondPlayer
            if a<=28:
                if whoIsTheFirst == 1:
                    print('Осталось ', a, 'шт., их забирает', player1, 'и победил ', player1)
                else:
                    print('Осталось ', a, 'шт., их забирает', player2, 'и победил ', player2)
        
        else:
            if whoIsTheFirst == 1:
                print('Осталось ', a, 'шт., их забирает', player2, 'и победил ', player2)
            else:
                print('Осталось ', a, 'шт., их забирает', player1, 'и победил ', player1)

# ---------------------------------------------

# В качестве дополнительного усложнения можно:
#         a) Добавьте игру против бота ( где бот берет рандомное количество конфет от 0 до 28)
#         b) Подумайте как наделить бота ""интеллектом"" (есть алгоритм, позволяющий выяснить какое количесвто конфет необходимо брать, чтобы гарантированно победить, соответственно внедрить этот алгоритм боту )

# Ниже игра против бота - просьба раскомментировать при проверке.

# import random
# from random import randint, choice
 
# messages = ['Ваш ход', 'Возьмите конфеты']
# max_number_move = 0
 
# def introduce_players():
#     player1 = input('Первый игрок, представьтесь\n')
#     player2 = 'SmartBOT'
#     print(f'Вы играете с искуственным {player2}')
#     return [player1, player2]
 
# def sweets_game(players):
#     global max_number_move
#     total_sweets = int(input('Введите количество конфет в игре:\n'))
#     max_number_move = int(input('Введите количество конфет, которое можно забрать за один ход:\n'))
#     first = int(input(f'{players[0]}, если хотите ходить первым, нажмите 1, если нет, любую другую клавишу\n'))
#     if first != 1:
#         first = 0
#     return [total_sweets, max_number_move, int(first)]
 
# max_move = max_number_move
 
# def game_player_vs_smart_bot(sweets, players, messages):
#     global max_number_move
#     count = sweets[2]
 
 
#     while sweets[0] > 0:
#         if sweets[0] == (max_number_move and sweets[0] < max_number_move and sweets[0] > 1):
#             move = sweets[0] -1
#             print(f'Бот забирает {move}')
 
#         elif not count % 2:
#             move = random.randint(1, sweets[1])
#             print(f'Бот забирает {move}')
#         else:
#             print(f'{players[0]}, {choice(messages)}')
#             move = int(input())
#             if move > sweets[0] or move > sweets[1]:
#                 print(
#                     f'Можно взять не более {sweets[1]} конфет, у нас всего {sweets[0]} конфет')
#                 chance = 2
#                 while chance > 0:
#                     if sweets[0] >= move <= sweets[1]:
#                         break
#                     print(f'Попробуйте ещё раз, у Вас {chance} попытки')
#                     move = int(input())
#                     chance -= 1
#                 else:
#                     return print(f'Попыток не осталось. Game over!')
#         sweets[0] = sweets[0] - move
#         if sweets[0] > 0:
#             print(f'Осталось {sweets[0]} конфет')
#         else:
#             print('Конфеты закончились.')
#         count += 1
#     return players[not count % 2]
 
 
# players = introduce_players()
# sweets = sweets_game(players)
 
# winer = game_player_vs_smart_bot(sweets, players, messages)
# if not winer:
#     print('У нас нет победителя.')
# else:
#     print(
#         f'Победил {winer}. Он забирает все конфеты.')