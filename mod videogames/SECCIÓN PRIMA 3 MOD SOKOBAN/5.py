import pygame
import sys
import language_tool_python

# Initialize Pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sokoban with Grammar Checker")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Game objects
TILE_SIZE = 50
PLAYER = pygame.Surface((TILE_SIZE, TILE_SIZE))
PLAYER.fill(RED)
BOX = pygame.Surface((TILE_SIZE, TILE_SIZE))
BOX.fill(BLUE)
TARGET = pygame.Surface((TILE_SIZE, TILE_SIZE))
TARGET.fill(GREEN)

# Sokoban level
level = [
    "########",
    "#      #",
    "#  $   #",
    "#  .   #",
    "#  @   #",
    "#      #",
    "########"
]

# Convert level to game objects
player_pos = None
boxes = []
targets = []

for y, row in enumerate(level):
    for x, cell in enumerate(row):
        if cell == '@':
            player_pos = [x, y]
        elif cell == '$':
            boxes.append([x, y])
        elif cell == '.':
            targets.append([x, y])

# Grammar checker
language_tool = language_tool_python.LanguageTool('en-UK')

# Game variables
moves_left = 50
font = pygame.font.Font(None, 36)

# Input box
input_box = pygame.Rect(10, HEIGHT - 50, WIDTH - 20, 40)
input_text = ''
input_active = False

def draw_level():
    for y, row in enumerate(level):
        for x, cell in enumerate(row):
            if cell == '#':
                pygame.draw.rect(screen, BLACK, (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
    
    for target in targets:
        screen.blit(TARGET, (target[0] * TILE_SIZE, target[1] * TILE_SIZE))
    
    for box in boxes:
        screen.blit(BOX, (box[0] * TILE_SIZE, box[1] * TILE_SIZE))
    
    screen.blit(PLAYER, (player_pos[0] * TILE_SIZE, player_pos[1] * TILE_SIZE))

def move_player(dx, dy):
    global moves_left
    new_x, new_y = player_pos[0] + dx, player_pos[1] + dy
    
    if level[new_y][new_x] != '#':
        if [new_x, new_y] in boxes:
            box_new_x, box_new_y = new_x + dx, new_y + dy
            if level[box_new_y][box_new_x] != '#' and [box_new_x, box_new_y] not in boxes:
                boxes[boxes.index([new_x, new_y])] = [box_new_x, box_new_y]
                player_pos[0], player_pos[1] = new_x, new_y
                moves_left -= 1
        else:
            player_pos[0], player_pos[1] = new_x, new_y
            moves_left -= 1

def check_win():
    return all(box in targets for box in boxes)

# Game loop
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                move_player(-1, 0)
            elif event.key == pygame.K_RIGHT:
                move_player(1, 0)
            elif event.key == pygame.K_UP:
                move_player(0, -1)
            elif event.key == pygame.K_DOWN:
                move_player(0, 1)
            elif event.key == pygame.K_RETURN:
                if input_active:
                    mistakes = language_tool.check(input_text)
                    moves_left -= len(mistakes)
                    input_text = ''
            elif event.key == pygame.K_BACKSPACE:
                input_text = input_text[:-1]
            else:
                input_text += event.unicode
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_box.collidepoint(event.pos):
                input_active = not input_active
            else:
                input_active = False

    screen.fill(WHITE)
    draw_level()

    # Draw moves left
    moves_text = font.render(f"Moves left: {moves_left}", True, GREEN)
    screen.blit(moves_text, (10, 10))

    # Draw input box
    pygame.draw.rect(screen, BLACK if input_active else RED, input_box, 2)
    text_surface = font.render(input_text, True, BLACK)
    screen.blit(text_surface, (input_box.x + 5, input_box.y + 5))

    pygame.display.flip()

    if check_win():
        print("You won!")
        running = False
    
    if moves_left <= 0:
        print("Game over!")
        running = False

    clock.tick(60)

pygame.quit()
language_tool.close()
sys.exit()
