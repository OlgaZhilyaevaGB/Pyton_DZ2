#Создайте программу для игры с конфетами человек против человека.

# Правила: На столе лежит 150 конфет. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота 'интеллектом'

from random import randint

def Player_vs_player(candi):
    player = 0
    player1 = input('Введите имя первого игрока: ')
    player2 = input('Введите имя второго игрока: ')

    flag = randint(1, 2) #очередность хода
    while candi > 0:
        if flag == 1:
            player = 1
            print(f'Ход игрока {player1}.')
            move = int(input('Введите количество конфет, которые Вы заберете: '))
            while move < 1 or move > 28: #проверка количества
                  move = int(input(f"{player1}, введите правильное количество конфет: "))
            candi -= move
            print(f'Осталось {candi} конфет.')
            if candi == 0:
                break
            player = 2
            print(f'Ход игрока {player2}.')
            move = int(input('Введите количество конфет, которые Вы заберете: '))
            while move < 1 or move > 28:
                  move = int(input(f"{player2}, введите правильное количество конфет: "))
            candi -= move
            print(f'Осталось {candi} конфет.')
        else:
            player = 2
            print(f'Ход игрока {player2}.')
            move = int(input('Введите количество конфет, которые Вы заберете: '))
            while move < 1 or move > 28:
                  move = int(input(f"{player2}, введите правильное количество конфет: "))
            candi -= move
            print(f'Осталось {candi} конфет.')
            if candi == 0:
                break

            player = 1
            print(f'Ход игрока {player1}.')
            move = int(input('Введите количество конфет, которые Вы заберете: '))
            while move < 1 or move > 28:
                  move = int(input(f"{player2}, введите правильное количество конфет: "))
            candi -= move
            print(f'Осталось {candi} конфет.')
   
    winner = player1 if player == 1 else player2
    print(f'Победил игрок {winner}')

def Player_vs_bot (candi, max_move, intel):
    player = 0
    player1 = input('Введите имя  игрока: ')

    flag = randint(1, 2)
    while candi > 0:
        if flag == 1:
            player = 1
            print(f'Ход игрока {player1}.')
            move = int(input('Введите количество конфет, которые Вы заберете: '))
            while move < 1 or move > 28:
                  move = int(input(f"{player1}, введите правильное количество конфет: "))
            candi -= move
            print(f'Осталось {candi} конфет.')
            if candi == 0:
                break
            
            player = 2
            if candi <= max_move:
                move = candi
            else:
                if intel == 0:
                    move = randint(1, max_move)
                else:
                    move = candi - max_move * (candi // max_move) - 1
                    if move <= 0:
                        move += max_move
            print(f'Бот забрал {move} конфет.')
            candi -= move
            print(f'Осталось {candi} конфет.')
        else:
            player == 2
            if candi <= max_move:
                move = candi
            else:
                if intel == 0:
                    move = randint(1, max_move)
                else:
                    move = candi - max_move * (candi // max_move) - 1
                    if move <= 0:
                        move += max_move
            print(f'Бот забрал {move} конфет.')
            candi -= move
            print(f'Осталось {candi} конфет.')
            if candi == 0:
                break

            player = 1
            print(f'Ход игрока {player1}.')
            move = int(input('Введите количество конфет, которые Вы заберете: '))
            candi -= move
            print(f'Осталось {candi} конфет.')
    if player == 1:
        winner = player1
    else:
        winner = 'Бот'
    print(f'Победил(а) {winner}')



candies = int(input("Введите количество конфет на столе: "))
max_move = 28
type_game = int(input('Введите 1, если хотите играть с другим игроком, или любую другую цифру, если с ботом... '))
if(type_game == 1):
    Player_vs_player(candies)
else:
    intel = int(input('Введите 0, если хотите играть с глупым ботом, или любую другую цифру, если с умным... '))
    Player_vs_bot(candies, max_move, intel)