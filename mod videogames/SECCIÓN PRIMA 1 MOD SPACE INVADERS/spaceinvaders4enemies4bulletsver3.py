
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

color_names = list(colors.keys())

# Player
player_width = 50
player_height = 10
player_x = (screen_width - player_width) // 2
player_y = screen_height - player_height - 10
player_speed = 5

# Bullets
bullet_width = 5
bullet_height = 10
bullet_speed = 7
bullets = []

# Enemies
enemy_width = 50
enemy_height = 30
enemy_speed = 2
enemies = []

# Score
score = 0
font = pygame.font.Font(None, 36)

# Game clock
clock = pygame.time.Clock()

def create_enemy():
    x = random.randint(0, screen_width - enemy_width)
    y = random.randint(-100, -40)
    color = random.choice(color_names)
    return {"x": x, "y": y, "color": color}

def draw_player():
    pygame.draw.rect(screen, colors["green"], (player_x, player_y, player_width, player_height))

def draw_bullet(bullet):
    pygame.draw.rect(screen, colors[bullet["color"]], (bullet["x"], bullet["y"], bullet_width, bullet_height))

def draw_enemy(enemy):
    pygame.draw.rect(screen, colors[enemy["color"]], (enemy["x"], enemy["y"], enemy_width, enemy_height))

def check_collision(bullet, enemy):
    return (bullet["x"] < enemy["x"] + enemy_width and
            bullet["x"] + bullet_width > enemy["x"] and
            bullet["y"] < enemy["y"] + enemy_height and
            bullet["y"] + bullet_height > enemy["y"])

def show_score():
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

# Main game loop
running = True
while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < screen_width - player_width:
        player_x += player_speed
    if keys[pygame.K_SPACE]:
        if len(bullets) < 5:  # Limit the number of bullets on screen
            bullet_color = random.choice(color_names)
            bullets.append({"x": player_x + player_width // 2, "y": player_y, "color": bullet_color})

    # Update bullets
    for bullet in bullets[:]:
        bullet["y"] -= bullet_speed
        if bullet["y"] < 0:
            bullets.remove(bullet)

    # Update enemies
    if random.randint(1, 20) == 1:
        enemies.append(create_enemy())

    for enemy in enemies[:]:
        enemy["y"] += enemy_speed
        if enemy["y"] > screen_height:
            enemies.remove(enemy)

    # Check for collisions
    for bullet in bullets[:]:
        for enemy in enemies[:]:
            if check_collision(bullet, enemy):
                if bullet["color"] == enemy["color"]:
                    score += 10
                bullets.remove(bullet)
                enemies.remove(enemy)
                break

    # Draw everything
    draw_player()
    for bullet in bullets:
        draw_bullet(bullet)
    for enemy in enemies:
        draw_enemy(enemy)
    show_score()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
