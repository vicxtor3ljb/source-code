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

# Player 
player_img = pygame.image.load("assets/pixel_ship_orange.png") # Load your player image here
player_x = screen_width // 2 - 32
player_y = screen_height - 70
player_x_change = 0

def player(x, y): 
	screen.blit(player_img, (x, y))

# blue enemy
blue_enemy_img = pygame.image.load('assets/pixel_ship_blue_small.png')
blue_enemy_x = random.randint(0, screen_width - 64)
blue_enemy_y = random.randint(50, 150)
blue_enemy_x_change = 0
blue_enemy_y_change = 0
def blue_enemy(x, y):
	screen.blit(blue_enemy_img, (x, y))
	
# green enemy
green_enemy = []
green_enemy_img = pygame.image.load('assets/pixel_ship_green_small.png')
green_enemy_x = random.randint(0, screen_width - 64)
green_enemy_y = random.randint(50, 150)
green_enemy_x_change = 0
green_enemy_y_change = 0
green_enemy.append([green_enemy_x, green_enemy_y, 1, 40])

def green_enemy(x, y):
	screen.blit(green_enemy_img, (x, y))
	
# purple enemy
purple_enemy_img = pygame.image.load('assets/pixel_ship_purple_small.png')
purple_enemy_x = random.randint(0, screen_width - 64)
purple_enemy_y = random.randint(50, 150)
purple_enemy_x_change = 0
purple_enemy_y_change = 0

def purple_enemy(x, y):
	screen.blit(purple_enemy_img, (x, y))
	
# white enemy
white_enemy_img = pygame.image.load('assets/pixel_ship_white_small.png')
white_enemy_x = random.randint(0, screen_width - 64)
white_enemy_y = random.randint(50, 150)
white_enemy_x_change = 0
white_enemy_y_change = 0

def white_enemy(x, y):
	screen.blit(white_enemy_img, (x, y))
	
# Game Loop
running = True
while running: 
	# Background color
	screen.fill(black)
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
			
		# Player movement: 
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT: 
				player_x_change = -0.5
			if event.key == pygame.K_RIGHT:
				player_x_change = 0.5
		
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT: 
				player_x_change = 0
	
	# Update player position
	player_x += player_x_change
	
	# Boundary checking for the player
	if player_x <= 0: 
		player_x = 0
	elif player_x >= screen_width - 90: 
		player_x = screen_width - 90
	
	# Draw player
	player(player_x, player_y)
	
	blue_enemy_x += blue_enemy_x_change
	green_enemy_x += green_enemy_x_change
	purple_enemy_x += purple_enemy_x_change
	white_enemy_x += white_enemy_x_change
	
	# Boundary checking for the enemy
	if blue_enemy_x <= 0 or blue_enemy_x >= screen_width - 50: 
		blue_enemy_x_change = -blue_enemy_x
		blue_enemy_y += blue_enemy_y_change
	
	if green_enemy_x <= 0 or green_enemy_x >= screen_width - 50: 
		green_enemy_x_change = -green_enemy_x
		green_enemy_y += green_enemy_y_change
	
	if purple_enemy_x <= 0 or purple_enemy_x >= screen_width - 50: 
		purple_enemy_x_change = -purple_enemy_x
		purple_enemy_y += purple_enemy_y_change
	
	if white_enemy_x <= 0 or white_enemy_x >= screen_width - 50: 
		white_enemy_x_change = -white_enemy_x
		white_enemy_y += white_enemy_y_change
	
	# Draw enemy
	blue_enemy(blue_enemy_x, blue_enemy_y)
	green_enemy(green_enemy_x, green_enemy_y)
	purple_enemy(purple_enemy_x, purple_enemy_y)
	white_enemy(white_enemy_x, white_enemy_y)
	
	# Update display
	pygame.display.update()
