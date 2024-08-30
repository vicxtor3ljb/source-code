import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
PURPLE = (128, 0, 128)

# Player
player_width = 50
player_height = 50
player_x = WIDTH // 2 - player_width // 2
player_y = HEIGHT - player_height - 10
player_speed = 5
player_lives = 3

# Bullet
bullet_width = 5
bullet_height = 15
bullet_speed = 7
bullet_state = "ready"
bullet_x = 0
bullet_y = 0

# Enemies
enemy_width = 50
enemy_height = 50
enemy_x = [100, 300, 500, 700]
enemy_y = [50, 50, 50, 50]
enemy_speed = 2
enemy_colors = [BLUE, GREEN, PURPLE, WHITE]

# Game variables
score = 0
stage = 1
game_state = "menu"

# Fonts
font = pygame.font.Font(None, 36)

def draw_player(x, y):
    pygame.draw.rect(screen, WHITE, (x, y, player_width, player_height))

def draw_bullet(x, y, color):
    pygame.draw.rect(screen, color, (x, y, bullet_width, bullet_height))

def draw_enemy(x, y, color):
    pygame.draw.rect(screen, color, (x, y, enemy_width, enemy_height))

def show_score():
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

def show_lives():
    lives_text = font.render(f"Lives: {player_lives}", True, WHITE)
    screen.blit(lives_text, (WIDTH - 100, 10))

def show_stage():
    stage_text = font.render(f"Stage: {stage}", True, WHITE)
    screen.blit(stage_text, (WIDTH // 2 - 50, 10))

def show_menu():
    title_text = font.render("Space Invaders", True, WHITE)
    start_text = font.render("Press SPACE to start", True, WHITE)
    screen.blit(title_text, (WIDTH // 2 - 100, HEIGHT // 2 - 50))
    screen.blit(start_text, (WIDTH // 2 - 120, HEIGHT // 2 + 50))

def show_pause_menu():
    pause_text = font.render("PAUSED", True, WHITE)
    resume_text = font.render("Press P to resume", True, WHITE)
    screen.blit(pause_text, (WIDTH // 2 - 50, HEIGHT // 2 - 50))
    screen.blit(resume_text, (WIDTH // 2 - 100, HEIGHT // 2 + 50))

def show_win_screen():
    win_text = font.render("You Win!", True, WHITE)
    restart_text = font.render("Press R to restart", True, WHITE)
    screen.blit(win_text, (WIDTH // 2 - 50, HEIGHT // 2 - 50))
    screen.blit(restart_text, (WIDTH // 2 - 100, HEIGHT // 2 + 50))

def reset_game():
    global player_x, player_y, enemy_x, enemy_y, score, stage, game_state, player_lives
    player_x = WIDTH // 2 - player_width // 2
    player_y = HEIGHT - player_height - 10
    enemy_x = [100, 300, 500, 700]
    enemy_y = [50, 50, 50, 50]
    score = 0
    stage = 1
    game_state = "playing"
    player_lives = 3

# Game loop
clock = pygame.time.Clock()
running = True

while running:
    screen.fill(BLACK)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if game_state == "menu" and event.key == pygame.K_SPACE:
                game_state = "playing"
            elif game_state == "playing" and event.key == pygame.K_p:
                game_state = "paused"
            elif game_state == "paused" and event.key == pygame.K_p:
                game_state = "playing"
            elif game_state == "win" and event.key == pygame.K_r:
                reset_game()
            
            if game_state == "playing":
                if event.key == pygame.K_SPACE and bullet_state == "ready":
                    bullet_x = player_x + player_width // 2 - bullet_width // 2
                    bullet_y = player_y
                    bullet_state = "fire"
    
    if game_state == "menu":
        show_menu()
    elif game_state == "paused":
        show_pause_menu()
    elif game_state == "win":
        show_win_screen()
    elif game_state == "playing":
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x < WIDTH - player_width:
            player_x += player_speed
        
        # Move bullet
        if bullet_state == "fire":
            bullet_y -= bullet_speed
            if bullet_y <= 0:
                bullet_state = "ready"
        
        # Move enemies
        for i in range(4):
            enemy_x[i] += enemy_speed
            if enemy_x[i] <= 0 or enemy_x[i] >= WIDTH - enemy_width:
                enemy_speed *= -1
                for j in range(4):
                    enemy_y[j] += 20
        
        # Check for collisions
        for i in range(4):
            if (bullet_x < enemy_x[i] + enemy_width and
                bullet_x + bullet_width > enemy_x[i] and
                bullet_y < enemy_y[i] + enemy_height and
                bullet_y + bullet_height > enemy_y[i]):
                
                if (stage == 1 and i == 0) or (stage == 2 and i == 1) or (stage == 3 and i == 2) or (stage == 4 and i == 3):
                    score += 10
                    stage += 1
                    if stage > 4:
                        game_state = "win"
                    else:
                        enemy_x = [100, 300, 500, 700]
                        enemy_y = [50, 50, 50, 50]
                else:
                    enemy_x = [100, 300, 500, 700]
                    enemy_y = [50, 50, 50, 50]
                
                bullet_state = "ready"
        
        # Check for player collision
        for i in range(4):
            if (player_x < enemy_x[i] + enemy_width and
                player_x + player_width > enemy_x[i] and
                player_y < enemy_y[i] + enemy_height and
                player_y + player_height > enemy_y[i]):
                player_lives -= 1
                if player_lives <= 0:
                    game_state = "menu"
                else:
                    player_x = WIDTH // 2 - player_width // 2
                    player_y = HEIGHT - player_height - 10
                    enemy_x = [100, 300, 500, 700]
                    enemy_y = [50, 50, 50, 50]
        
        # Draw game objects
        draw_player(player_x, player_y)
        if bullet_state == "fire":
            draw_bullet(bullet_x, bullet_y, enemy_colors[stage - 1])
        for i in range(4):
            draw_enemy(enemy_x[i], enemy_y[i], enemy_colors[i])
        
        show_score()
        show_lives()
        show_stage()
    
    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()
