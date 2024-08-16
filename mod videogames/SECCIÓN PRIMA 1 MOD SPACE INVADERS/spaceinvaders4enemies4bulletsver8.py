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
red = (255, 0, 0)


# Ship class
class Ship:
    def __init__(self):
        self.color = random.choice(list(colors.values()))
        self.rect = pygame.Rect(screen_width // 2, screen_height - 50, 50, 30)
        self.speed = 5

    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect)

    def move(self, dx):
        self.rect.x += dx * self.speed
        self.rect.x = max(0, min(screen_width - self.rect.width, self.rect.x))

# Bullet class
class Bullet:
    def __init__(self, x, y, color):
        self.rect = pygame.Rect(x, y, 5, 10)
        self.color = color
        self.speed = -7

    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect)

    def move(self):
        self.rect.y += self.speed

# Enemy class
class Enemy:
    def __init__(self, x, y, color):
        self.rect = pygame.Rect(x, y, 50, 30)
        self.color = color

    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect)

# Main game loop
def main():
    clock = pygame.time.Clock()
    ship = Ship()
    bullets = []
    enemies = [Enemy(random.randint(0, screen_width - 50), random.randint(0, 200), color) for color in colors.values()]
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    bullet_color = red
                    bullets.append(Bullet(ship.rect.centerx, ship.rect.top, red))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            ship.move(-1)
        if keys[pygame.K_RIGHT]:
            ship.move(1)

        screen.fill((0, 0, 0))

        for bullet in bullets[:]:
            bullet.move()
            bullet.draw()
            if bullet.rect.bottom < 0:
                bullets.remove(bullet)
            elif bullet.color == ship.color and bullet.rect.colliderect(ship.rect):
                running = False

        for enemy in enemies:
            enemy.draw()

        ship.draw()
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
