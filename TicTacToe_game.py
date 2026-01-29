import random

# The board is a 3x3 matrix (list of lists) representing the game grid.
# Squares 1-9 are available targets; 'X' and 'O' represent player moves.

board = [ 
    [1, 2, 3],
    [4, 'X', 6],# The computer always takes the middle square first
    [7, 8, 9]
]


def display_board(board):
    """Prints the current state of the board in a user-friendly ASCII format."""
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
    """Prompts the user for a move, validates input, and updates the board."""
    while True:
        try:
            move = int(input('Enter postion on board: '))
            moved = False

            # Search the 2D list for the number provided by the user
            for row in range(3):
                for col in range(3):
                    if board[row][col] == move:
                        board[row][col] = 'O'
                        moved = True
                        break

            # If moved is True, the input was valid and the square was free
            if moved:
                break
            else:
                print('Space already taken or invalid number')
                        
        except:
            print('Invaild Input')

def make_list_of_free_fields(board):
    """Scans the board and returns a list of tuples containing (row, column) for empty squares."""
    free = []
    for row in range(3):
        for col in range(3):
            # If the square contains a number (not X or O), it is free
            if board[row][col] not in ['X','O']:
                free.append((row, col))
    return free

def bot_move(board):
    """Selects a random square from the available free fields and places an 'X'."""
    free = make_list_of_free_fields(board)
    lol = len(free)
    options = range(0, lol)
    ran = random.randrange(lol)
    free[ran] # Unpack the coordinates from the random selection
    row, col = free[ran]
    board[row][col] = 'X'

def victory_for(board, sign):
    """Checks all possible win conditions (rows, columns, diagonals) for a given sign."""
    # Check rows and columns
    for row in range(3):
        # Horizontal win
        if board[row][0] == sign and board[row][1] == sign and board[row][2] == sign:
            return True
        for col in range(3):
            # Vertical win
            if board[0][col] == sign and board[1][col] == sign and board[2][col] == sign:
                return True
    # Diagonal win (Top-left to Bottom-right)
    if board[0][0] == sign and board[1][1] == sign and board[2][2] == sign:
        return True
    # Diagonal win (Top-right to Bottom-left)
    elif board[0][2] == sign and board[1][1] == sign and board[2][0] == sign:
        return True
    return False

# --- MAIN GAME LOOP ---
while True:           
    display_board(board)
     # Check for a draw (no more free squares)
    if len(make_list_of_free_fields(board)) == 0:
        print('Draw!')
        break
    # Player's turn
    enter_move(board)
    if victory_for(board, 'O'):  
        display_board(board)
        print("Player 1 won!")
        break

    display_board(board)
    # Computer's turn
    bot_move(board)
    if victory_for(board, 'X'):  
        display_board(board)
        print("Bot won!")
        break