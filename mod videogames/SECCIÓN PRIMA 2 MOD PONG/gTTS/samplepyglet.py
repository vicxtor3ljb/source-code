# Import the required module for text
# to speech conversion
from gtts import gTTS
from time import sleep
import os 
import pyglet
import winsound 

from pydub import AudioSegment

# Import pygame for playing the converted audio
import pygame

pygame.init()
pygame.display.set_mode((200,100))

# The text that you want to convert to audio
mytext = 'Welcome to geeksforgeeks!'

# Language in which you want to convert
language = 'en'

# Passing the text and language to the engine, 
# here we have marked slow=False. Which tells
# the module that the converted audio should
# have a high speed
myobj = gTTS(text=mytext, lang=language, slow=False)

# Saving the converted audio in a mp3 file named 
# welcome
myobj.save("welcome2.mp3")

sound = AudioSegment.from_mp3("welcome2.mp3")
sound.export("welcome2.wav", format="wav")

pygame.mixer.init()

pygame.mixer.music.load("welcome2.wav")

pygame.mixer.music.play(0)

winsound.PlaySound("welcome2.mp3", 1)

