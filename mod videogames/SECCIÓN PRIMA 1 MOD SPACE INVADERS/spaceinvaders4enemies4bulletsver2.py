import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Title and Icon
pygame.display.set_caption("Space Invaders")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)

# Player
player_img = pygame.Surface((64, 64))
player_img.fill(white)
player_x = screen_width // 2 - 32
player_y = screen_height - 70
player_x_change = 0

def player(x, y):
    screen.blit(player_img, (x, y))

# Enemies with different colors
enemy_colors = [red, green, blue, yellow]
enemies = []
for i in range(4):  # Creating only four enemies with different colors
    enemy_img = pygame.Surface((64, 64))
    enemy_img.fill(enemy_colors[i])
    enemy_x = random.randint(0, screen_width - 64)
    enemy_y = random.randint(50, 150)
    enemies.append([enemy_img, enemy_x, enemy_y, 1, 40, enemy_colors[i]])

def enemators(enemy_img, x, y):
    screen.blit(enemy_img, (x, y))

# Bullets, one for each color
bullet_colors = [red, green, blue, yellow]
bullets = []
for color in bullet_colors:
    bullet_img = pygame.Surface((10, 40))
    bullet_img.fill(color)
    bullets.append({"img": bullet_img, "x": 0, "y": player_y, "y_change": 10, "state": "ready", "color": color})

def fire_bullet(bullet):
    bullet["state"] = "fire"
    screen.blit(bullet["img"], (bullet["x"] + 27, bullet["y"] + 10))

# Collision Detection
def is_collision(enemy_x, enemy_y, bullet_x, bullet_y):
    distance = ((enemy_x - bullet_x) ** 2 + (enemy_y - bullet_y) ** 2) ** 0.5
    return distance < 27

# Game Loop
running = True
while running:
    # Background color
    screen.fill(black)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Player movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -1
            if event.key == pygame.K_RIGHT:
                player_x_change = 1
            if event.key == pygame.K_1 and bullets[0]["state"] == "ready":
                bullets[0]["x"] = player_x
                fire_bullet(bullets[0])
            if event.key == pygame.K_2 and bullets[1]["state"] == "ready":
                bullets[1]["x"] = player_x
                fire_bullet(bullets[1])
            if event.key == pygame.K_3 and bullets[2]["state"] == "ready":
                bullets[2]["x"] = player_x
                fire_bullet(bullets[2])
            if event.key == pygame.K_4 and bullets[3]["state"] == "ready":
                bullets[3]["x"] = player_x
                fire_bullet(bullets[3])

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_x_change = 0

    # Update player position
    player_x += player_x_change

    # Boundary checking for the player
    if player_x <= 0:
        player_x = 0
    elif player_x >= screen_width - 64:
        player_x = screen_width - 64

    # Bullet movement
    for bullet in bullets:
        if bullet["state"] == "fire":
            fire_bullet(bullet)
            bullet["y"] -= bullet["y_change"]
        
        if bullet["y"] <= 0:
            bullet["y"] = player_y
            bullet["state"] = "ready"

    # Collision
    for enemy in enemies:
        enemy_img, enemy_x, enemy_y, enemy_x_change, enemy_y_change, enemy_color = enemy
        for bullet in bullets:
            if bullet["state"] == "fire" and bullet["color"] == enemy_color:
                if is_collision(enemy_x, enemy_y, bullet["x"], bullet["y"]):
                    bullet["y"] = player_y
                    bullet["state"] = "ready"
                    # Reset enemy position after hit
                    enemy[1] = random.randint(0, screen_width - 64)
                    enemy[2] = random.randint(50, 150)

        # Move the enemy
        enemy_x += enemy_x_change

        # Boundary checking for the enemy
        if enemy_x <= 0 or enemy_x >= screen_width - 64:
            enemy[3] = -enemy[3]
            enemy[2] += enemy_y_change

        # Draw enemy
        enemators(enemy_img, enemy_x, enemy_y)

    # Draw player
    player(player_x, player_y)

    # Update display
    pygame.display.update()

