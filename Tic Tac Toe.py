current_state = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
turn = [1]


def display_board():
    print(f' {current_state[0]}  |  {current_state[1]}  |  {current_state[2]}')
    print(f'____|_____|____')
    print(f' {current_state[3]}  |  {current_state[4]}  |  {current_state[5]}')
    print(f'____|_____|____')
    print(f' {current_state[6]}  |  {current_state[7]}  |  {current_state[8]}')
    print(f'    |     |    ')
    print('************************')


display_board()


def player_one_move(x):
    if current_state[x] == ' ':
        current_state[x] = 'X'
        turn[0] = 2
    else:
        print('Invalid move, enter another index.')
    display_board()
    player_one_win_check()
    draw_check()


def player_two_move(x):
    if current_state[x] == ' ':
        current_state[x] = 'O'
        turn[0] = 1
    else:
        print('Invalid move, enter another index.')
    display_board()
    player_two_win_check()
    draw_check()


def player_one_win_check():
    if current_state[0] == 'X' and current_state[1] == 'X' and current_state[2] == 'X':
        print('Player One Wins!')
        exit()
    elif current_state[3] == 'X' and current_state[4] == 'X' and current_state[5] == 'X':
        print('Player One Wins!')
        exit()
    elif current_state[6] == 'X' and current_state[7] == 'X' and current_state[8] == 'X':
        print('Player One Wins!')
        exit()
    elif current_state[0] == 'X' and current_state[4] == 'X' and current_state[8] == 'X':
        print('Player One Wins!')
        exit()
    elif current_state[2] == 'X' and current_state[4] == 'X' and current_state[6] == 'X':
        print('Player One Wins!')
        exit()
    elif current_state[0] == 'X' and current_state[3] == 'X' and current_state[6] == 'X':
        print('Player One Wins!')
        exit()
    elif current_state[1] == 'X' and current_state[4] == 'X' and current_state[7] == 'X':
        print('Player One Wins!')
        exit()
    elif current_state[2] == 'X' and current_state[5] == 'X' and current_state[8] == 'X':
        print('Player One Wins!')
        exit()


def player_two_win_check():
    if current_state[0] == 'O' and current_state[1] == 'O' and current_state[2] == 'O':
        print('Player Two Wins!')
        exit()
    elif current_state[3] == 'O' and current_state[4] == 'O' and current_state[5] == 'O':
        print('Player Two Wins!')
        exit()
    elif current_state[6] == 'O' and current_state[7] == 'O' and current_state[8] == 'O':
        print('Player Two Wins!')
        exit()
    elif current_state[0] == 'O' and current_state[4] == 'O' and current_state[8] == 'O':
        print('Player Two Wins!')
        exit()
    elif current_state[2] == 'O' and current_state[4] == 'O' and current_state[6] == 'O':
        print('Player Two Wins!')
        exit()
    elif current_state[0] == 'O' and current_state[3] == 'O' and current_state[6] == 'O':
        print('Player Two Wins!')
        exit()
    elif current_state[1] == 'O' and current_state[4] == 'O' and current_state[7] == 'O':
        print('Player Two Wins!')
        exit()
    elif current_state[2] == 'O' and current_state[5] == 'O' and current_state[8] == 'O':
        print('Player Two Wins!')
        exit()


def draw_check():
    if ' ' not in current_state:
        print('Game is a draw!')
        exit()


while True:
    if turn[0] == 1:
        x = int(input('Player One enter index to play: '))
        player_one_move(x)
    elif turn[0] == 2:
        x = int(input('Player Two enter index to play: '))
        player_two_move(x)
