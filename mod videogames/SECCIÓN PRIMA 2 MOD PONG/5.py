import pygame
import sys
import random
import pyttsx3
import speech_recognition as sr
import threading

# Initialize Pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong with Shopkeeper Dialogue")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Game objects
PADDLE_WIDTH, PADDLE_HEIGHT = 15, 90
BALL_SIZE = 15

# Paddle positions
left_paddle = pygame.Rect(50, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
right_paddle = pygame.Rect(WIDTH - 50 - PADDLE_WIDTH, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)

# Ball
ball = pygame.Rect(WIDTH//2 - BALL_SIZE//2, HEIGHT//2 - BALL_SIZE//2, BALL_SIZE, BALL_SIZE)
ball_speed_x = 7 * random.choice((1, -1))
ball_speed_y = 7 * random.choice((1, -1))

# Paddle speed
PADDLE_SPEED = 7

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Initialize speech recognizer
recognizer = sr.Recognizer()

# Dialogue
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

current_dialogue_index = 0
user_can_play = False

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

def dialogue_thread():
    global current_dialogue_index, user_can_play
    while current_dialogue_index < len(dialogue):
        if current_dialogue_index % 2 == 0:
            print(f"Shopkeeper: {dialogue[current_dialogue_index]}")
            speak(dialogue[current_dialogue_index])
            current_dialogue_index += 1
            user_can_play = True
        else:
            print(f"Expected response: {gemma_responses[current_dialogue_index//2]}")
            user_input = listen()
            if user_input == gemma_responses[current_dialogue_index//2].lower():
                current_dialogue_index += 1
                user_can_play = False
            else:
                print("That's not the expected response. Please try again.")

# Start dialogue thread
threading.Thread(target=dialogue_thread, daemon=True).start()

# Game loop
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the AI paddle (left)
    if left_paddle.top < ball.y:
        left_paddle.y += PADDLE_SPEED
    elif left_paddle.bottom > ball.y:
        left_paddle.y -= PADDLE_SPEED

    # Move the user paddle (right) only when allowed
    if user_can_play:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and right_paddle.top > 0:
            right_paddle.y -= PADDLE_SPEED
        if keys[pygame.K_DOWN] and right_paddle.bottom < HEIGHT:
            right_paddle.y += PADDLE_SPEED

    # Ball movement
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Ball collision with top and bottom
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed_y *= -1

    # Ball collision with paddles
    if ball.colliderect(left_paddle) or ball.colliderect(right_paddle):
        ball_speed_x *= -1

    # Ball out of bounds
    if ball.left <= 0 or ball.right >= WIDTH:
        ball.center = (WIDTH//2, HEIGHT//2)
        ball_speed_x *= random.choice((1, -1))
        ball_speed_y *= random.choice((1, -1))

    # Drawing
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, left_paddle)
    pygame.draw.rect(screen, WHITE, right_paddle)
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.draw.aaline(screen, WHITE, (WIDTH//2, 0), (WIDTH//2, HEIGHT))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
