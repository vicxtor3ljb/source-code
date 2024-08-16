import math
import random
import pygame
from pygame import mixer

# initialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 500))

# Background
background = pygame.image.load('background.png')

# Sound
mixer.music.load("spaceinvaders.wav")
mixer.music.play(-1)

# Caption and Icon
pygame.display.set_caption("Space Invaders")
#icon = pygame.image.load('ufo.png')
#pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('pixel_ship_yellow.png')
playerX = 370
playerY = 380
playerX_change = 0

# Enemy 1
enemy1Img = pygame.image.load('pixel_ship_blue_small.png')
enemy1X = random.randint(0, 736)
enemy1Y = random.randint(0, 150)
enemy1X_change = 4
enemy1Y_change = 40

# Enemy 2
enemy2Img = pygame.image.load('pixel_ship_green_small.png')
enemy2X = random.randint(0, 736)
enemy2Y = random.randint(50, 150)
enemy2X_change = 4
enemy2Y_change = 40

# Enemy 3
enemy3Img = pygame.image.load('pixel_ship_purple_small.png')
enemy3X = random.randint(0, 736)
enemy3Y = random.randint(50, 150)
enemy3X_change = 4
enemy3Y_change = 40

# Enemy 4
enemy4Img = pygame.image.load('pixel_ship_white_small.png')
enemy4X = random.randint(0, 736)
enemy4Y = random.randint(50, 150)
enemy4X_change = 4
enemy4Y_change = 40

# Bullets
# Ready- You can't see the bullet on the screen
# Fire - The bullet is currently moving

# Bullet 1
bullet1Img = pygame.image.load('pixel_laser_blue.png')
bullet1X = 0
bullet1Y = 380
bullet1X_change = 0
bullet1Y_change = 10
bullet1_state = "ready"

# Bullet 2
bullet2Img = pygame.image.load('pixel_laser_green.png')
bullet2X = 0
bullet2Y = 380
bullet2X_change = 0
bullet2Y_change = 10
bullet2_state = "ready"

# Bullet 3
bullet3Img = pygame.image.load('pixel_laser_purple.png')
bullet3X = 0
bullet3Y = 380
bullet3X_change = 0
bullet3Y_change = 10
bullet3_state = "ready"

# Bullet 4
bullet4Img = pygame.image.load('pixel_laser_white.png')
bullet4X = 0
bullet4Y = 380
bullet4X_change = 0
bullet4Y_change = 10
bullet4_state = "ready"

# Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf',32)
textX = 10
textY = 10

# Game Over
Game_over_font = pygame.font.Font('freesansbold.ttf',64)

def show_score(x,y):
	score = font.render("Score: "+ str(score_value), True, (255,255,255))
	screen.blit(score, (x,y))

def game_over_text():
	game_over_text=Game_over_font.render("GAME OVER", True, (255,255,255))
	screen.blit(game_over_text,(200,250))

def player(x,y):
	screen.blit(playerImg, (x,y))

def Enemy1(x,y):
	screen.blit(enemy1Img, (x,y))

def Enemy2(x,y):
	screen.blit(enemy2Img, (x,y))

def Enemy3(x,y):
	screen.blit(enemy3Img, (x,y))

def Enemy4(x,y):
	screen.blit(enemy4Img, (x,y))
	
def fire_bullet1(x,y):
	global bullet1_state
	bullet1_state= "fire"
	screen.blit(bullet2Img, (x+16,y+10))

def fire_bullet2(x,y):
	global bullet2_state
	bullet2_state= "fire"
	screen.blit(bullet2Img, (x+16,y+10))

def fire_bullet3(x,y):
	global bullet3_state
	bullet3_state = "fire"
	screen.blit(bullet3Img, (x+16,y+10))
	
def fire_bullet4(x,y):
	global bullet4_state
	bullet4_state = "fire"
	screen.blit(bullet4Img, (x+16,y+10))

def isCollision1(enemy1X,enemy1Y,bullet1X,bullet1Y):
	distance = math.sqrt(math.pow(enemy1X-bullet1X,2) + (math.pow(enemy1Y-bullet1Y,2)))
	if distance < 27:
		return True
	else: 
		return False
		
def isCollision2(enemy2X,enemy2Y,bullet2X,bullet2Y):
	distance = math.sqrt(math.pow(enemy2X-bullet2X,2) + (math.pow(enemy2Y-bullet2Y,2)))
	if distance < 27:
		return True
	else: 
		return False
		
def isCollision3(enemy3X,enemy3Y,bullet3X,bullet3Y):
	distance = math.sqrt(math.pow(enemy3X-bullet3X,2) + (math.pow(enemy3Y-bullet3Y,2)))
	if distance < 27:
		return True
	else: 
		return False
		
def isCollision4(enemy4X,enemy4Y,bullet4X,bullet4Y):
	distance = math.sqrt(math.pow(enemy4X-bullet4X,2) + (math.pow(enemy4Y-bullet4Y,2)))
	if distance < 27:
		return True
	else: 
		return False

