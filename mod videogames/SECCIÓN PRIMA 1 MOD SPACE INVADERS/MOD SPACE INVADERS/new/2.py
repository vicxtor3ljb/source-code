import pygame
import random
import math
from pygame import mixer

# initializing pygame
pygame.init()

# creating screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# caption and icon
pygame.display.set_caption("Welcome to Space Invaders Game by: -styles")

# Score
score_val = 0
scoreX = 5 
scoreY = 5
font = pygame.font.Font('freesansbold.ttf', 20)

# Game Over
game_over_font = pygame.font.Font('freesansbold.ttf', 64)

def show_score(x, y):
	score = font.render("Points: " + str(score_val), 
						True, (255, 255, 255))
	screen.blit(score, (x, y ))
	
def game_over():
	game_over_text = game_over_font.render("GAME OVER", True, (255,255,255))
	screen.blit(game_over_text, (190, 250))

# Background Sound
# mixer.music.load('space.wav')
# mixer music.play(-1)

# Player
playerImage = pygame.image.load('pixel_ship_yellow.png')
player_X = 370
player_Y = 500
player_Xchange = 0

# Blueship
BlueshipImage = pygame.image.load('pixel_ship_blue_small.png')
Blueship_X = random.randint(64, 737)
Blueship_Y = random.randint(30, 180)
Blueship_Xchange = 1.2
Blueship_Ychange = 50

# Greenship
GreenshipImage = pygame.image.load('pixel_ship_green_small.png')
Greenship_X = random.randint(64, 737)
Greenship_Y = random.randint(30, 180)
Greenship_Xchange = 1.2
Greenship_Ychange = 50

# Purpleship
PurpleshipImage = pygame.image.load('pixel_ship_purple_small.png')
Purpleship_X = random.randint(64, 737)
Purpleship_Y = random.randint(30, 180)
Purpleship_Xchange = 1.2
Purpleship_Ychange = 50

# Whiteship
WhiteshipImage = pygame.image.load('pixel_ship_white_small.png')
Whiteship_X = random.randint(64, 737)
Whiteship_Y = random.randint(30, 180)
Whiteship_Xchange = 1.2
Whiteship_Ychange = 50

# Bluebullet
# rest - bullet is not moving
# fire - bullet is moving
BluebulletImage = pygame.image.load('pixel_laser_blue.png')
Bluebullet_X = 0
Bluebullet_Y = 500
Bluebullet_Xchange = 0 
Bluebullet_Ychange = 3
Bluebullet_state = "rest"

# Greenbullet
# rest - bullet is not moving
# fire - bullet is moving
GreenbulletImage = pygame.image.load('pixel_laser_green.png')
Greenbullet_X = 0
Greenbullet_Y = 500
Greenbullet_Xchange = 0 
Greenbullet_Ychange = 3
Greenbullet_state = "rest"

# Purplebullet
# rest - bullet is not moving
# fire - bullet is moving
PurplebulletImage = pygame.image.load('pixel_laser_purple.png')
Purplebullet_X = 0
Purplebullet_Y = 500
Purplebullet_Xchange = 0 
Purplebullet_Ychange = 3
Purplebullet_state = "rest"

# Whitebullet
# rest - bullet is not moving
# fire - bullet is moving
WhitebulletImage = pygame.image.load('pixel_laser_white.png')
Whitebullet_X = 0
Whitebullet_Y = 500
Whitebullet_Xchange = 0 
Whitebullet_Ychange = 3
Whitebullet_state = "rest"

# Collision Concept
def isCollision(x1, x2, y1, y2):
	distance = math.sqrt((math.pow(x1 - x2,2)) + (math.pow(y1 - y2,2)))
	
	if distance <= 50:
		return True
	else: 
		return False

def player(x, y):
	screen.blit(playerImage, (x - 16, y + 10))
	
def blueinvader(x, y):
	screen.blit(BlueshipImage, (x, y))	
	
def greeninvader(x, y):
	screen.blit(GreenshipImage, (x, y))

def purpleinvader(x, y):
	screen.blit(PurpleshipImage, (x, y))

def whiteinvader(x, y):
	screen.blit(WhiteshipImage, (x, y))
	
def bluebullet(x, y): 
	global bullet_state
	screen.blit(BluebulletImage, (x, y))
	bullet_state = "fire"

def greenbullet(x, y): 
	global bullet_state
	screen.blit(GreenbulletImage, (x, y))
	bullet_state = "fire"
	
def Purplebullet(x, y): 
	global bullet_state
	screen.blit(PurplebulletImage, (x, y))
	bullet_state = "fire"
	
def Whitebullet(x, y): 
	global bullet_state
	screen.blit(WhitebulletImage, (x, y))
	bullet_state = "fire"	

# game loop
running = True 
while running: 
	# RGB
	screen.fill((0,0,0))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
			
	# Controlling the player movement
	# from the arrow queys
	if event.type == pygame.KEYDOWN:
		if event.key == pygame.K_LEFT: 
			player_Xchange = -1.7
		if event.key == pygame.K_RIGHT:
			player_Xchange = 1.7
		if event.key == pygame.K_UP:
			player_Ychange = -1.7
		if event.key == pygame.K_DOWN: 
			player_Ychange = 1.7
		if event.key == pygame.K_a: 
			if Bluebullet_state == "rest":
				Bluebullet_X = player_X
				bluebullet(Bluebullet_X, Bluebullet_Y)
		if event.key == pygame.K_s:		
			if Greenbullet_state == "rest":
				Greenbullet_X = player_X
				greenbullet(Greenbullet_X, Greenbullet_Y)
		if event.key == pygame.K_d:
			if Purplebullet_state == "rest":
				Purplebullet_X = player_X
				purplebullet(Purplebullet_X, Purplebullet_Y)
		if event.key == pygame.K_f:
			if Whitebullet_state == "rest": 
				Whitebullet_X = player_X
				whitebullet(Whitebullet_X, Whitebullet_Y)

	if event.type == pygame.KEYUP: 	
		player_Xchange = 0
	
	#adding the change in the player position
	player_X += player_Xchange
	#for i in range(no_of_invaders):
	#	invader_X[i] += invader_Xchange[i]
	
	# bullets movement
	if Bluebullet_Y <= 0: 
		Bluebullet_Y = 600
		Bluebullet_state = "rest"
	if Bluebullet_state == "fire":
		Bluebullet(Bluebullet_X, Bluebullet_Y)
		Bluebullet_Y -= Bluebullet_Ychange
	
	if Greenbullet_Y <= 0: 
		Greenbullet_Y = 600
		Greenbullet_state = "rest"
	if Greenbullet_state == "fire":
		Greenbullet(Greenbullet_X, Greenbullet_Y)
		Greenbullet_Y -= Greenbullet_Ychange

	if Purplebullet_Y <= 0: 
		Purplebullet_Y = 600
		Purplebullet_state = "rest"
	if Purplebullet_state == "fire":
		Purplebullet(Purplebullet_X, Purplebullet_Y)
		Purplebullet_Y -= Purplebullet_Ychange

	if Whitebullet_Y <= 0: 
		Whitebullet_Y = 600
		Whitebullet_state = "rest"
	if Whitebullet_state == "fire":
		Whitebullet(Whitebullet_X, Whitebullet_Y)
		Whitebullet_Y -= Whitebullet_Ychange
	
	# movement of the invaders
	
	# restricting the spaceship so that
	# it doesn't go out of the screen
	if player_X <= 16:
		player_X = 16;
	elif player_X >= 750:
		player_X = 750
	
	player(player_X, player_Y)
	show_score(scoreX, scoreY)
	pygame.display.update()

