import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Colors
colors = {
    "red": (255, 0, 0),
    "green": (0, 255, 0),
    "blue": (0, 0, 255),
    "yellow": (255, 255, 0)
}

# Player settings
player_width = 50
player_height = 50
player_x = screen_width // 2 - player_width // 2
player_y = screen_height - player_height - 10
player_speed = 5

# Enemy settings
enemy_width = 50
enemy_height = 50
enemy_speed = 1
enemies = []

# Bullet settings
bullet_width = 5
bullet_height = 10
bullet_speed = 7
bullets = []

# Game settings
score = 0
font = pygame.font.SysFont(None, 35)
game_over = False

def show_score(x, y):
    score_display = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_display, (x, y))

# Main loop
running = True
clock = pygame.time.Clock()

# Enemy colors for each level
enemy_colors = list(colors.values())

while running:
    clock.tick(60)
    screen.fill((0, 0, 0))
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < screen_width - player_width:
        player_x += player_speed
    
    # Bullet firing
    if keys[pygame.K_r]:  # Red bullet
        bullet_color = colors["red"]
    elif keys[pygame.K_g]:  # Green bullet
        bullet_color = colors["green"]
    elif keys[pygame.K_b]:  # Blue bullet
        bullet_color = colors["blue"]
    elif keys[pygame.K_y]:  # Yellow bullet
        bullet_color = colors["yellow"]
    else:
        bullet_color = None

    if bullet_color:
        if len(bullets) < 5:  # Limit the number of bullets
            bullets.append([player_x + player_width // 2 - bullet_width // 2, player_y, bullet_color])

    # Spawn enemies
    if len(enemies) < 5:
        enemy_x = random.randint(0, screen_width - enemy_width)
        enemy_y = random.randint(-100, -40)
        enemy_color = random.choice(enemy_colors)
        enemies.append([enemy_x, enemy_y, enemy_color])

    # Bullet movement
    for bullet in bullets:
        bullet[1] -= bullet_speed
        if bullet[1] < 0:
            bullets.remove(bullet)
    
    # Enemy movement
    for enemy in enemies:
        enemy[1] += enemy_speed
        if enemy[1] > screen_height:
            enemies.remove(enemy)

    # Collision detection
    for bullet in bullets:
        for enemy in enemies:
            if (bullet[0] < enemy[0] + enemy_width and
                bullet[0] + bullet_width > enemy[0] and
                bullet[1] < enemy[1] + enemy_height and
                bullet[1] + bullet_height > enemy[1]):
                if bullet[2] == enemy[2]:  # Check if colors match
                    score += 1
                bullets.remove(bullet)
                enemies.remove(enemy)
                break

    # Draw player
    pygame.draw.rect(screen, (255, 255, 255), (player_x, player_y, player_width, player_height))
    
    # Draw bullets
    for bullet in bullets:
        pygame.draw.rect(screen, bullet[2], (bullet[0], bullet[1], bullet_width, bullet_height))
    
    # Draw enemies
    for enemy in enemies:
        pygame.draw.rect(screen, enemy[2], (enemy[0], enemy[1], enemy_width, enemy_height))
    
    # Display score
    show_score(10, 10)

    # Update screen
    pygame.display.flip()

pygame.quit()
