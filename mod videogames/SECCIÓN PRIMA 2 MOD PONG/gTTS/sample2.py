from gtts import gTTS
from io import BytesIO

text = "I am the queen of Ireland."

lang = 'en'

# get audio from server
tts = gTTS(text=text, lang=lang)

# convert to file-like object
fp = BytesIO()
tts.write_to_fp(fp)
fp.seek(0)

# --- play it ---

import pygame

print('fp')

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(fp)
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)
