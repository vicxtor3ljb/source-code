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
	draw_text("Read about four people who describe their experiences", text_font, purple, 0, 0)
	draw_text("living in the UK and for questions 1 to 4, choose the correct answer.", text_font, purple, 0, 10)
	
	draw_text("The British ways", text_font, purple, 0, 30)
	draw_text("Yuki from Japan", text_font, purple, 20, 40)
	draw_text("I like living in the UK.", text_font, purple, 40, 50)
	draw_text("People are always polite and friendly, which makes me feel welcome.", text_font, purple, 40, 60)
	draw_text("It often rains, but I don’t mind because I love the green parks.", text_font, purple, 40, 70)
	draw_text("I enjoy drinking tea with my friends and learning about British traditions.", text_font, purple, 40, 80)
	draw_text("British food is different, but I like it. I sometimes miss Japanese food.", text_font, purple, 40, 90)
	
	draw_text("Carlos from Spain", text_font, purple, 20, 110)
	draw_text("In the UK, people drink tea many times a day, which is interesting to me.", text_font, purple, 40, 120)
	draw_text("I often see them queuing for everything, and I think it’s very polite. ", text_font, purple, 40, 130)
	draw_text("It is sometimes cold, and it often rains. I miss the sun from Spain.", text_font, purple, 40, 140)
	draw_text("But in the UK, there are beautiful parks and green countryside.", text_font, purple, 40, 150)
	draw_text("The pubs are nice places to go with friends.", text_font, purple, 40, 160)
	
	draw_text("Anna from Poland", text_font, purple, 20, 180)
	draw_text("I like British customs very much. ", text_font, purple, 40, 190)
	draw_text("People say ‘please’ and ‘thank you’ all the time, which is very polite.", text_font, purple, 40, 200)
	draw_text("It rains a lot in the UK, and everyone has an umbrella. ", text_font, purple, 40, 210)
	draw_text("I enjoy visiting the museums, which are usually free.", text_font, purple, 40, 220)
	draw_text("I’m not a fan of the food here, but the old buildings and the history are very interesting.", text_font, purple, 40, 230)
	
	draw_text("Ahmed from Egypt", text_font, purple, 20, 240)
	draw_text("In many countries, people are often late,", text_font, purple, 40, 250)
	draw_text("but in the UK, people are always on time, which is good.", text_font, purple, 40, 260)
	draw_text("They drink tea very often. I also drink a lot of tea.", text_font, purple, 40, 270)
	draw_text("It is usually cold, but the houses are nice and warm.", text_font, purple, 40, 280)
	draw_text("I sometimes miss the nice weather of my country.", text_font, purple, 40, 290)
	
	
	# CORRECT ANSWER: "A)" EQUALS BLACK APPLE
	draw_text("1) What does Yuki like?", text_font, white, 0, 350)
	draw_text("a) Living in the UK.", text_font, white, 0, 360)
	draw_text("b) Living in Spain.", text_font, white, 0, 370)
	draw_text("b) Living in Poland.", text_font, white, 0, 380)
	draw_text("b) Living in Egypt.", text_font, white, 0, 390)
	
	
	# CORRECT ANSWER: "B)" EQUALS RED APPLE
	draw_text("2) What does Carlos miss?", text_font, red, 0, 410)
	draw_text("a) The sun from Japan.", text_font, red, 0, 420)
	draw_text("b) The sun from Spain.", text_font, red, 0, 430)
	draw_text("c) The sun from Poland.", text_font, red, 0, 440)
	draw_text("d) The sun from Egypt.", text_font, red, 0, 450)
	
	
	# CORRECT ANSWER: "C" EQUALS BLUE APPLE 
	draw_text("3) What is usually free in the UK?", text_font, green, 0, 470)
	draw_text("a) Visiting pubs.", text_font, green, 0, 480)
	draw_text("b) Getting an umbrella", text_font, green, 0, 490)
	draw_text("c) Visiting Museum.", text_font, green, 0, 500)
	draw_text("d) Queing for everything.", text_font, green, 0, 510)
	
	# CORRECT ANSWER: "D" EQUALS WHITE APPLE
	draw_text("4) Where is Ahmed from?", text_font, blue, 0, 530)
	draw_text("a) From Japan.", text_font, blue, 0, 540)
	draw_text("b) From Spain.", text_font, blue, 0, 550)
	draw_text("c) From Poland.", text_font, blue, 0, 560)
	draw_text("d) From Egypt.", text_font, blue, 0, 570)
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
			
	pygame.display.flip()
	
pygame.quit()

# https://test-english.com/reading/a1/the-british-ways-a1-english-reading-test/
"""
The British ways
Yuki from Japan
I like living in the UK. 
People are always polite and friendly, which makes me feel welcome. 
It often rains, but I don’t mind because I love the green parks. 
I enjoy drinking tea with my friends and learning about British traditions. 
British food is different, but I like it. I sometimes miss Japanese food.

Carlos from Spain
In the UK, people drink tea many times a day, which is interesting to me. 
I often see them queuing for everything, and I think it’s very polite. 
It is sometimes cold, and it often rains. I miss the sun from Spain. 
But in the UK, there are beautiful parks and green countryside. 
The pubs are nice places to go with friends.

Anna from Poland
I like British customs very much. 
People say ‘please’ and ‘thank you’ all the time, which is very polite. 
It rains a lot in the UK, and everyone has an umbrella. 
I enjoy visiting the museums, which are usually free. 
I’m not a fan of the food here, but the old buildings and the history are very interesting.

Ahmed from Egypt
In many countries, people are often late, 
but in the UK, people are always on time, which is good. 
They drink tea very often. I also drink a lot of tea. 
It is usually cold, but the houses are nice and warm. 
I sometimes miss the nice weather of my country.
"""
