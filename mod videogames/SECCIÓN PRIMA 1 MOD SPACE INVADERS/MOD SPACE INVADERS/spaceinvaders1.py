#import libraries
import pygame 
import os
import time
import random

#init font
pygame.font.init()

# Screen
WIDTH, HEIGHT = 700, 700
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders")

# Load images from assets
BLUE_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_blue_small.png"))
GREEN_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_green_small.png"))
PURPLE_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_purple_small.png"))
WHITE_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_white_small.png"))

# Player ship
YELLOW_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_yellow.png"))

# Lasers
BLUE_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_blue.png"))
GREEN_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_green.png"))
PURPLE_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_purple.png"))
WHITE_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_white.png"))

# Background image
BG = pygame.transform.scale(pygame.image.load(os.path.join("assets", "background-black.png")), (WIDTH, HEIGHT))

# Class Laser
class Laser:
	def __init__(self, x, y, img):
		self.x = x
		self.y = y
		self.img = img
		self.mask = pygame.mask.from_surface(self.img)
		
	def draw(self, window):
		window.blit(self.img, (self.x, self.y))
		
	def move(self, vel):
		self.y += vel
	
	def off_screen(self, height):
		return not(self.y <= height and self.y >= 0)
	
	def collision(self, obj):
		return collide(self, obj)
		
# Class Ship
class Ship: 
	COOLDOWN = 30
		
	def __init__(self, x, y, health=100):
		self.x = x
		self.y = y
		self.health = health
		self.ship_img = None
		self.laser_img1 = None
		self.laser_img2 = None
		self.laser_img3 = None
		self.laser_img4 = None
		self.lasers = []
		self.cool_down_counter = 0
		
	def draw(self, window):
		window.blit(self.ship_img, (self.x,  self.y))
		for laser in self.lasers:
			laser.draw(window)

	def move_lasers(self, vel, obj):
		self.cooldown()
		for laser in self.lasers:
			laser.move(vel)
			if laser.off_screen(HEIGHT):
				self.lasers.remove(laser)
			elif laser.collision(obj):
				obj.health -= 10
				self.lasers.remove(laser)

	
	def cooldown(self):
		if self.cool_down_counter >= self.COOLDOWN:
			self.cool_down_counter = 0
		elif self.cool_down_counter > 0: 
			self.cool_down_counter += 1

	def blue_shoot(self):
		if self.cool_down_counter == 0: 
			laser1 = Laser(self.x, self.y, self.laser_img1)
			self.lasers.append(laser1)
			self.cool_down_counter = 1
	
	def green_shoot(self):
		if self.cool_down_counter == 0:
			laser2 = Laser(self.x, self.y, self.laser_img2)
			self.lasers.append(laser2)
			self.cool_down_counter = 1
	
	def purple_shoot(self):
		if self.cool_down_counter == 0:
			laser3 = Laser(self.x, self.y, self.laser_img3)
			self.lasers.append(laser3)
			self.cool_down_counter = 1
	
	def white_shoot(self):
		if self.cool_down_counter == 0:
			laser4 = Laser(self.x, self.y, self.laser_img4)
			self.lasers.append(laser4)
			self.cool_down_counter = 1
	
	def get_width(self):
		return self.ship_img.get_width()
	
	def get_height(self):
		return self.ship_img.get_height()

# Class Player inherits from ship
class Player(Ship):
	def __init__(self, x, y, health=100):
		super().__init__(x, y, health)
		self.ship_img = YELLOW_SPACE_SHIP
		self.laser_img1 = BLUE_LASER
		self.laser_img2 = GREEN_LASER
		self.laser_img3 = PURPLE_LASER
		self.laser_img4 = WHITE_LASER
		self.mask = pygame.mask.from_surface(self.ship_img)
		self.max_health = health
	
	def move_lasers(self, vel, objs):
		self.cooldown()
		for laser in self.lasers:
			laser.move(vel)
			if laser.off_screen(HEIGHT):
				self.lasers.remove(laser)
			else:
				for obj in objs:
					if laser.collision(obj):
						objs.remove(obj)
						if laser in self.lasers:
							self.lasers.remove(laser)
		
	def draw(self, window):
		super().draw(window)
		self.healthbar(window)
	
	def healthbar(self, window):
		pygame.draw.rect(window, (255,0,0), (self.x, self.y + self.ship_img.get_height() + 10, self.ship_img.get_width(), 10))
		pygame.draw.rect(window, (0,255,0), (self.x, self.y + self.ship_img.get_height() + 10, self.ship_img.get_width() * (self.health/self.max_health), 10))

