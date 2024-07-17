import pygame
import random

# Initialize Pygame
pygame.init()

# Set up display
screen = pygame.display.set_mode((540, 600))
pygame.display.set_caption("Sudoku Solver")

# Define grid and cell size
grid_size = 540
cell_size = grid_size // 9
font = pygame.font.Font(None, 36)

# Generate a valid Sudoku board
def generate_board():
    base  = 3
    side  = base * base

    def pattern(r,c): return (base*(r%base)+r//base+c)%side
    def shuffle(s): return random.sample(s, len(s)) 
    r_base = range(base) 
    rows  = [g*base + r for g in shuffle(r_base) for r in shuffle(r_base)] 
    cols  = [g*base + c for g in shuffle(r_base) for c in shuffle(r_base)]
    nums  = shuffle(range(1, base*base + 1))

    board = [[nums[pattern(r, c)] for c in cols] for r in rows]

    squares = side * side
    empties = squares * 3 // 4
    for p in random.sample(range(squares), empties):
        board[p // side][p % side] = 0

    return board

# Draw grid
def draw_grid():
    for x in range(0, grid_size, cell_size):
        for y in range(0, grid_size, cell_size):
            rect = pygame.Rect(x, y, cell_size, cell_size)
            pygame.draw.rect(screen, (0, 0, 0), rect, 1)

    # Draw thicker lines for 3x3 boxes
    for x in range(0, grid_size, cell_size * 3):
        pygame.draw.line(screen, (0, 0, 0), (x, 0), (x, grid_size), 3)
        pygame.draw.line(screen, (0, 0, 0), (0, x), (grid_size, x), 3)

# Draw numbers on the board
def draw_numbers(board, colors):
    for i in range(9):
        for j in range(9):
            if board[i][j] != 0:
                color = colors[i][j] if colors[i][j] else (0, 0, 0)
                text = font.render(str(board[i][j]), True, color)
                screen.blit(text, (j * cell_size + 20, i * cell_size + 15))

# Find empty cell
def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None

# Check if the board is valid
def is_valid(board, num, pos):
    # Check row
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False

    return True

# Solve the Sudoku board using backtracking
def solve(board):
    find = find_empty(board)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if is_valid(board, i, (row, col)):
            board[row][col] = i

            if solve(board):
                return True

            board[row][col] = 0

    return False

# Get the position of the mouse click
def get_clicked_pos(pos):
    x, y = pos
    return y // cell_size, x // cell_size

# Main function
def main():
    board = generate_board()
    colors = [[None for _ in range(9)] for _ in range(9)]
    running = True
    key = None
    selected = None

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                selected = get_clicked_pos(pygame.mouse.get_pos())
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    key = 1
                if event.key == pygame.K_2:
                    key = 2
                if event.key == pygame.K_3:
                    key = 3
                if event.key == pygame.K_4:
                    key = 4
                if event.key == pygame.K_5:
                    key = 5
                if event.key == pygame.K_6:
                    key = 6
                if event.key == pygame.K_7:
                    key = 7
                if event.key == pygame.K_8:
                    key = 8
                if event.key == pygame.K_9:
                    key = 9
                if event.key == pygame.K_DELETE:
                    if selected:
                        row, col = selected
                        board[row][col] = 0
                        colors[row][col] = None
                        key = None
                if event.key == pygame.K_RETURN:
                    solve(board)

                if key is not None and selected is not None:
                    row, col = selected
                    if board[row][col] == 0:
                        if is_valid(board, key, (row, col)):
                            colors[row][col] = (0, 255, 0)  # Green for valid
                            board[row][col] = key
                        else:
                            colors[row][col] = (255, 0, 0)  # Red for invalid
                    key = None

        screen.fill((255, 255, 255))
        draw_grid()
        draw_numbers(board, colors)

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()