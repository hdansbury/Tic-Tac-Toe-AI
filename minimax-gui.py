import pygame
import sys

# Constants
WIDTH, HEIGHT = 600, 600
LINE_WIDTH = 15
BOARD_ROWS, BOARD_COLS = 3, 3
SQUARE_SIZE = WIDTH // BOARD_COLS
CIRCLE_RADIUS = SQUARE_SIZE // 3
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = SQUARE_SIZE // 4

# Colors
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
CIRCLE_COLOR = (239, 231, 200)
CROSS_COLOR = (66, 66, 66)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tic-Tac-Toe')
screen.fill(BG_COLOR)

# Drawing functions
def draw_lines():
    # 1 horizontal
    pygame.draw.line(screen, LINE_COLOR, (0, SQUARE_SIZE), (WIDTH, SQUARE_SIZE), LINE_WIDTH)
    # 2 horizontal
    pygame.draw.line(screen, LINE_COLOR, (0, 2 * SQUARE_SIZE), (WIDTH, 2 * SQUARE_SIZE), LINE_WIDTH)
    # 1 vertical
    pygame.draw.line(screen, LINE_COLOR, (SQUARE_SIZE, 0), (SQUARE_SIZE, HEIGHT), LINE_WIDTH)
    # 2 vertical
    pygame.draw.line(screen, LINE_COLOR, (2 * SQUARE_SIZE, 0), (2 * SQUARE_SIZE, HEIGHT), LINE_WIDTH)

def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 'O':
                pygame.draw.circle(screen, CIRCLE_COLOR, (int(col * SQUARE_SIZE + SQUARE_SIZE // 2), int(row * SQUARE_SIZE + SQUARE_SIZE // 2)), CIRCLE_RADIUS, CIRCLE_WIDTH)
            elif board[row][col] == 'X':
                pygame.draw.line(screen, CROSS_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE), CROSS_WIDTH)
                pygame.draw.line(screen, CROSS_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE), (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), CROSS_WIDTH)

def mark_square(row, col, player):
    board[row][col] = player

def available_square(row, col):
    return board[row][col] == ' '

def is_board_full():
    return all(cell != ' ' for row in board for cell in row)

def check_win(player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or \
            all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or \
        all(board[i][2-i] == player for i in range(3)):
        return True
    return False

def get_empty_positions():
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']

def minimax(board, depth, is_maximizing):
    if check_win('O'):  # AI wins
        return 1
    if check_win('X'):  # Player wins
        return -1
    if is_board_full():  # Draw
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for move in get_empty_positions():
            board[move[0]][move[1]] = 'O'
            score = minimax(board, depth + 1, False)
            board[move[0]][move[1]] = ' '  # Undo move
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for move in get_empty_positions():
            board[move[0]][move[1]] = 'X'
            score = minimax(board, depth + 1, True)
            board[move[0]][move[1]] = ' '  # Undo move
            best_score = min(score, best_score)
        return best_score

# Minimax AI Move
def ai_move():
    best_score = -float('inf')
    best_move = None
    for move in get_empty_positions():
        board[move[0]][move[1]] = 'O'
        score = minimax(board, 0, False)
        board[move[0]][move[1]] = ' '  # Undo move
        if score > best_score:
            best_score = score
            best_move = move
    return best_move

def reset_game():
    global board, player, game_over
    board = [[' ' for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]
    player = 'X'
    game_over = False
    screen.fill(BG_COLOR)
    draw_lines()


# Main Game Loop 
if __name__ == "__main__":
    # Main game logic
    board = [[' ' for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]
    player = 'X'
    game_over = False

    draw_lines()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if game_over:
                    reset_game()
                elif player == 'X' and not game_over:
                    mouseX = event.pos[0]  # x
                    mouseY = event.pos[1]  # y

                    clicked_row = int(mouseY // SQUARE_SIZE)
                    clicked_col = int(mouseX // SQUARE_SIZE)

                    if available_square(clicked_row, clicked_col):
                        mark_square(clicked_row, clicked_col, player)
                        if check_win(player):
                            game_over = True
                        elif is_board_full():
                            game_over = True
                        else:
                            player = 'O'

        if player == 'O' and not game_over:
            move = ai_move()
            if move:
                mark_square(move[0], move[1], player)
                if check_win(player):
                    game_over = True
                elif is_board_full():
                    game_over = True
                else:
                    player = 'X'

        screen.fill(BG_COLOR)
        draw_lines()
        draw_figures()

        if game_over:
            font = pygame.font.Font(None, 36)
            if check_win('X'):
                text = font.render("Player X wins! Click to restart.", True, CROSS_COLOR)
            elif check_win('O'):
                text = font.render("AI (O) wins! Click to restart.", True, CIRCLE_COLOR)
            else:
                text = font.render("It's a tie! Click to restart.", True, (255, 255, 255))
            screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))

        pygame.display.update()
