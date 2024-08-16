from os import stat_result
import pygame
import random
import time
import os.path

# Ideas: 
# Add tutorial levels: 0.1, 0.2, 0.3 or tips list and display "str(level) + tips[level-1]"

# Define some constants
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 1000
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

CYAN = (0, 255, 255)
GRAY = (100, 100, 100)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (150, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 100, 0)

class Player(pygame.sprite.Sprite):
	# Sprite class for the player
	def __init__(self, image_us, image_s):
		pygame.sprite.Sprite.__init__(self)
		self.image_normal = image_us
		self.image_shielded = image_s
		self.image.set_colorkey(BLACK)
		self.rect =self.image.get_rect()
		sefl.rect.centerx = SCREEN_WIDTH // 2
		self.rect.bottom = SCREEN_HEIGHT - 50
		self.shielded = False
		
	def update(self):
		self.speedx = 0
		# If left or right key is pressed, move left or right
		pressed_key = pygame.key.get_pressed()
		if pressed_key[pygame.K_LEFT]:
			self.speedx = -5
		if pressed_key[pygame.K_RIGHT]:
			self.speedx = 5
		
		# No further move if off screen
		if self.rect.right > SCREEN_WIDTH:
			self.rect.right = SCREEN_WIDTH
		if self.rect.left < 0: 
			self.rect.left = 0
	
	def shield(self):
		self.shielded = True 
		x_pos = self.rect.centerx
		self.image = self.image_normal
		self.immage.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
		self.rect.centerx = x_pos
		self.fect.bottom = SCREEN_HEIGHT - 50
	def unshield(self):
		self.shielded = False
		x_pos = self.rect.centerx
		self.image = self.image_normal
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
		self.rect.centerx = x_pos
		self.rect.bottom = SCREEN_HEIGHT - 50
	
class Mob(pygame.sprite.Sprite):
	# Sprite class for the mobs
	def __init__(self, x, y, speed, health, mob_self_img):
		
		
