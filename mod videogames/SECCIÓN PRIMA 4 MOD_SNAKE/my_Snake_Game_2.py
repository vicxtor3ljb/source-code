# https://www.mrmichaelsclass.com/python-programming/python-projects/pygame-snake

import pygame
from random import randint

pygame.init()

width = 500
height = 500
win = pygame.display.set_mode((width, height))

pygame.display.set_caption('Snake Mod')

# Colors (R, G, B)
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
purple = (255, 0, 255)

# Object Classes
class Snake(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface([10,10])
		self.image.fill(black)
		self.rect = self.image.get_rect()
		self.score = 0
		self.highScore = 0
		self.speed = 10
		self.dx = 0
		self.dy = 0
	
class redFood(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface([10, 10])
		self.image.fill(red)
		self.rect = self.image.get_rect()
	def move(self):
		food1.rect.x = randint(50, width - 50)
		food1.rect.y = randint(50, height - 50)

class blackFood(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface([10, 10])
		self.image.fill(black)
		self.rect = self.image.get_rect()
	def move(self):
		food2.rect.x = randint(50, width - 50)
		food2.rect.y = randint(50, height - 50)
	
class blueFood(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface([10, 10])
		self.image.fill(blue)
		self.rect = self.image.get_rect()
	def move(self):
		food3.rect.x = randint(50, width - 50)
		food3.rect.y = randint(50, height - 50)	

class whiteFood(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface([10, 10])
		self.image.fill(white)
		self.rect = self.image.get_rect()
	def move(self):
		food4.rect.x = randint(50, width - 50)
		food4.rect.y = randint(50, height - 50)	

		
class Bomb(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface([25, 25])
		self.image.fill(purple)
		self.rect = self.image.get_rect()
	
# Where to draw obejcts
snake = Snake()
snake.rect.x = width // 2
snake.rect.y = height // 2

food1 = redFood()
food1.rect.x = randint(50, width - 50)
food1.rect.y = randint(50, height - 50)

food2 = blackFood()
food2.rect.x = randint(50, width - 50)
food2.rect.y = randint(50, height - 50)

food3 = blueFood()
food3.rect.x = randint(50, width - 50)
food3.rect.y = randint(50, height - 50)

food4 = whiteFood()
food4.rect.x = randint(50, width - 50)
food4.rect.y = randint(50, height - 50)


# Sprite groups
sprites_group = pygame.sprite.Group()
sprites_group.add(snake)
sprites_group.add(food1)
sprites_group.add(food2)
sprites_group.add(food3)
sprites_group.add(food4)

bomb_group = pygame.sprite.Group()

def redraw():
	if playing:
		win.fill(green)
		
		# Score Text
		font = pygame.font.SysFont('Times New Roman', 24)
		score = font.render('SCORE: ' + str(snake.score), False, black)
		scoreRect = score.get_rect()
		scoreRect.center = (width//2, 50)
		win.blit(score, scoreRect)
		
		# Draw Sprite Groups
		sprites_group.update()
		sprites_group.draw(win)
		bomb_group.update()
		bomb_group.draw(win)
	else:
		win.fill(black)
		
		font = pygame.font.SysFont('Times New Roman', 60)
		# Title Text
		title = font.render('SNAKE', False, green)
		titleRect = title.get_rect()
		titleRect.center = (width//2, 100)
		win.blit(title, titleRect)
		
		# High Score Text
		high = font.render('High Score: ' + str(snake.highScore), False, purple)
		highRect = high.get_rect()
		highRect.center = (width//2, height//2)
		win.blit(high, highRect)
		
		# Start Text
		start = font.render('Press Space to Start', False, ((randint(0,255), randint(0,255),randint(0,255))))
		startRect = start.get_rect()
		startRect.center = (width//2, height - 50)
		win.blit(start, startRect)
	
	pygame.display.update()
	
running = True
playing = False

while running: 
	
	pygame.time.delay(60)
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	
	if playing:
		snake.rect.x += snake.dx
		snake.rect.y += snake.dy
		
		#Movement Controls
		key = pygame.key.get_pressed()
		if key[pygame.K_LEFT]:
			snake.dx = -snake.speed
			snake.dy = 0
		if key[pygame.K_RIGHT]:
			snake.dx = snake.speed
			snake.dy = 0
		if key[pygame.K_UP]:
			snake.dx = 0
			snake.dy = -snake.speed
		if key[pygame.K_DOWN]:
			snake.dx = 0
			snake.dy = snake.speed
		
		#Collision
		if snake.rect.colliderect(food1.rect):
			food1.move()
			bomb = Bomb()
			bomb.rect.x = snake.rect.x + 50
			bomb.rect.y = snake.rect.y + 50
			bomb_group.add(bomb)
			snake.score += 1
		
		elif snake.rect.colliderect(food2.rect):
			food2.move()
			bomb = Bomb()
			bomb.rect.x = snake.rect.x + 50
			bomb.rect.y = snake.rect.y + 50
			bomb_group.add(bomb)
			snake.score += 1
		
		elif snake.rect.colliderect(food3.rect):
			food3.move()
			bomb = Bomb()
			bomb.rect.x = snake.rect.x + 50
			bomb.rect.y = snake.rect.y + 50
			bomb_group.add(bomb)
			snake.score += 1
		
		elif snake.rect.colliderect(food4.rect):
			food4.move()
			bomb = Bomb()
			bomb.rect.x = snake.rect.x + 50
			bomb.rect.y = snake.rect.y + 50
			bomb_group.add(bomb)
			snake.score += 1
		
		for bomb in bomb_group:
			if bomb.rect.colliderect(snake.rect):
				if snake.score > snake.highScore:
					snake.highScore = snake.score
				playing = False
				
	else: 
		key = pygame.key.get_pressed()
		if key[pygame.K_SPACE]:
			playing = True
			snake.rect.x = width // 2
			snake.rect.y = height // 2
			snake.score = 0
			bomb_group.empty()
	redraw()

pygame.quit()
