def print_board(board):
    for row in board:
        print('|'.join(row))
        print('-' * 5)
    print()

def check_win(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or \
            all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or \
        all(board[i][2-i] == player for i in range(3)):
        return True
    return False

def is_board_full(board):
    return all(cell != ' ' for row in board for cell in row)

def get_empty_positions(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']

# Main Game Loop
board = [[' ' for _ in range(3)] for _ in range(3)]
turn = 'X'

while True:
    print_board(board)
    
    if turn == 'X':
        while True:
            try:
                row, col = map(int, input("Player X, enter row and column (0-2): ").split())
                if board[row][col] == ' ':
                    board[row][col] = 'X'
                    break
                else:
                    print("Cell already taken, try again.")
            except (ValueError, IndexError):
                print("Invalid input. Please enter numbers 0-2 for row and column.")
    else:
        while True:
            try:
                row, col = map(int, input("Player O, enter row and column (0-2): ").split())
                if board[row][col] == ' ':
                    board[row][col] = 'O'
                    break
                else:
                    print("Cell already taken, try again.")
            except (ValueError, IndexError):
                print("Invalid input. Please enter numbers 0-2 for row and column.")
    
    if check_win(board, turn):
        print_board(board)
        print(f"Player {turn} wins!")
        break
    
    if is_board_full(board):
        print_board(board)
        print("It's a tie!")
        break
    
    turn = 'O' if turn == 'X' else 'X'
