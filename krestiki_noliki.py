board = [[' ', '1', '2', '3'],
         ['1', '-', '-', '-'],
         ['2', '-', '-', '-'],
         ['3', '-', '-', '-']]

def print_board():
    print(*board[0])
    print(*board[1])
    print(*board[2])
    print(*board[3])


def result():
    victory = [[board[1][1], board[1][2], board[1][3]],
               [board[2][1], board[2][2], board[2][3]],
               [board[3][1], board[3][2], board[3][3]],
               [board[1][1], board[2][1], board[3][1]],
               [board[1][2], board[2][2], board[3][2]],
               [board[1][3], board[2][3], board[3][3]],
               [board[1][1], board[2][2], board[3][3]],
               [board[1][3], board[2][3], board[3][1]]]

    board_ind = [board[1][1], board[1][2], board[1][3],
                 board[2][1], board[2][2], board[2][3],
                 board[3][1], board[3][2], board[3][3]]

    winner = 0

    for n in board_ind:
        if n == '-':
            winner = 0
            break
        else:
            winner = 3

    for i in victory:
         if i[0] == i[1] == i[2] == 'x':
            winner = 1
         elif i[0] == i[1] == i[2] == 'o':
            winner = 2

    return winner

player_1 = True
game_over = False

while not game_over:
    print_board()
    print('-' * 30)
    x = int(input("Игрок, введи номер строки: "))
    y = int(input("Игрок, введи номер столбца: "))
    if 1 <= x <= 3 and 1 <= y <= 3:
        if board[x][y] == '-':
            if player_1:
                board[x][y] = 'x'
            else:
                board[x][y] = 'o'
        else:
            print('-' * 30)
            print('Эта клетка уже занята!')
            print('-' * 30)
            continue
    else:
        print('-' * 30)
        print('Неправильный номер строки или столбца!')
        print('-' * 30)
        continue

    winner = result()

    if winner != 0:
        game_over = True

    player_1 = not player_1

print_board()
if winner in [1, 2]:
    print('-' * 30)
    print(f'Игрок {winner} победил!')
    print('-' * 30)
else:
    print('-' * 30)
    print('Ничья!')
    print('-' * 30)