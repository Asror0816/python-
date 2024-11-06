# Инициализация доски
board = [' '] * 9
curret_player = 'X'

# Основной игровой цикл
while True:
    # Показать доску
    print('\n'.join([' | '.join(board[i:i+3]) for i in range(0, 9, 3)]))

    # Получить ход игрока
    ход = input(f"Игрок {curret_player}, введите ваш ход (1-9): ")
    if ход.isdigit() and 1 <= int(ход) <= 9:
        if board[int(ход) - 1] == ' ':
            board[int(ход) - 1] = curret_player
        else:
            print("Эта ячейка уже занята. Пожалуйста, выберите другую.")
            continue
    else:
        print("Неверный ход. Пожалуйста, введите число от 1 до 9.")
        continue

    # Проверка на победу
    for i in range(0, 9, 3):
        if board[i] == board[i + 1] == board[i + 2] != ' ' or \
           board[i // 3] == board[(i // 3) + 3] == board[(i // 3) + 6] != ' ':
            print(f"Игрок {curret_player} победил!")
            exit()

    if board[0] == board[4] == board[8] != ' ' or board[2] == board[4] == board[6] != ' ':
        print(f"Игрок {curret_player} победил!")
        exit()

    # Проверка на ничью
    if ' ' not in board:
        print("Игра закончилась вничью!")
        exit()

    # Смена игрока
    curret_player = 'O' if curret_player == 'X' else 'X'
