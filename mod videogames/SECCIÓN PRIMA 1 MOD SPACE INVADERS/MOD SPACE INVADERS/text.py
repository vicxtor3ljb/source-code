# text

# https://stackoverflow.com/questions/77578337/how-to-display-text-on-screen-with-tkinter

#import tkinter as tk

#ws = tk.Tk()
#ws.title('Questions')
#ws.overrideredirect(True)
#ws.wm_attributes('-transparentcolor','white')
#ws.config(bg="black")
#ws.config(bg='#D9D8D7')
#ws.geometry('700x300')

#label = tk.Label(text='Text on the screen', 
#		font=('Times', '50'), 
#		fg='black', 
#		bg='white', 
#		width=50)

#label.pack(padx=25, pady=25)

#ws.mainloop()

# https://www.kaggle.com/discussions/general/273188

#print("\033[1;31;40m This is red \n")

#print("\033[1;32;40m This is green \n")

#print("\033[1;34;40m This is blue \n")

#print("\033[1;37;40m This is white \n")


# https://www.geeksforgeeks.org/python-display-text-to-pygame-window/
# import pygame module in this program
#import pygame
 
# activate the pygame library
# initiate pygame and give permission
# to use pygame's functionality.
#pygame.init()
 
# define the RGB value for white,
#  green, blue colour .
#white = (255, 255, 255)
#green = (0, 255, 0)
#blue = (0, 0, 128)
#red = (255, 0, 0)
 
# assigning values to X and Y variable
#X = 400
#Y = 400
 
# create the display surface object
# of specific dimension..e(X, Y).
#display_surface = pygame.display.set_mode((X, Y))
 
# set the pygame window name
#pygame.display.set_caption('Show Text')
 
# create a font object.
# 1st parameter is the font file
# which is present in pygame.
# 2nd parameter is size of the font
#font = pygame.font.Font('freesansbold.ttf', 32)
 
# create a text surface object,
# on which text is drawn on it.
#text1 = font.render('This is white', True, white)
#text2 = font.render('This is green', True, green)
#text3 = font.render('This is blue', True, blue)
#text4 = font.render("This is red", True, red)


# create a rectangular object for the
# text surface object
#textRect1 = text1.get_rect()
#textRect2 = text2.get_rect()
#textRect3 = text3.get_rect()
#textRect4 = text4.get_rect()
 
# set the center of the rectangular object.
#textRect.center = (X // 2, Y // 2)
 
# infinite loop
#while True:
 
    # completely fill the surface object
    # with white color
#    display_surface.fill(white)
 
    # copying the text surface object
    # to the display surface object
    # at the center coordinate.
#   display_surface.blit(text1, textRect1)
#	display_surface.blit(text2, textRect2)
#	display_surface.blit(text3, textRect3)
#	display_surface.blit(text4, textRect4)
    
    # iterate over the list of Event objects
    
    # that was returned by pygame.event.get() method.
    
#    for event in pygame.event.get():
 
        # if event object type is QUIT
        # then quitting the pygame
        # and program both.
#        if event.type == pygame.QUIT:
 
            # deactivates the pygame library
#            pygame.quit()
 
            # quit the program.
#            quit()
 
        # Draws the surface object to the screen.
#        pygame.display.update()

# coding with Russ
# https://www.youtube.com/watch?v=ndtFoWWBAoE
import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
red = (255, 0, 0)
purple = (255, 0, 255)
grey = (200, 200, 200)
black = (0, 0, 0)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

text_font = pygame.font.SysFont("Arial", 10)

def draw_text(text, font, text_col, x, y):
	img = font.render(text, True, text_col)
	screen.blit(img, (x, y))

run = True
while run: 
	screen.fill((200, 200, 200))
	draw_text("Listen to the audio twice and choose the correct answer:", text_font, red, 0, 0)
	
	# CORRECT ANSWER: "A)" EQUALS BLUE SHIP
	draw_text("1) What does Jamie want for starter?", text_font, blue, 10, 20)
	draw_text("a) French onion soup.", text_font, blue, 20, 30)
	draw_text("b) Tomato salad.", text_font, blue, 20, 40)
	draw_text("b) Thai chicken.", text_font, blue, 20, 50)
	draw_text("b) Rice.", text_font, blue, 20, 60)
	
	
	# CORRECT ANSWER: "B)" EQUALS GREEN SHIP
	draw_text("2) What does Sally want for started?", text_font, green, 10, 80)
	draw_text("a) French onion soup.", text_font, green, 20, 90)
	draw_text("b) Tomato salad.", text_font, green, 20, 100)
	draw_text("c) Thai chicken.", text_font, green, 20, 110)
	draw_text("d) Rice.", text_font, green, 20, 120)
	
	
	# CORRECT ANSWER: "C" EQUALS PURPLE SHIP
	draw_text("3) How many tables do the customers want?", text_font, purple, 10, 140)
	draw_text("a) Two.", text_font, purple, 20, 150)
	draw_text("b) Three.", text_font, purple, 20, 160)
	draw_text("c) One.", text_font, purple, 20, 170)
	draw_text("d) Four.", text_font, purple, 20, 180)
	
	# CORRECT ANSWER: "D" EQUALS WHITE SHIP
	draw_text("4) What do Sally and Jamie want for main course?", text_font, white, 10, 200)
	draw_text("a) French onion soup.", text_font, white, 20, 210)
	draw_text("b) Tomato salad.", text_font, white, 20, 220)
	draw_text("c) French orange juice.", text_font, white, 20, 230)
	draw_text("d) Thai chicken and rice.", text_font, white, 20, 240)
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
			
	pygame.display.flip()
	
pygame.quit()

# tps://learnenglishteens.britishcouncil.org/skills/listening/a2-listening/eating-out
"""
Waiter: Hello.
Jamie: Hi. A table for two, please.
Waiter: Of course. Over here, please. Here’s the menu.
Sally: Thank you.
(pause)
Waiter: Are you ready to order?
Sally: Yes, we are.
Waiter: What would you like for your starter?
Jamie: I’d like French onion soup, please.
Sally: And I’ll have a tomato salad, please.
Waiter: And for your main course?
Jamie: Mmm, I’m not sure. I don’t know whether to have the steak or Thai chicken.
Sally: Oh, I’d like the Thai chicken and rice please.
Jamie: OK, me too.
Waiter: So that’s two Thai chicken and rice. What would you like to drink?
Jamie: I’ll have a fresh orange juice and ...
Sally: I’d like some mineral water, please.
Waiter: OK, thank you.
"""
