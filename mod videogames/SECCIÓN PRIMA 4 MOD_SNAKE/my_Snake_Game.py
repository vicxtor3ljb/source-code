# modified from: 
	# https://github.com/rajatdiptabiswas/snake-pygame

#snake pygame

"""
Snake Eater
Made with PyGame
"""

import os
import pygame, sys, time, random
from pygame._sdl2 import Window, Texture, Image, Renderer, get_drivers, messagebox
import texttoimage
import pygame.freetype

# Difficulty settings
# Easy       -> 10
# Medium     -> 25
# Hard       -> 40
# Harder     -> 60
# Impossible -> 120

difficulty = 5

"""
Setting up an environment to initialize pygame
"""
mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption('game base')
screen = pygame.display.set_mode((600, 300),0,32)
 
#setting font settings
font = pygame.font.SysFont(None, 30)

# Window size
frame_size_x = 720
frame_size_y = 480
screen = pygame.display.set_mode((frame_size_x, frame_size_y))
screen = pygame.display.set_mode((frame_size_x, frame_size_y))
gameDisplay = pygame.display.set_mode((frame_size_x,frame_size_y))
clock = pygame.time.Clock()
#game_state = "start_menu"

#pause_text = pygame.font.SysFont('Consolas', 32).render('Pause', True, pygame.color.Color('White'))

def load_img(file):
    return pg.image.load(os.path.join(data_dir, file))

# Check for errors encountered
check_errors = pygame.init()
# pygame.init() example output -> (6, 0)
# second number in tuple gives number of errors
if check_errors[1] > 0:
	print(f'[!] Had {check_errors[1]} errors when initialising game, exiting...')
	sys.exit(-1)
else: 
	print('[+] Game succesfully initialised')

text_font = pygame.font.SysFont("Arial", 30)

#def draw_text(text, font, text_col, x, y):
#	img = font.render(text, True, text_col)
#	game_window2.blit(img, (x, y))
	
# Initialise game window
# pygame.display.set_caption('Snake Eater')
game_window1 = pygame.display.set_mode((frame_size_x, frame_size_y))
#game_window2 = Window("Text Hello World", size=(frame_size_x, frame_size_y), always_on_top=False)
#font = pygame.font.Font(pygame.font.get_default_font(), 300)
#text_surface = font.render('Hello world\n Here I am \n I am gonna give it everything I can', True, pygame.Color('grey'))
#pepe = texttoimage.convert(text, image_file ='text.png', font_size=100, color='red')
#alpha_image_surface = pygame.image.load('text.png').convert_alpha()
#renderer2 = Renderer(game_window2)
#tex2 = Texture.from_surface(renderer2, text_surface)
#tex2.draw()
#renderer2.present()
#del tex2
#renderer2.clear()

# Colors (R, G, B)
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

# second game window
#game_window2.fill(black)
#font = pygame.font.SysFont("Arial",36)
#txtsurf = font.render("Hello, World", True, white)
#pygame.display.update() 

# FPS (frames per second) controller
fps_controller = pygame.time.Clock()

# Game variables
snake_pos = [100, 50]
snake_body = [[100, 50], [100-10, 50], [100-(2*10),50]]