# Class Enemy inherits from ship
class BlueEnemy(Ship):
	def __init__(self, x, y, color, health=100):
		super().__init__(x, y, health)
		self.ship_img, self.laser_img = BLUE_SPACE_SHIP, BLUE_LASER
		self.mask = pygame.mask.from_surface(self.ship_img)
	
	def move(self, vel):
		self.y += vel
		
	def blue_shoot(self):
		if self.cool_down_counter == 0: 
			laser1 = Laser(self.x-20, self.y, self.laser_img)
			self.lasers.append(laser1)
			self.cool_down_counter = 1

	def green_shoot(self):
		if self.cool_down_counter == 0: 
			laser2 = Laser(self.x-20, self.y, self.laser_img)
			self.lasers.append(laser2)
			self.cool_down_counter = 1
			
	def purple_shoot(self):
		if self.cool_down_counter == 0: 
			laser3 = Laser(self.x-20, self.y, self.laser_img)
			self.lasers.append(laser3)
			self.cool_down_counter = 1

	def white_shoot(self):
		if self.cool_down_counter == 0: 
			laser3 = Laser(self.x-20, self.y, self.laser_img)
			self.lasers.append(laser4)
			self.cool_down_counter = 1

class GreenEnemy(Ship):
	def __init__(self, x, y, color, health=100):
		super().__init__(x, y, health)
		self.ship_img, self.laser_img = GREEN_SPACE_SHIP, GREEN_LASER
		self.mask = pygame.mask.from_surface(self.ship_img)
	
	def move(self, vel):
		self.y += vel
	"""	
	def blue_shoot(self):
		if self.cool_down_counter == 0: 
			laser1 = Laser(self.x-20, self.y, self.laser_img)
			self.lasers.append(laser1)
			self.cool_down_counter = 1
	"""	
	def green_shoot(self):
		if self.cool_down_counter == 0: 
			laser2 = Laser(self.x-20, self.y, self.laser_img)
			self.lasers.append(laser2)
			self.cool_down_counter = 1
	"""		
	def purple_shoot(self):
		if self.cool_down_counter == 0: 
			laser3 = Laser(self.x-20, self.y, self.laser_img)
			self.lasers.append(laser3)
			self.cool_down_counter = 1

	def white_shoot(self):
		if self.cool_down_counter == 0: 
			laser3 = Laser(self.x-20, self.y, self.laser_img)
			self.lasers.append(laser4)
			self.cool_down_counter = 1
	"""
class PurpleEnemy(Ship):
	def __init__(self, x, y, color, health=100):
		super().__init__(x, y, health)
		self.ship_img, self.laser_img = PURPLE_SPACE_SHIP, PURPLE_LASER
		self.mask = pygame.mask.from_surface(self.ship_img)
	
	def move(self, vel):
		self.y += vel
		
	def blue_shoot(self):
		if self.cool_down_counter == 0: 
			laser1 = Laser(self.x-20, self.y, self.laser_img)
			self.lasers.append(laser1)
			self.cool_down_counter = 1

	def green_shoot(self):
		if self.cool_down_counter == 0: 
			laser2 = Laser(self.x-20, self.y, self.laser_img)
			self.lasers.append(laser2)
			self.cool_down_counter = 1
			
	def purple_shoot(self):
		if self.cool_down_counter == 0: 
			laser3 = Laser(self.x-20, self.y, self.laser_img)
			self.lasers.append(laser3)
			self.cool_down_counter = 1

	def white_shoot(self):
		if self.cool_down_counter == 0: 
			laser3 = Laser(self.x-20, self.y, self.laser_img)
			self.lasers.append(laser4)
			self.cool_down_counter = 1

class WhiteEnemy(Ship):
	def __init__(self, x, y, color, health=100):
		super().__init__(x, y, health)
		self.ship_img, self.laser_img = WHITE_SPACE_SHIP, WHITE_LASER
		self.mask = pygame.mask.from_surface(self.ship_img)
	
	def move(self, vel):
		self.y += vel
		
	def blue_shoot(self):
		if self.cool_down_counter == 0: 
			laser1 = Laser(self.x-20, self.y, self.laser_img)
			self.lasers.append(laser1)
			self.cool_down_counter = 1

	def green_shoot(self):
		if self.cool_down_counter == 0: 
			laser2 = Laser(self.x-20, self.y, self.laser_img)
			self.lasers.append(laser2)
			self.cool_down_counter = 1
			
	def purple_shoot(self):
		if self.cool_down_counter == 0: 
			laser3 = Laser(self.x-20, self.y, self.laser_img)
			self.lasers.append(laser3)
			self.cool_down_counter = 1

	def white_shoot(self):
		if self.cool_down_counter == 0: 
			laser3 = Laser(self.x-20, self.y, self.laser_img)
			self.lasers.append(laser4)
			self.cool_down_counter = 1


