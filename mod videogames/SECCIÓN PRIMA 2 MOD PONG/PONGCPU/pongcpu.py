# https://medium.com/geekculture/making-pong-with-pygame-19a632b882d

import pygame
import random 
import pygame_pause
import sys, os
from pygame.locals import *

# Environment
mainClock = pygame.time.Clock()

pygame.init()
pygame.font.init()

#setting font settings
font = pygame.font.SysFont(None, 30)

# game_on
game_on = True

# Initialization of the Game
pygame.init()
width = 1500
height = 900
screen = pygame.display.set_mode((width, height)) # Width by Height

# Window Stuff
pygame.display.set_caption('Pong')
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

# Player Stuff
player_img = pygame.image.load('player.png')
player_X = 10
player_Y_default = height/2 - 100
player_Y_dif = 0

# Ball Stuff
ball_img = pygame.image.load('ball.png')
ball_X = width/2 - 15
ball_Y = height/2 - 15
ball_dir_X = -3
ball_dir_Y = 3

# CPU Stuff
cpu_img = pygame.image.load('player.png')
cpu_X = width - 10 - 27
cpu_Y = height/2 - 100

# draw text function
#def draw_text(text, font, color, surface, x, y):
#	textobj = font.render(text, 1, color)
#	textrect = textobj.get_rect()
#	textrect.topleft = (x, y)
#	surface.blit(textobj, textrect)

# main_menu function
#def main_menu():
#		global click
#		global font
#		while True:
#			screen.fill((0,190,255))
#			draw_text('Main Menu', font, (0,0,0), screen, 250, 40)
#			
#			mx, my = pygame.mouse.get_pos()
#			
#			# creating buton
#			button_1 = pygame.Rect(200, 100, 200, 50)
#			
#			# defining functions when a certain button is pressed
#			if button_1.collidepoint((mx, my)):
#				if click:
#					score = 0
#					print("score = 0")
#					game()
#			pygame.draw.rect(screen, (255, 0, 0), button_1)
#			
#			# writing text on top of button
#			draw_text('PLAY', font, (255, 255, 255), screen, 270, 115)
#			
#			click = False
#			for event in pygame.event.get():
#				if event.type == QUIT: 
#					pygame.quit()
#					sys.exit()
#				if event.type == KEYDOWN: 
#					if event.key == K_ESCAPE:
#						pygame.quit()
#						sys.exit()
#				if event.type == MOUSEBUTTONDOWN: 
#					if event.button == 1:
#						click = True
#			
#			pygame.display.update()
#			mainClock.tick(60)



# game function
#def game():
#	global game_on
#	while game_on: 
#		screen.fill((255,225,226))
#	
#	for event in pygame.event.get():
#		if event.type==pygame.QUIT:
#			game_on=False
#	
#	key_input = pygame.key.get_pressed()
#	if key_input[pygame.K_w]:
#		move_up(4)
#	elif key_input[pygame.K_s]:
#		move_down(4)
#	elif key_input[pygame.K_UP]:
#		move_up(4)
#	elif key_input[pygame.K_DOWN]:
#		move_down(4)
#
#	if key_input[pygame.K_5]:
#		game_on=False
#
#
#	player(player_Y_default+player_Y_dif)
#	calc_ball()
#	calc_cpu()
#	ball()
#	cpu()
#	pygame.display.update()
#

def player(y_val):
	screen.blit(player_img, (player_X, y_val))
	
def ball():
	screen.blit(ball_img, (ball_X, ball_Y))
	
def cpu():
	screen.blit(cpu_img, (cpu_X, cpu_Y))
	
def calc_cpu():
	global cpu_Y
	global ball_Y
	if cpu_Y+100-ball_Y-15 > 0:
		cpu_Y -= 3
	elif cpu_Y+100-ball_Y-15 < 0:
		cpu_Y += 3
	cpu_Y = min(cpu_Y, height-10-200)
	cpu_Y = max(cpu_Y, 10)
	
def game_over(win):
	global ball_dir_X
	global ball_dir_Y
	global ball_X
	global ball_Y
	print(win)
	ball_X = width/2 - 15
	ball_Y = height/2 - 15
	ball_dir_X = -3
	ball_dir_Y = 3

def calc_ball():
	global ball_dir_X
	global ball_dir_Y
	global ball_X
	global ball_Y
	if ball_Y == 10:
		ball_dir_Y *= -1
	elif ball_Y == height-10-30:
		ball_dir_Y *= -1
	if ball_X <= 37 and ball_Y >= player_Y_default+player_Y_dif-30 and ball_Y <= player_Y_default+player_Y_dif+200 and ball_dir_X < 0:
		ball_dir_X *= -1
	if ball_X >= cpu_X and ball_Y >= cpu_Y-11 and ball_Y <= cpu_Y+200-19 and ball_dir_X > 0:
		ball_dir_X *= -1

	ball_X+=ball_dir_X
	ball_Y+=ball_dir_Y
	if(ball_X < 30):
		game_over(False)
	elif (ball_X > cpu_X+10):
		game_over(True)
	ball_Y = min(ball_Y, height-10-30)
	ball_Y = max(ball_Y, 10)
	
def move_up(y_val):
	global player_Y_dif
	if player_Y_dif-y_val >= -player_Y_default+10:
		player_Y_dif -= y_val

def move_down(y_val):
	global player_Y_dif
	if player_Y_dif+y_val <= player_Y_default-10:
		player_Y_dif += y_val
	

while game_on:
	screen.fill((255,225,226))
	
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			game_on=False
	
	key_input = pygame.key.get_pressed()
	if key_input[pygame.K_w]:
		move_up(4)
	elif key_input[pygame.K_s]:
		move_down(4)
	elif key_input[pygame.K_UP]:
		move_up(4)
	elif key_input[pygame.K_DOWN]:
		move_down(4)

	if key_input[pygame.K_5]:
		game_on=False

	player(player_Y_default+player_Y_dif)
	calc_ball()
	calc_cpu()
	ball()
	cpu()
	pygame.display.update()