food1_pos = [random.randrange(1, (frame_size_x//10)) * 10, random.randrange(1, (frame_size_y//10)) * 10]
food1_spawn = True
food2_pos = [random.randrange(1, (frame_size_x//10)) * 10, random.randrange(1, (frame_size_y//10)) * 10]
food2_spawn = True 
food3_pos = [random.randrange(1, (frame_size_x//10)) * 10, random.randrange(1, (frame_size_y//10)) * 10]
food3_spawn = True
food4_pos = [random.randrange(1, (frame_size_x//10)) * 10, random.randrange(1, (frame_size_y//10)) * 10]
food4_spawn = True 

direction = 'RIGHT'
change_to = direction 

score = 0

"""
# text objects
def text_objects(text, font):
	textSurface = font.render(text, True, black)
	return textSurface, textSurface.get_rect()
"""

"""
# Start menu
def draw_start_menu():
   screen.fill((0, 0, 0))
   font = pygame.font.SysFont('arial', 40)
   title = font.render('My Game', True, (255, 255, 255))
   start_button = font.render('Start', True, (255, 255, 255))
   screen.blit(title, (frame_size_x/2 - title.get_width()/2, frame_size_y/2 - title.get_height()/2))
   screen.blit(start_button, (frame_size_x/2 - start_button.get_width()/2, frame_size_y/2 + start_button.get_height()/2))
   pygame.display.update()
				
# Game Over 
def game_over():
	my_font = pygame.font.SysFont('times new roman', 90)
	game_over_surface = my_font.render('YOU DIED', True, red)
	game_over_rect = game_over_surface.get_rect()
	game_over_rect.midtop = (frame_size_x/2, frame_size_y/4)
	game_window1.fill(black)
	game_window1.blit(game_over_surface, game_over_rect)
	show_score(0, red, 'times', 20)
	pygame.display.flip()
	time.sleep(3)
	pygame.quit()
	sys.exit()
"""

# Score 
def show_score(choice, color, font, size):
	score_font = pygame.font.SysFont(font, size)
	score_surface = score_font.render('Score: ' + str(score), True, color)
	score_rect = score_surface.get_rect()
	if choice == 1:
		score_rect.midtop = (frame_size_x/10,15)
	else: 
		score_rect.midtop = (frame_size_x/2, frame_size_y/1.25)
	game_window1.blit(score_surface, score_rect)
	# pygame.display.flip()
	
"""
A function that can be used to write text on our screen and buttons
"""
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
 
# A variable to check for the status later
click = False
 
# Main container function that holds the buttons and game functions
def main_menu():
    while True:
 
        screen.fill((0,190,255))
        draw_text('Main Menu', font, (0,0,0), screen, 250, 40)
 
        mx, my = pygame.mouse.get_pos()

        #creating buttons
        button_1 = pygame.Rect(200, 100, 200, 50)
        button_2 = pygame.Rect(200, 180, 200, 50)

        #defining functions when a certain button is pressed
        if button_1.collidepoint((mx, my)):
            if click:
                game()
        if button_2.collidepoint((mx, my)):
            if click:
                options()
        pygame.draw.rect(screen, (255, 0, 0), button_1)
        pygame.draw.rect(screen, (255, 0, 0), button_2)
 
        #writing text on top of button
        draw_text('PLAY', font, (255,255,255), screen, 270, 115)
        draw_text('OPTIONS', font, (255,255,255), screen, 250, 195)


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
 
"""
This function is called when the "PLAY" button is clicked.
"""
def game():
    running = True
    while running:
		pygame.time.delay(60)
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT: 
			running = False
			
		keys = pygame.key.get_pressed() 
		if keys[pygame.K_UP]:
			change_to = 'UP'
		if keys[pygame.K_DOWN]:
			change_to = 'DOWN'
		if keys[pygame.K_LEFT]:
			change_to = 'LEFT'
		if keys[pygame.K_RIGHT]:
			change_to = 'RIGHT'
		# Esc -> Create event to quit the game
		if keys[pygame.K_ESCAPE]: 
			pygame.event.post(pygame.event.Event(pygame.QUIT))
	
	# Making sure the snake cannot move in the opposite direction instantaneously
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
		snake_pos[1] -= 10
	if direction == 'DOWN':
		snake_pos[1] += 10
	if direction == 'LEFT':
		snake_pos[0] -= 10
	if direction == 'RIGHT':
		snake_pos[0] += 10
	
	# Snake body growing mechanism
	snake_body.insert(0, list(snake_pos))
	if snake_pos[0] == food1_pos[0] and snake_pos[1] == food1_pos[1]: 
		score += 1
		food1_spawn = False
	elif snake_pos[0] == food2_pos[0] and snake_pos[1] == food2_pos[1]:
		score += 1
		food2_spawn = False 
	elif snake_pos[0] == food3_pos[0] and snake_pos[1] == food3_pos[1]:
		score += 1
		food3_spawn = False
	elif snake_pos[0] == food4_pos[0] and snake_pos[1] == food4_pos[1]:
		score += 1
		food4_spawn = False
	else: 
		snake_body.pop() 
		
	# Spawning food on the screen
	if not food1_spawn: 
		food1_pos = [random.randrange(1, (frame_size_x//10)) * 10, random.randrange(1, (frame_size_y//10)) * 10]
	food1_spawn = True
	if not food2_spawn: 
		food2_pos = [random.randrange(1, (frame_size_x//10)) * 10, random.randrange(1, (frame_size_y//10)) * 10]
	food2_spawn = True
	if not food3_spawn: 
		food3_pos = [random.randrange(1, (frame_size_x//10)) * 10, random.randrange(1, (frame_size_y//10)) * 10]	
	food3_spawn = True
	if not food4_spawn: 
		food4_pos = [random.randrange(1, (frame_size_x//10)) * 10, random.randrange(1, (frame_size_y//10)) * 10]
	food4_spawn = True

	# GFX
	game_window1.fill(black)
	for pos in snake_body:
		# Snake body
		# .draw.rect(play_surface, color, xy-coordinate)
		# xy-coordinate -> .Rect(x, y, size_x, size_y)
		pygame.draw.rect(game_window1, green, pygame.Rect(pos[0], pos[1], 10, 10))
		
	# Snake foods
	pygame.draw.rect(game_window1, white, pygame.Rect(food1_pos[0], food1_pos[1], 10, 10))
	pygame.draw.rect(game_window1, red, pygame.Rect(food2_pos[0], food2_pos[1], 10, 10))
	pygame.draw.rect(game_window1, green, pygame.Rect(food3_pos[0], food3_pos[1], 10, 10))
	pygame.draw.rect(game_window1, blue, pygame.Rect(food4_pos[0], food4_pos[1], 10, 10))

	# Game Over conditions
	# Getting out of bounds
	if snake_pos[0] < 0 or snake_pos[0] > frame_size_x-10:
		game_over()
	if snake_pos[1] < 0 or snake_pos[1] > frame_size_y-10:
		game_over()
	# Touching the snake body
	for block in snake_body[1:]:
		if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
			game_over()
	
	show_score(1, white, 'consolas', 20)
	# Refresh game screen
	pygame.display.update()
	# Refresh rate
	fps_controller.tick(difficulty)

		
		
    #screen.fill((0,0,0))
    #draw_text('GAME SCREEN', font, (255, 255, 255), screen, 20, 20)
	#for event in pygame.event.get():
	#	if event.type == QUIT:
	#		pygame.quit()
	#		sys.exit()
	#	if event.type == KEYDOWN:
	#		if event.key == K_ESCAPE:
	#			running = False
    #   pygame.display.update()
    #   mainClock.tick(60)

"""
    while running:
        pygame.time.delay(60)
        
	for event in pygame.event.get():
		if event.type == pygame.QUIT: 
			running = False
			
		keys = pygame.key.get_pressed() 
		if keys[pygame.K_UP]:
			change_to = 'UP'
		if keys[pygame.K_DOWN]:
			change_to = 'DOWN'
		if keys[pygame.K_LEFT]:
			change_to = 'LEFT'
		if keys[pygame.K_RIGHT]:
			change_to = 'RIGHT'
		# Esc -> Create event to quit the game
		if keys[pygame.K_ESCAPE]: 
			pygame.event.post(pygame.event.Event(pygame.QUIT))
	
	# Making sure the snake cannot move in the opposite direction instantaneously
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
		snake_pos[1] -= 10
	if direction == 'DOWN':
		snake_pos[1] += 10
	if direction == 'LEFT':
		snake_pos[0] -= 10
	if direction == 'RIGHT':
		snake_pos[0] += 10
	
	# Snake body growing mechanism
	snake_body.insert(0, list(snake_pos))
	if snake_pos[0] == food1_pos[0] and snake_pos[1] == food1_pos[1]: 
		score += 1
		food1_spawn = False
	elif snake_pos[0] == food2_pos[0] and snake_pos[1] == food2_pos[1]:
		score += 1
		food2_spawn = False 
	elif snake_pos[0] == food3_pos[0] and snake_pos[1] == food3_pos[1]:
		score += 1
		food3_spawn = False
	elif snake_pos[0] == food4_pos[0] and snake_pos[1] == food4_pos[1]:
		score += 1
		food4_spawn = False
	else: 
		snake_body.pop() 
		
	# Spawning food on the screen
	if not food1_spawn: 
		food1_pos = [random.randrange(1, (frame_size_x//10)) * 10, random.randrange(1, (frame_size_y//10)) * 10]
	food1_spawn = True
	if not food2_spawn: 
		food2_pos = [random.randrange(1, (frame_size_x//10)) * 10, random.randrange(1, (frame_size_y//10)) * 10]
	food2_spawn = True
	if not food3_spawn: 
		food3_pos = [random.randrange(1, (frame_size_x//10)) * 10, random.randrange(1, (frame_size_y//10)) * 10]	
	food3_spawn = True
	if not food4_spawn: 
		food4_pos = [random.randrange(1, (frame_size_x//10)) * 10, random.randrange(1, (frame_size_y//10)) * 10]
	food4_spawn = True

	# GFX
	game_window1.fill(black)
	for pos in snake_body:
		# Snake body
		# .draw.rect(play_surface, color, xy-coordinate)
		# xy-coordinate -> .Rect(x, y, size_x, size_y)
		pygame.draw.rect(game_window1, green, pygame.Rect(pos[0], pos[1], 10, 10))
		
	# Snake foods
	pygame.draw.rect(game_window1, white, pygame.Rect(food1_pos[0], food1_pos[1], 10, 10))
	pygame.draw.rect(game_window1, red, pygame.Rect(food2_pos[0], food2_pos[1], 10, 10))
	pygame.draw.rect(game_window1, green, pygame.Rect(food3_pos[0], food3_pos[1], 10, 10))
	pygame.draw.rect(game_window1, blue, pygame.Rect(food4_pos[0], food4_pos[1], 10, 10))

	# Game Over conditions
	# Getting out of bounds
	if snake_pos[0] < 0 or snake_pos[0] > frame_size_x-10:
		game_over()
	if snake_pos[1] < 0 or snake_pos[1] > frame_size_y-10:
		game_over()
	# Touching the snake body
	for block in snake_body[1:]:
		if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
			game_over()
	
	show_score(1, white, 'consolas', 20)
	# Refresh game screen
	pygame.display.update()
	# Refresh rate
	fps_controller.tick(difficulty)

        
"""        
"""
"""   
        
"""
This function is called when the "OPTIONS" button is clicked.
"""
def options():
    running = True
    while running:
        screen.fill((0,0,0))
        draw_text('OPTIONS SCREEN', font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
       
        pygame.display.update()
        mainClock.tick(60)
	
main_menu()
	
	
"""
# Redraw	
def redraw():
    if playing:
        win.blit(bg, (0,0))
        
        #Score Text
        font = pygame.font.SysFont('Time New Roman', 32)
        score = font.render('SCORE: '+ str(snake.score), False, white)
        scoreRect = score.get_rect()
        scoreRect.center = (width//2 , 50)
        win.blit(score, scoreRect)
        
        #Draw Sprite Groups
        sprites_group.update()
        sprites_group.draw(win)
        bomb_group.update()
        bomb_group.draw(win)
    else:
        win.fill(black)
        
        font = pygame.font.SysFont('Time New Roman', 60)
        #Title Text
        title = font.render('SNAKE', False, green)
        titleRect = title.get_rect()
        titleRect.center = (width//2 , 100)
        win.blit(title, titleRect)
        
        #High Score Text
        high = font.render('High Score: ' + str(snake.highScore), False, purple)
        highRect = high.get_rect()
        highRect.center = (width//2, height//2)
        win.blit(high, highRect)
        
        #Start Text
        start = font.render('Press Space to Start', False, ((randint(0,255),randint(0,255),randint(0,255))))
        startRect = start.get_rect()
        startRect.center = (width//2 , height - 50)
        win.blit(start, startRect)
        
    pygame.display.update()	
"""

running = True




# Main logic
while running: 
	
	pygame.time.delay(60)
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT: 
			running = False
			
		keys = pygame.key.get_pressed() 
		if keys[pygame.K_UP]:
			change_to = 'UP'
		if keys[pygame.K_DOWN]:
			change_to = 'DOWN'
		if keys[pygame.K_LEFT]:
			change_to = 'LEFT'
		if keys[pygame.K_RIGHT]:
			change_to = 'RIGHT'
		# Esc -> Create event to quit the game
		if keys[pygame.K_ESCAPE]: 
			pygame.event.post(pygame.event.Event(pygame.QUIT))
	
	# Making sure the snake cannot move in the opposite direction instantaneously
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
		snake_pos[1] -= 10
	if direction == 'DOWN':
		snake_pos[1] += 10
	if direction == 'LEFT':
		snake_pos[0] -= 10
	if direction == 'RIGHT':
		snake_pos[0] += 10
	
	# Snake body growing mechanism
	snake_body.insert(0, list(snake_pos))
	if snake_pos[0] == food1_pos[0] and snake_pos[1] == food1_pos[1]: 
		score += 1
		food1_spawn = False
	elif snake_pos[0] == food2_pos[0] and snake_pos[1] == food2_pos[1]:
		score += 1
		food2_spawn = False 
	elif snake_pos[0] == food3_pos[0] and snake_pos[1] == food3_pos[1]:
		score += 1
		food3_spawn = False
	elif snake_pos[0] == food4_pos[0] and snake_pos[1] == food4_pos[1]:
		score += 1
		food4_spawn = False
	else: 
		snake_body.pop() 
		
	# Spawning food on the screen
	if not food1_spawn: 
		food1_pos = [random.randrange(1, (frame_size_x//10)) * 10, random.randrange(1, (frame_size_y//10)) * 10]
	food1_spawn = True
	if not food2_spawn: 
		food2_pos = [random.randrange(1, (frame_size_x//10)) * 10, random.randrange(1, (frame_size_y//10)) * 10]
	food2_spawn = True
	if not food3_spawn: 
		food3_pos = [random.randrange(1, (frame_size_x//10)) * 10, random.randrange(1, (frame_size_y//10)) * 10]	
	food3_spawn = True
	if not food4_spawn: 
		food4_pos = [random.randrange(1, (frame_size_x//10)) * 10, random.randrange(1, (frame_size_y//10)) * 10]
	food4_spawn = True

	# GFX
	game_window1.fill(black)
	for pos in snake_body:
		# Snake body
		# .draw.rect(play_surface, color, xy-coordinate)
		# xy-coordinate -> .Rect(x, y, size_x, size_y)
		pygame.draw.rect(game_window1, green, pygame.Rect(pos[0], pos[1], 10, 10))
		
	# Snake foods
	pygame.draw.rect(game_window1, white, pygame.Rect(food1_pos[0], food1_pos[1], 10, 10))
	pygame.draw.rect(game_window1, red, pygame.Rect(food2_pos[0], food2_pos[1], 10, 10))
	pygame.draw.rect(game_window1, green, pygame.Rect(food3_pos[0], food3_pos[1], 10, 10))
	pygame.draw.rect(game_window1, blue, pygame.Rect(food4_pos[0], food4_pos[1], 10, 10))

	# Game Over conditions
	# Getting out of bounds
	if snake_pos[0] < 0 or snake_pos[0] > frame_size_x-10:
		game_over()
	if snake_pos[1] < 0 or snake_pos[1] > frame_size_y-10:
		game_over()
	# Touching the snake body
	for block in snake_body[1:]:
		if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
			game_over()
	
	show_score(1, white, 'consolas', 20)
	# Refresh game screen
	pygame.display.update()
	# Refresh rate
	fps_controller.tick(difficulty)
