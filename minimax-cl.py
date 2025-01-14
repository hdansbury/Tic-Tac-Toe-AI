# Board Methods 
def is_board_full(board):
    return all(cell != ' ' for row in board for cell in row)

def get_empty_positions(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']

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


# AI Methods 
def minimax(board, depth, is_maximizing):
    if check_win(board, 'O'):  # AI wins
        return 1
    if check_win(board, 'X'):  # Player wins
        return -1
    if is_board_full(board):  # Draw
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for move in get_empty_positions(board):
            board[move[0]][move[1]] = 'O'
            score = minimax(board, depth + 1, False)
            board[move[0]][move[1]] = ' '  # Undo move
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for move in get_empty_positions(board):
            board[move[0]][move[1]] = 'X'
            score = minimax(board, depth + 1, True)
            board[move[0]][move[1]] = ' '  # Undo move
            best_score = min(score, best_score)
        return best_score

def ai_move(board):
    best_score = -float('inf')
    best_move = None
    for move in get_empty_positions(board):
        board[move[0]][move[1]] = 'O'
        score = minimax(board, 0, False)
        board[move[0]][move[1]] = ' '  # Undo move
        if score > best_score:
            best_score = score
            best_move = move
    return best_move


# Main Game Loop
if __name__ == "__main__":
    board = [[' ' for _ in range(3)] for _ in range(3)]
    turn = 'X'

    while True:
        print_board(board)
        if turn == 'X':
            while True:
                try:
                    row, col = map(int, input("Enter row and column for X (0-2): ").split())
                    if board[row][col] == ' ':
                        board[row][col] = 'X'
                        break
                    else:
                        print("Cell already taken, try again.")
                except (ValueError, IndexError):
                    print("Invalid input. Please enter numbers 0-2 for row and column.")
        else:
            move = ai_move(board)
            board[move[0]][move[1]] = 'O'
        
        if check_win(board, turn):
            print_board(board)
            print(f"Player {turn} wins!")
            break
        
        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break
        
        turn = 'O' if turn == 'X' else 'X'