# Game Loop
running = True
while running: 
	# RGB = Red, Green, Blue
	screen.fill((0,0,0))

	# Background Image
	screen.blit(background, (0,0))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	
	# if keystroke is pressed check whether it's right or left
	if event.type == pygame.KEYDOWN: 
		if event.key == pygame.K_LEFT: 
			playerX_change = -5
		if event.key == pygame.K_RIGHT: 
			playerX_change = 5
		if event.key == pygame.K_a:
			if bullet1_state == "ready":
				bullet1X = playerX
				fire_bullet1(bullet1X,bullet1Y)
		if event.key == pygame.K_s:
			if bullet2_state == "ready":
				bullet2X = playerX
				fire_bullet2(bullet2X,bullet2Y)
		if event.key == pygame.K_d:
			if bullet3_state == "ready":
				bullet3Y = playerX
				fire_bullet3(bullet3X,bullet3Y)
		if event.key == pygame.K_f:
			if bullet4_state == "ready":
				bullet4Y = playerX
				fire_bullet4(bullet4X,bullet4Y)
	
	if event.type == pygame.KEYUP:
		if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
			playerX_change = 0
			
	# 5 = 5 + -0.1 -> 5 = 5 - 0.1
	# 5 = 5 + 0.1
	playerX += playerX_change
	if playerX <= 0:
		playerX = 0
	elif playerX >= 736: 
		playerX = 736
		
	# Enemy movement
	if enemy1Y > 349: 
		enemy1Y = 2000
		game_over_text()
		break
	if enemy2Y > 349:
		enemy2Y = 2000
		game_over_text()
		break
	if enemy3Y > 349:
		enemy3Y = 2000
		game_over_text()
		break
	if enemy4Y > 349:
		enemy4Y = 2000
		game_over_text()
		break
	
	enemy1X += enemy1X_change
	if enemy1X <= 0:
		enemy1X_change = 4
		enemy1Y += enemy1Y_change
	elif enemy1X >= 736:
		enemy1X_change = -4
		enemy1Y += enemy1Y_change
	
	enemy2X += enemy2X_change
	if enemy2X <= 0:
		enemy2X_change = 4
		enemy2Y += enemy2Y_change
	elif enemy2X >= 736:
		enemy2X_change = -4
		enemy2Y += enemy2Y_change

	enemy3X += enemy3X_change
	if enemy3X <= 0:
		enemy3X_change = 4
		enemy3Y += enemy3Y_change
	elif enemy3X >= 736:
		enemy3X_change = -4
		enemy3Y += enemy3Y_change
	
	enemy4X += enemy4X_change
	if enemy4X <= 0:
		enemy4X_change = 4
		enemy4Y += enemy4Y_change
	elif enemy4X >= 736:
		enemy4X_change = -4
		enemy4Y += enemy4Y_change
	
	# Collision
	collision1 = isCollision1(enemy1X, enemy1Y, bullet1X, bullet1Y)
	if collision1: 
		bullet1Y = 380
		bullet1_state = "ready"
		score_value += 1
		enemy1X = random.randint(0,736)
		enemy1Y = random.randint(50,150)
		Enemy1(enemy1X,enemy1Y)
	
	collision2 = isCollision2(enemy2X, enemy2Y, bullet2X, bullet2Y)
	if collision2: 
		bullet2Y = 380
		bullet2_state = "ready"
		score_value += 1
		enemy2X = random.randint(0,736)
		enemy2Y = random.randint(50,150)
		Enemy2(enemy2X,enemy2Y)

	collision3 = isCollision3(enemy3X, enemy3Y, bullet3X, bullet3Y)
	if collision3: 
		bullet3Y = 380
		bullet3_state = "ready"
		score_value += 1
		enemy3X = random.randint(0,736)
		enemy3Y = random.randint(50,150)
		Enemy3(enemy3X,enemy3Y)
	
	collision4 = isCollision4(enemy4X, enemy4Y, bullet4X, bullet4Y)
	if collision4: 
		bullet4Y = 380
		bullet4_state = "ready"
		score_value += 1
		enemy4X = random.randint(0,736)
		enemy4Y = random.randint(50,150)
		Enemy4(enemy3X,enemy3Y)
	
	# Bullet movement
	if bullet1Y <= 0:
		bullet1Y = 380
		bullet1_state = "ready"
	if bullet1_state == "fire":
		fire_bullet1(bullet1X, bullet1Y)
		bullet1Y -= bullet1Y_change
	
	if bullet2Y <= 0:
		bullet2Y = 380
		bullet2_state = "ready"
	if bullet2_state == "fire":
		fire_bullet2(bullet2X, bullet2Y)
		bullet2Y -= bullet2Y_change
	
	if bullet3Y <= 0:
		bullet3Y = 380
		bullet3_state = "ready"
	if bullet3_state == "fire":
		fire_bullet3(bullet3X, bullet3Y)
		bullet3Y -= bullet3Y_change
	
	if bullet4Y <= 0:
		bullet4Y = 380
		bullet4_state = "ready"
	if bullet4_state == "fire":
		fire_bullet4(bullet4X, bullet4Y)
		bullet4Y -= bullet4Y_change
	
player(playerX,playerY)
	#Enemy1(enemy1X,enemy1Y)
	#Enemy2(enemy2X,enemy2Y)
	#Enemy3(enemy3X,enemy3Y)
	#Enemy4(enemy4X,enemy4Y)
show_score(textX, textY)

pygame.display.update()
	

		
