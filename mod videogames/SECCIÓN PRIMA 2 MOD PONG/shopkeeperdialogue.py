import pyttsx3
import speech_recognition as sr

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Initialize speech recognizer
recognizer = sr.Recognizer()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print("You said:", text)
            return text.lower()
        except:
            print("Sorry, I didn't catch that. Please try again.")
            return ""

dialogue = [
    "Hi. Can I help you?",
    "Let's see … Top Sounds, that's £1.99.",
    "Yes.",
    "Over there in the fridge. Is that everything?",
    "OK.",
    "That's £3.40, please.",
    "Thank you … and there's £1.60 change. Would you like a bag?",
    "Bye."
]

gemma_responses = [
    "Hello. How much is this magazine?",
    "OK, can I have the magazine and do you have a bottle of water?",
    "Have you got cold ones?",
    "I think so. Oh … and these sweets.",
    "How much is that?",
    "Here you are.",
    "No, it's fine, thanks. Bye."
]

print("Shopkeeper: Welcome to the voice-activated shopkeeper chatbot!")
print("Please respond as Gemma when prompted.")

for i, shopkeeper_line in enumerate(dialogue):
    print(f"Shopkeeper: {shopkeeper_line}")
    speak(shopkeeper_line)
    
    if i < len(gemma_responses):
        print(f"Expected response: {gemma_responses[i]}")
        user_input = listen()
        
        while user_input != gemma_responses[i].lower():
            print("That's not the expected response. Please try again.")
            user_input = listen()

print("Conversation ended. Thank you for using the shopkeeper chatbot!")
