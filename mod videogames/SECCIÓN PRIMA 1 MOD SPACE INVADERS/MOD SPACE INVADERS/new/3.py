
import pygame
import random
import math
from pygame import mixer
 
# initializing pygame
pygame.init()
 
# creating screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width,
                                  screen_height))
 
# caption and icon
pygame.display.set_caption("Welcome to Space\
Invaders Game by:- styles")
 
 
# Score
score_val = 0
scoreX = 5
scoreY = 5
font = pygame.font.Font('freesansbold.ttf', 20)
 
# Game Over
game_over_font = pygame.font.Font('freesansbold.ttf', 64)
 
 
def show_score(x, y):
    score = font.render("Points: " + str(score_val),
                        True, (255,255,255))
    screen.blit(score, (x , y ))
 
def game_over():
    game_over_text = game_over_font.render("GAME OVER",
                                           True, (255,255,255))
    screen.blit(game_over_text, (190, 250))
 
# Background Sound
#mixer.music.load('space.wav')
#mixer.music.play(-1)
 
# player
playerImage = pygame.image.load('pixel_ship_yellow.png')
player_X = 370
player_Y = 523
player_Xchange = 0
 
# BlueInvader
BlueInvaderImage = pygame.image.load('pixel_ship_blue_small.png')
BlueInvader_X = random.randint(64, 737)
BlueInvader_Y = random.randint(30, 180)
BlueInvader_Xchange = 1.2
BlueInvader_Ychange = 50

# GreenInvader
GreenInvaderImage = pygame.image.load('pixel_ship_green_small.png')
GreenInvader_X = random.randint(64, 737)
GreenInvader_Y = random.randint(30, 180)
GreenInvader_Xchange = 1.2
GreenInvader_Ychange = 50

# PurpleInvader
PurpleInvaderImage = pygame.image.load('pixel_ship_purple_small.png')
PurpleInvader_X = random.randint(64, 737)
PurpleInvader_Y = random.randint(30, 180)
PurpleInvader_Xchange = 1.2
PurpleInvader_Ychange = 50

# WhiteInvader
WhiteInvaderImage = pygame.image.load('pixel_ship_white_small.png')
WhiteInvader_X = random.randint(64, 737)
WhiteInvader_Y = random.randint(30, 180)
WhiteInvader_Xchange = 1.2
WhiteInvader_Ychange = 50


invaderImage = []
invader_X = []
invader_Y = []
invader_Xchange = []
invader_Ychange = []
no_of_invaders = 2
 

 
for num in range(no_of_invaders):
    invaderImage.append(pygame.image.load('pixel_ship_blue_small.png'))
    invader_X.append(random.randint(64, 737))
    invader_Y.append(random.randint(30, 180))
    invader_Xchange.append(1.2)
    invader_Ychange.append(50)
 
# Bullet
# rest - bullet is not moving
# fire - bullet is moving
bulletImage = pygame.image.load('pixel_laser_blue.png')
bullet_X = 0
bullet_Y = 500
bullet_Xchange = 0
bullet_Ychange = 3
bullet_state = "rest"

greenbulletImage = pygame.image.load('pixel_laser_green.png')
greenbullet_X = 0
greenbullet_Y = 500
greenbullet_Xchange = 0
greenbullet_Ychange = 3
greenbullet_state = "rest"

purplebulletImage = pygame.image.load('pixel_laser_purple.png')
purplebullet_X = 0
purplebullet_Y = 500
purplebullet_Xchange = 0
purplebullet_Ychange = 3
purplebullet_state = "rest"

# Collision Concept
def isCollision(x1, x2, y1, y2):
    distance = math.sqrt((math.pow(x1 - x2,2)) +
                         (math.pow(y1 - y2,2)))
    if distance <= 50:
        return True
    else:
        return False
 
def player(x, y):
    screen.blit(playerImage, (x - 16, y + 10))
 
def invader(x, y, i):
    screen.blit(invaderImage[i], (x, y))
 
def bullet(x, y):
    global bullet_state
    screen.blit(bulletImage, (x, y))
    bullet_state = "fire"
 
def Greenbullet(x, y):
	global greenbullet_state
	screen.blit(greenbulletImage, (x, y))
	greenbullet_state = "fire"

# game loop
running = True
while running:
 
    # RGB
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
 
        # Controlling the player movement
        # from the arrow keys
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_Xchange = -1.7
            if event.key == pygame.K_RIGHT:
                player_Xchange = 1.7
            if event.key == pygame.K_SPACE: 
                if greenbullet_state == "rest":
                    greenbullet_X = player_X
                    Greenbullet(greenbullet_X, greenbullet_Y)
            #if event.key == pygame.K_a:
	#		print("a")
					   
        if event.type == pygame.KEYUP:
            player_Xchange = 0
 
    # adding the change in the player position
    player_X += player_Xchange
    for i in range(no_of_invaders):
        invader_X[i] += invader_Xchange[i]
 
    # bullet movement
    if bullet_Y <= 0:
        bullet_Y = 600
        bullet_state = "rest"
    if bullet_state is "fire":
        bullet(bullet_X, bullet_Y)
        bullet_Y -= bullet_Ychange
 
    if greenbullet_Y <= 0:
        greenbullet_Y = 600
        greenbullet_state = "rest"
    if greenbullet_state is "fire":
        Greenbullet(greenbullet_X, greenbullet_Y)
        greenbullet_Y -= greenbullet_Ychange

 
 
    # movement of the invader
    for i in range(no_of_invaders):
         
        if invader_Y[i] >= 450:
            if abs(player_X-invader_X[i]) < 80:
                for j in range(no_of_invaders):
                    invader_Y[j] = 2000
                    #explosion_sound = mixer.Sound('data/explosion.wav')
                    #explosion_sound.play()
                game_over()
                break
 
        if invader_X[i] >= 735 or invader_X[i] <= 0:
            invader_Xchange[i] *= -1
            invader_Y[i] += invader_Ychange[i]
        # Collision
        collision = isCollision(bullet_X, invader_X[i],
                                bullet_Y, invader_Y[i])
        collision1 = isCollision(greenbullet_X, invader_X[i],
								 greenbullet_Y, invader_Y[i])

        if collision or collision1:
            score_val += 1
            bullet_Y = 600
            greenbullet_Y = 600
            bullet_state = "rest"
            greenbullet_state = "rest"
            invader_X[i] = random.randint(64, 736)
            invader_Y[i] = random.randint(30, 200)
            invader_Xchange[i] *= -1
 
        invader(invader_X[i], invader_Y[i], i)
 
 
    # restricting the spaceship so that
    # it doesn't go out of screen
    if player_X <= 16:
        player_X = 16;
    elif player_X >= 750:
        player_X = 750
 
 
    player(player_X, player_Y)
    show_score(scoreX, scoreY)
    pygame.display.update()

