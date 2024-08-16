import pygame
import random

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 600, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Bullet class
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__()
        self.image = pygame.Surface((5, 20))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.color = color

    def update(self):
        self.rect.y -= 5
        if self.rect.bottom < 0:
            self.kill()

# Enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.color = color

    def update(self):
        self.rect.y += 1
        if self.rect.top > HEIGHT:
            self.rect.y = random.randint(-150, -40)
            self.rect.x = random.randint(0, WIDTH - 40)

# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT - 50)
        self.speed_x = 0

    def update(self):
        self.rect.x += self.speed_x
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH

    def shoot(self, color):
        bullet = Bullet(self.rect.centerx, self.rect.top, color)
        all_sprites.add(bullet)
        bullets.add(bullet)

# Game variables
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
bullets = pygame.sprite.Group()

player = Player()
all_sprites.add(player)

enemy_colors = [RED, GREEN, BLUE, YELLOW]
bullet_colors = [RED, GREEN, BLUE, YELLOW]

for i in range(10):
    x = random.randint(0, WIDTH - 40)
    y = random.randint(-150, -40)
    color = random.choice(enemy_colors)
    enemy = Enemy(x, y, color)
    all_sprites.add(enemy)
    enemies.add(enemy)

score = 0
font = pygame.font.Font(None, 36)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.speed_x = -5
            elif event.key == pygame.K_RIGHT:
                player.speed_x = 5
			elif event.key == pygame.K_a:
                player.shoot(RED)
			elif event.key == pygame.K_s:
				player.shoot(GREEN)
			elif event.key == pygame.K_d: 
				player.shoot(BLUE)
			elif event.key == pygame.K_f: 
				player.shoot(YELLOW)

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player.speed_x = 0

    # Update
    all_sprites.update()

    # Check for collisions between bullets and enemies
    hits = pygame.sprite.groupcollide(enemies, bullets, True, True)
    for hit in hits:
        if hit.color == hits[hit][0].color:
            score += 10
        else:
            score -= 5
        new_enemy = Enemy(random.randint(0, WIDTH - 40), random.randint(-150, -40), random.choice(enemy_colors))
        all_sprites.add(new_enemy)
        enemies.add(new_enemy)

    # Draw / render
    screen.fill(BLACK)
    all_sprites.draw(screen)

    # Display score
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    # Flip the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)

pygame.quit()
