import pygame
from pygame.locals import *
import sys

pygame.init()

# Constants for screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors (R, G, B)
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
purple = pygame.Color(255, 0, 255)


# Create the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Space Invaders')

# Set the background color
bg_color = (0, 0, 0) # Black

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("pixel_ship_yellow.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 5

    def move_left(self):
        self.rect.x -= self.speed
        if self.rect.x < 0:
            self.rect.x = 0

    def move_right(self):
        self.rect.x += self.speed
        if self.rect.x > SCREEN_WIDTH - self.rect.width:
            self.rect.x = SCREEN_WIDTH - self.rect.width

class BlueEnemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("pixel_ship_blue_small.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 2

    def update(self):
        self.rect.x += self.speed
        if self.rect.x < 0 or self.rect.x > SCREEN_WIDTH - self.rect.width:
            self.speed = -self.speed
            self.rect.y += self.rect.height

class GreenEnemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("pixel_ship_green_small.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 2

    def update(self):
        self.rect.x += self.speed
        if self.rect.x < 0 or self.rect.x > SCREEN_WIDTH - self.rect.width:
            self.speed = -self.speed
            self.rect.y += self.rect.height

class PurpleEnemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("pixel_ship_purple_small.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 2

    def update(self):
        self.rect.x += self.speed
        if self.rect.x < 0 or self.rect.x > SCREEN_WIDTH - self.rect.width:
            self.speed = -self.speed
            self.rect.y += self.rect.height

class WhiteEnemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("pixel_ship_white_small.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 2

    def update(self):
        self.rect.x += self.speed
        if self.rect.x < 0 or self.rect.x > SCREEN_WIDTH - self.rect.width:
            self.speed = -self.speed
            self.rect.y += self.rect.height

class BlueBullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((4, 10))
        self.image.fill(blue)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 10

    def update(self):
        self.rect.y -= self.speed

class GreenBullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((4, 10))
        self.image.fill(green)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 10

    def update(self):
        self.rect.y -= self.speed

class PurpleBullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((4, 10))
        self.image.fill(purple)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 10

    def update(self):
        self.rect.y -= self.speed

class WhiteBullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((4, 10))
        self.image.fill(white)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 10

    def update(self):
        self.rect.y -= self.speed

player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 100)

enemies = pygame.sprite.Group()
for i in range(5):
    for j in range(5):
        enemy = BlueEnemy(50 + i * 100, 50 + j * 70)
        enemies.add(enemy)

bullets = pygame.sprite.Group()

clock = pygame.time.Clock()

while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_a:
                bullet = BlueBullet(player.rect.centerx, player.rect.y)
                bullets.add(bullet)
	    #if event.key == K_s:
	    #	bullet = GreenBullet(player.rect.centerx, player.rect.y)
	    #bullets.add(bullet)
            #if event.key == K_d:
			#	bullet = PurpleBullet(player.rect.centerx, player.rect.y)
            #    bullets.add(bullet)
			#if event.key == K_f:
			#	bullet = WhiteBullet(player.rect.centerx, player.rect.y)
            #   bullets.add(bullet)
         
    keys = pygame.key.get_pressed()
    if keys[K_LEFT]:
        player.move_left()
    if keys[K_RIGHT]:
        player.move_right()

    # Update game objects
    enemies.update()
    bullets.update()

    # Check for collisions
    pygame.sprite.groupcollide(bullets, enemies, True, True)

    # Draw game objects
    screen.fill(bg_color)
    screen.blit(player.image, player.rect)
    enemies.draw(screen)
    bullets.draw(screen)

    pygame.display.flip()
    clock.tick(60)
