import pygame
import random
import math

pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Space Invaders")

clock = pygame.time.Clock()


white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)

font = pygame.font.Font(None, 36)

player_img = pygame.image.load("player.png")
playerX = 370
playerY = 480
playerX_change = 0

enemy_imgs = [pygame.image.load("enemy1.png"),
               pygame.image.load("enemy2.png"),
               pygame.image.load("enemy3.png"),
               pygame.image.load("enemy4.png")]
enemyX = []
enemyY = []
enemyX_change = []
num_enemies = 4
for i in range(num_enemies):
    enemyX.append(random.randint(0, screen_width))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(0.3)

bullet_img = pygame.image.load("bullet.png")
bulletX = 0
bulletY = 480
bulletY_change = 0.5
bullet_state = "ready"

score = 0

def player(x, y):
    screen.blit(player_img, (x, y))

def enemy(x, y, i):
    screen.blit(enemy_imgs[i], (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_img, (x + 16, y + 10))

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((enemyX - bulletX) ** 2 + (enemyY - bulletY) ** 2)
    if distance < 27:
        return True
    else:
        return False
        
running = True
while running:
    screen.fill(black)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.5
            elif event.key == pygame.K_RIGHT:
                playerX_change = 0.5
            elif event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    playerX += playerX_change
    if playerX < 0:
        playerX = 0
    elif playerX > screen_width - 64:
        playerX = screen_width - 64

    for i in range(num_enemies):
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 0.3
            enemyY[i] += 40
        elif enemyX[i] >= screen_width - 64:
            enemyX_change[i] = -0.3
            enemyY[i] += 40

        if enemyY[i] >= 440:
            for j in range(num_enemies):
                enemyY[j] = 2000
            game_over_text = font.render("GAME OVER", True, white)
            screen.blit(game_over_text, (screen_width // 2 - 100, screen_height // 2 - 50))
            pygame.display.update()
            break

        if bulletY <= 0:
            bulletY = 480
            bullet_state = "ready"

        if bullet_state == "fire":
            fire_bullet(bulletX, bulletY)
            bulletY -= bulletY_change

        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            bulletY = 480
            bullet_state = "ready"
            score += 1
            enemyX[i] = random.randint(0, screen_width)
            enemyY[i] = random.randint(50, 150)

    player(playerX, playerY)
    for i in range(num_enemies):
        enemy(enemyX[i], enemyY[i], i)
    fire_bullet(bulletX, bulletY)

    score_text = font.render("Score: " + str(score), True, white)
    screen.blit(score_text, (10, 10))

    pygame.display.update()
