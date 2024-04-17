from gtts import gTTS
import os

file = open("texto.txt", "r").read().replace("\n", " ")

language = "es-es"

speech = gTTS(text = str(file), lang = language, slow = False)

speech.save("texto_textazo.mp3")

os.system("start texto_textazo.mp3")