# Collide
def collide(obj1, obj2):
	offset_x = obj2.x - obj1.x
	offset_y = obj2.y - obj1.y
	return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None

# Main loop
def main():
	run = True
	FPS = 60
	level = 1
	lives = 5
	main_font = pygame.font.SysFont("comicsans", 30)
	lost_font = pygame.font.SysFont("comicsans", 60)
	
	enemies = []
	wave_length = 5
	enemy_vel = 1
	
	player_vel = 5
	laser_vel = 5
	
	player = Player(300, 600)
	
	clock = pygame.time.Clock()

	lost = False
	lost_count = 0

	def redraw_window():
		WIN.blit(BG, (0,0))
		#draw text
		lives_label = main_font.render(f"Lives: {lives}", 1, (255,255,255))
		level_label = main_font.render(f"Level: {level}", 1, (255,255,255))
		
		WIN.blit(lives_label, (10, 10))
		WIN.blit(level_label, (WIDTH - level_label.get_width() - 10, 10))
		
		for enemy in enemies:
			enemy.draw(WIN)
		
		player.draw(WIN)
		
		if lost:
			lost_label = lost_font.render("¡Perdiste!", 1, (255,255,255))
			WIN.blit(lost_label, (WIDTH/2 - lost_label.get_width()/2, 350))
			
		pygame.display.update()
	
	while run: 
		clock.tick(FPS)
		redraw_window()
	
		if lives <= 0 or player.health <= 0: 
			lost = True
			lost_count += 1
		
		if lost:
			if lost_count > FPS * 3: 
				run = False
			else:
				continue
		
		if len(enemies) == 0:
			level += 1
			wave_length += 5
			for i in range(1):
				enemy1 = BlueEnemy(random.randrange(50, WIDTH-100), random.randrange(-1500, -100), "blue")
				enemies.append(enemy1)
				enemy2 = GreenEnemy(random.randrange(50, WIDTH-100), random.randrange(-1500, -100), "green")
				enemies.append(enemy2)
				enemy3 = PurpleEnemy(random.randrange(50, WIDTH-100), random.randrange(-1500, -100), "purple")
				enemies.append(enemy3)
				enemy4 = WhiteEnemy(random.randrange(50, WIDTH-100), random.randrange(-1500, -100), "white")
				enemies.append(enemy4)
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit()
		
		keys = pygame.key.get_pressed()
		if keys[pygame.K_LEFT] and player.x - player_vel > 0: #left
			player.x -= player_vel
		if keys[pygame.K_RIGHT] and player.x + player_vel + 50 < WIDTH: # right
			player.x += player_vel
		if keys[pygame.K_UP] and player.y - player_vel > 0: # up
			player.y -= player_vel
		if keys[pygame.K_DOWN] and player.y + player_vel + 50 < HEIGHT: # down
			player.y += player_vel 
		if keys[pygame.K_a]: # blue missile
			player.blue_shoot()
		if keys[pygame.K_s]: # green missile
			player.green_shoot()
		if keys[pygame.K_d]: # purple missile
			player.purple_shoot()
		if keys[pygame.K_f]: # white missile
			player.white_shoot()

	
		
		for enemy in enemies[:]:
			enemy.move(enemy_vel)
			enemy.move_lasers(laser_vel, player)
			
			if random.randrange(0, 2*60) == 1:
				enemy.blue_shoot()
				enemy.green_shoot()
				enemy.purple_shoot()
				enemy.white_shoot()
				
			if collide(enemy, player):
				player.health -= 10
				enemies.remove(enemy)
			elif enemy.y + enemy.get_height() > HEIGHT:
				lives -= 1
				enemies.remove(enemy)
		
		player.move_lasers(-laser_vel, enemies)
		
def main_menu():
	title_font = pygame.font.SysFont("comicsans", 20)
	run = True
	while run: 
		WIN.blit(BG, (0,0))
		title_label = title_font.render("Presiona el ratón para comenzar...", 1, (255,255,255))
		WIN.blit(title_label, (WIDTH/2 - title_label.get_width()/2, 50))
		pygame.display.update()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False 
			if event.type == pygame.MOUSEBUTTONDOWN:
				main()
	pygame.quit()
		
main_menu() 
