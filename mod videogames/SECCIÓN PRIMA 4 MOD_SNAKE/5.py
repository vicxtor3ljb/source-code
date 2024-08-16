# Importing libraries
import pygame
import time
import random
import sys
from pygame.locals import *


# Environment
mainClock = pygame.time.Clock()

# Snake speed
snake_speed = 5

# Window size
window_x = 720
window_y = 480

# Colors (R, G, B)
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
purple = pygame.Color(255, 0, 255)

# Initialising pygame
pygame.init()

#setting font settings
font = pygame.font.SysFont(None, 30)

# Initialise game window
pygame.display.set_caption('Snake Mod')
game_window = pygame.display.set_mode((window_x, window_y))

# FPS (Frames per second) controller
fps = pygame.time.Clock()

# defining snake default position
snake_position = [100, 50]

# defining first 4 blocks of snake
# body
snake_body = [ 	[100, 50],
				[90, 50],
				[80, 50],
				[70, 50]
]

# fruits position
whitefruit_position = [random.randrange(1, (window_x//10)) * 10,
					   random.randrange(1, (window_y//10)) * 10]
whitefruit_spawn = True

redfruit_position = [random.randrange(1, (window_x//10)) * 10,
					   random.randrange(1, (window_y//10)) * 10]
redfruit_spawn = True

greenfruit_position = [random.randrange(1, (window_x//10)) * 10,
					   random.randrange(1, (window_y//10)) * 10]
greenfruit_spawn = True

bluefruit_position = [random.randrange(1, (window_x//10)) * 10,
					   random.randrange(1, (window_y//10)) * 10]
bluefruit_spawn = True

# setting default snake direction
# towards right
direction= 'RIGHT'
change_to = direction

# initial score
score = 0

# draw text
def draw_text(text, font, color, surface, x, y):
	textobj = font.render(text, 1, color)
	textrect = textobj.get_rect()
	textrect.topleft = (x, y)
	surface.blit(textobj, textrect)

# displaying Score function
def show_score(choice, color, font, size):
	
	# creating font object score_font
	score_font = pygame.font.SysFont(font, size)
	
	# create the display surface object
	# score_surface
	score_surface = score_font.render('Score : ' + str(score), True, color)
	
	# create a rectangular object for the
	# text surface object
	score_rect = score_surface.get_rect()
	
	# displaying text
	game_window.blit(score_surface, score_rect)
	
# game over function
def game_over():
	# creating font object my_font
	my_font = pygame.font.SysFont('times new roman', 50)
	
	# creating a text surface on which text
	# will be drawn
	game_over_surface = my_font.render('Your Score is: ' + str(score), True, red)
	
	# create a rectangular object for the text
	# surface object
	game_over_rect = game_over_surface.get_rect()
	
	# setting position of the text
	game_over_rect.midtop = (window_x/2, window_y/4)
	
	# blit will draw the text on the screen
	game_window.blit(game_over_surface, game_over_rect)
	pygame.display.flip()
	
	# after 2 seconds we will quit the
	# program
	time.sleep(2)
	
	# deactivating pygame library
	pygame.quit()
	
	# quit the program
	quit()
		
# you won function
def you_won():
	# creating font object my_font
	my_font = pygame.font.SysFont('times new roman', 50)
	
	# creating a text surface on which text
	# will be drawn
	you_won_surface = my_font.render('You won. Your Score is: ' + str(score), True, red)
	
	# create a rectangular object for the text
	# surface object
	you_won_rect = you_won_surface.get_rect()
	
	# setting position of the text
	you_won_rect.midtop = (window_x/2, window_y/4)
	
	# blit will draw the text on the screen
	game_window.blit(you_won_surface, you_won_rect)
	pygame.display.flip()
	
	# after 2 seconds we will quit the
	# program
	time.sleep(2)
	
	# deactivating pygame library
	pygame.quit()
	
	# quit the program
	quit()
	
# main_menu function
def main_menu():
		global click
		while True:
			game_window.fill((0,190,255))
			draw_text('Main Menu', font, (0,0,0), game_window, 250, 40)
			
			mx, my = pygame.mouse.get_pos()
			
			# creating buton
			button_1 = pygame.Rect(200, 100, 200, 50)
			
			# defining functions when a certain button is pressed
			if button_1.collidepoint((mx, my)):
				if click:
					score = 0
					print("score = 0")
					game()
			pygame.draw.rect(game_window, (255, 0, 0), button_1)
			
			# writing text on top of button
			draw_text('PLAY', font, (255, 255, 255), game_window, 270, 115)
			
			click = False
			for event in pygame.event.get():
				if event.type == QUIT: 
					pygame.quit()
					sys.exit()
				if event.type == KEYDOWN: 
					if event.key == K_ESCAPE:
						pygame.quit()
						sys.exit()
				if event.type == MOUSEBUTTONDOWN: 
					if event.button == 1:
						click = True
			
			pygame.display.update()
			mainClock.tick(60)
			
# game function
def game():
	while True: 
			global direction
			global change_to
			global whitefruit_position
			global whitefruit_spawn
			global redfruit_position
			global redfruit_spawn
			global greenfruit_position
			global greenfruit_spawn
			global bluefruit_position
			global bluefruit_spawn
			global score
			
			# handling key events
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN: 
					if event.key == pygame.K_ESCAPE: 
						pygame.quit()
						sys.exit()
					if event.key == pygame.K_UP:
						change_to = 'UP'
					if event.key == pygame.K_DOWN:
						change_to = 'DOWN'
					if event.key == pygame.K_LEFT:
						change_to = 'LEFT'
					if event.key == pygame.K_RIGHT:
						change_to = 'RIGHT'
			
			# If two keys pressed simultaneously
			# we don't want snake to move into two directions
			# simultaneously
			if change_to == 'UP' and direction != 'DOWN':
				direction = 'UP'
			if change_to == 'DOWN' and direction != 'UP': 
				direction = 'DOWN'
			if change_to == 'LEFT' and direction != 'RIGHT':
				direction = 'LEFT'
			if change_to == 'RIGHT' and direction != 'LEFT':
				direction = 'RIGHT'
			
			# Moving the snake
			if direction == 'UP':
				snake_position[1] -= 10
			if direction == 'DOWN':
				snake_position[1] += 10
			if direction == 'LEFT':
				snake_position[0] -= 10
			if direction == 'RIGHT':
				snake_position[0] += 10
			
			# Snake body growing mechanism
			# if fruits and snakes collide then scores will be 
			# incremented by 10
			snake_body.insert(0, list(snake_position))
			if snake_position[0] == whitefruit_position[0] and snake_position[1] == whitefruit_position[1] and score == 0:
				score += 10
				whitefruit_spawn = False
				snake_body.pop()
			if snake_position[0] == redfruit_position[0] and snake_position[1] == redfruit_position[1] and score == 0:
				redfruit_spawn = False
				snake_body.pop()
			if snake_position[0] == greenfruit_position[0] and snake_position[1] == greenfruit_position[1] and score == 0:
				greenfruit_spawn = False
				snake_body.pop()
			if snake_position[0] == bluefruit_position[0] and snake_position[1] == bluefruit_position[1] and score == 0:
				bluefruit_spawn = False
				snake_body.pop()
	
			if snake_position[0] == whitefruit_position[0] and snake_position[1] == whitefruit_position[1] and score == 10:
				whitefruit_spawn = False
				snake_body.pop()
			if snake_position[0] == redfruit_position[0] and snake_position[1] == redfruit_position[1] and score == 10:
				score += 10
				redfruit_spawn = False
				snake_body.pop()
			if snake_position[0] == greenfruit_position[0] and snake_position[1] == greenfruit_position[1] and score == 10:
				greenfruit_spawn = False
				snake_body.pop()
			if snake_position[0] == bluefruit_position[0] and snake_position[1] == bluefruit_position[1] and score == 10:
				bluefruit_spawn = False
				snake_body.pop()
				
			if snake_position[0] == whitefruit_position[0] and snake_position[1] == whitefruit_position[1] and score == 20:
				whitefruit_spawn = False
				snake_body.pop()
			if snake_position[0] == redfruit_position[0] and snake_position[1] == redfruit_position[1] and score == 20:
				redfruit_spawn = False
				snake_body.pop()
			if snake_position[0] == greenfruit_position[0] and snake_position[1] == greenfruit_position[1] and score == 20:
				score += 10
				greenfruit_spawn = False
				snake_body.pop()
			if snake_position[0] == bluefruit_position[0] and snake_position[1] == bluefruit_position[1] and score == 20:
				bluefruit_spawn = False
				snake_body.pop()
			
			if snake_position[0] == whitefruit_position[0] and snake_position[1] == whitefruit_position[1] and score == 30:
				whitefruit_spawn = False
				snake_body.pop()
			if snake_position[0] == redfruit_position[0] and snake_position[1] == redfruit_position[1] and score == 30:
				redfruit_spawn = False
				snake_body.pop()
			if snake_position[0] == greenfruit_position[0] and snake_position[1] == greenfruit_position[1] and score == 30:
				greenfruit_spawn = False
				snake_body.pop()
			if snake_position[0] == bluefruit_position[0] and snake_position[1] == bluefruit_position[1] and score == 30:
				you_won()
			
	
			#else: 
			#	snake_body.pop()
			
			if whitefruit_spawn == False:
				whitefruit_position = [random.randrange(1, (window_x//10)) * 10,
									   random.randrange(1, (window_y//10)) * 10]
			
			if redfruit_spawn == False:
				redfruit_position = [random.randrange(1, (window_x//10)) * 10,
									   random.randrange(1, (window_y//10)) * 10]
			
			if greenfruit_spawn == False:
				greenfruit_position = [random.randrange(1, (window_x//10)) * 10,
									   random.randrange(1, (window_y//10)) * 10]
			
			if bluefruit_spawn == False:
				bluefruit_position = [random.randrange(1, (window_x//10)) * 10,
									   random.randrange(1, (window_y//10)) * 10]
			
			whitefruit_spawn = True
			redfruit_spawn = True
			greenfruit_spawn = True
			bluefruit_spawn = True 
			
			game_window.fill(black)
			
			for pos in snake_body:
				pygame.draw.rect(game_window, green, pygame.Rect(
					pos[0], pos[1], 10, 10))
					
			pygame.draw.rect(game_window, white, pygame.Rect(
				whitefruit_position[0], whitefruit_position[1], 10, 10))
			
			pygame.draw.rect(game_window, red, pygame.Rect(
				redfruit_position[0], redfruit_position[1], 10, 10))
			
			pygame.draw.rect(game_window, green, pygame.Rect(
				greenfruit_position[0], greenfruit_position[1], 10, 10))
			
			pygame.draw.rect(game_window, blue, pygame.Rect(
				bluefruit_position[0], bluefruit_position[1], 10, 10))
			
			
			# Game Over conditions
			if snake_position[0] < 0 or snake_position[0] > window_x-10:
				game_over()
			if snake_position[1] < 0 or snake_position[1] > window_y-10:
				game_over()
			
			# Touching the snake body
			for block in snake_body[1:]:
				if snake_position[0] == block[0] and snake_position[1] == block[1]:
					game_over()
				
			# displaying score continuously
			show_score(1, white, 'times new roman', 20)		
			
			# Refresh game screen
			pygame.display.update()
			
			# Frame Per Second / Refresh Rate
			fps.tick(snake_speed)
	
"""
		game_window.fill((0,0,0))
		
		draw_text('GAME SCREEN', font, (255, 255, 255), game_window, 20, 20)
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			if event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					running = False
		
		pygame.display.update()
		mainClock.tick(60)
"""
		

 

main_menu()

"""
		if score == 0:
		# handling key events
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN: 
					if event.key == pygame.K_UP:
						change_to = 'UP'
					if event.key == pygame.K_DOWN:
						change_to = 'DOWN'
					if event.key == pygame.K_LEFT:
						change_to = 'LEFT'
					if event.key == pygame.K_RIGHT:
						change_to = 'RIGHT'
			
			# If two keys pressed simultaneously
			# we don't want snake to move into two directions
			# simultaneously
			if change_to == 'UP' and direction != 'DOWN':
				direction = 'UP'
			if change_to == 'DOWN' and direction != 'UP': 
				direction = 'DOWN'
			if change_to == 'LEFT' and direction != 'RIGHT':
				direction = 'LEFT'
			if change_to == 'RIGHT' and direction != 'LEFT':
				direction = 'RIGHT'
			
			# Moving the snake
			if direction == 'UP':
				snake_position[1] -= 10
			if direction == 'DOWN':
				snake_position[1] += 10
			if direction == 'LEFT':
				snake_position[0] -= 10
			if direction == 'RIGHT':
				snake_position[0] += 10
			
			# Snake body growing mechanism
			# if fruits and snakes collide then scores will be 
			# incremented by 10
			snake_body.insert(0, list(snake_position))
			if snake_position[0] == whitefruit_position[0] and snake_position[1] == whitefruit_position[1]:
				score += 10
				whitefruit_spawn = False
			else: 
				snake_body.pop()
			
			if not whitefruit_spawn:
				whitefruit_position = [random.randrange(1, (window_x//10)) * 10,
									   random.randrange(1, (window_y//10)) * 10]
			
			whitefruit_spawn = True
			game_window.fill(black)
			
			for pos in snake_body:
				pygame.draw.rect(game_window, green, pygame.Rect(
					pos[0], pos[1], 10, 10))
					
			pygame.draw.rect(game_window, white, pygame.Rect(
				whitefruit_position[0], whitefruit_position[1], 10, 10))
				
			# Game Over conditions
			if snake_position[0] < 0 or snake_position[0] > window_x-10:
				game_over()
			if snake_position[1] < 0 or snake_position[1] > window_y-10:
				game_over()
			
			# Touching the snake body
			for block in snake_body[1:]:
				if snake_position[0] == block[0] and snake_position[1] == block[1]:
					game_over()
				
			# displaying score continuously
			show_score(1, white, 'times new roman', 20)		
			
			# Refresh game screen
			pygame.display.update()
			
			# Frame Per Second / Refresh Rate
			fps.tick(snake_speed)
"""
