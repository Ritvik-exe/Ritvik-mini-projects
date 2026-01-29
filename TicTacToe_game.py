import random
board = [
    [1, 2, 3],
    [4, 'X', 6],
    [7, 8, 9]
]


def display_board(board):
    print(f'''        +--------------+---------------+--------------+
        |              |               |              |
        |      {board[0][0]}       |       {board[0][1]}       |       {board[0][2]}      |
        |              |               |              |     
        +--------------+---------------+--------------+
        |              |               |              |
        |      {board[1][0]}       |       {board[1][1]}       |       {board[1][2]}      |
        |              |               |              |
        +--------------+---------------+--------------+
        |              |               |              |
        |      {board[2][0]}       |       {board[2][1]}       |       {board[2][2]}      |
        |              |               |              |
        +--------------+---------------+--------------+                                                      ''')

def enter_move(board):
    while True:
        try:
            move = int(input('Enter postion on board: '))
            moved = False
            for row in range(3):
                for col in range(3):
                    if board[row][col] == move:
                        board[row][col] = 'O'
                        moved = True
                        break
            if moved:
                break
            else:
                print('Space already taken or invalid number')
                        
        except:
            print('Invaild Input')

def make_list_of_free_fields(board):
    free = []
    for row in range(3):
        for col in range(3):
            if board[row][col] not in ['X','O']:
                free.append((row, col))
    return free

def bot_move(board):
    free = make_list_of_free_fields(board)
    lol = len(free)
    options = range(0, lol)
    ran = random.randrange(lol)
    free[ran]
    row, col = free[ran]
    board[row][col] = 'X'

def victory_for(board, sign):
    for row in range(3):
        if board[row][0] == sign and board[row][1] == sign and board[row][2] == sign:
            return True
        for col in range(3):
            if board[0][col] == sign and board[1][col] == sign and board[2][col] == sign:
                return True
    if board[0][0] == sign and board[1][1] == sign and board[2][2] == sign:
        return True
    elif board[0][2] == sign and board[1][1] == sign and board[2][0] == sign:
        return True
    return False

while True:           
    display_board(board)
    if len(make_list_of_free_fields(board)) == 0:
        print('Draw!')
        break
    enter_move(board)
    if victory_for(board, 'O'):  
        display_board(board)
        print("Player 1 won!")
        break
    display_board(board)
    bot_move(board)
    if victory_for(board, 'X'):  
        display_board(board)
        print("Bot won!")
        break