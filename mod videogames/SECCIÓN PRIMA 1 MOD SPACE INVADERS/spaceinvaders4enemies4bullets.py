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
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0)]  # Red, Green, Blue, Yellow

# Fonts
font = pygame.font.Font('freesansbold.ttf', 32)

# Score
score_value = 0
def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, white)
    screen.blit(score, (x, y))

# Player
player_img = pygame.Surface((64, 64))
player_img.fill(white)
player_x = screen_width // 2 - 32
player_y = screen_height - 70
player_x_change = 0

def player(x, y):
    screen.blit(player_img, (x, y))

# Enemies
enemies = []
for i in range(4):
    enemy_x = random.randint(0, screen_width - 64)
    enemy_y = random.randint(50, 150)
    enemy_color = colors[i]
    enemies.append([enemy_x, enemy_y, 1, 40, enemy_color])

def draw_enemy(x, y, color):
    enemy_img = pygame.Surface((64, 64))
    enemy_img.fill(color)
    screen.blit(enemy_img, (x, y))

# Bullets
bullets = {
    (255, 0, 0): {"img": pygame.Surface((8, 32)), "state": "ready", "x": 0, "y": player_y, "y_change": 10},  # Red bullet
    (0, 255, 0): {"img": pygame.Surface((8, 32)), "state": "ready", "x": 0, "y": player_y, "y_change": 10},  # Green bullet
    (0, 0, 255): {"img": pygame.Surface((8, 32)), "state": "ready", "x": 0, "y": player_y, "y_change": 10},  # Blue bullet
    (255, 255, 0): {"img": pygame.Surface((8, 32)), "state": "ready", "x": 0, "y": player_y, "y_change": 10},  # Yellow bullet
}

for bullet in bullets.values():
    bullet["img"].fill(bullet["img"].get_at((0, 0)))  # Fill with the bullet's color

def fire_bullet(color):
    bullets[color]["state"] = "fire"
    bullets[color]["x"] = player_x + 28  # Center bullet horizontally above the player
    bullets[color]["y"] = player_y

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
                player_x_change = -2
            if event.key == pygame.K_RIGHT:
                player_x_change = 2
            if event.key == pygame.K_a and bullets[(255, 0, 0)]["state"] == "ready":
                fire_bullet((255, 0, 0))  # Fire red bullet
            if event.key == pygame.K_s and bullets[(0, 255, 0)]["state"] == "ready":
                fire_bullet((0, 255, 0))  # Fire green bullet
            if event.key == pygame.K_d and bullets[(0, 0, 255)]["state"] == "ready":
                fire_bullet((0, 0, 255))  # Fire blue bullet
            if event.key == pygame.K_f and bullets[(255, 255, 0)]["state"] == "ready":
                fire_bullet((255, 255, 0))  # Fire yellow bullet

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

    # Move and draw enemies
    for enemy in enemies:
        enemy_x, enemy_y, enemy_x_change, enemy_y_change, enemy_color = enemy
        enemy_x += enemy_x_change

        # Boundary checking for the enemy
        if enemy_x <= 0 or enemy_x >= screen_width - 64:
            enemy_x_change = -enemy_x_change
            enemy_y += enemy_y_change
        enemy[0] = enemy_x
        enemy[2] = enemy_x_change

        # Draw enemy
        draw_enemy(enemy_x, enemy_y, enemy_color)

        # Check for collision with corresponding bullet
        bullet = bullets[enemy_color]
        if bullet["state"] == "fire" and is_collision(enemy_x, enemy_y, bullet["x"], bullet["y"]):
            bullet["y"] = player_y
            bullet["state"] = "ready"
            # Reset enemy position after hit
            enemy[0] = random.randint(0, screen_width - 64)
            enemy[1] = random.randint(50, 150)

    # Bullet movement
    for color, bullet in bullets.items():
        if bullet["state"] == "fire":
            screen.blit(bullet["img"], (bullet["x"], bullet["y"]))
            bullet["y"] -= bullet["y_change"]

        if bullet["y"] <= 0:
            bullet["y"] = player_y
            bullet["state"] = "ready"

    # Draw player
    player(player_x, player_y)

    # Update display
    pygame.display.update()
