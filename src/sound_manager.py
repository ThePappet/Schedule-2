import pygame
import time
from config import PRE_LESSON_SOUND, START_LESSON_SOUND, CLICK_SOUND

# Инициализация pygame mixer
pygame.mixer.init()

def play_sound(file_path):
    try:
        sound = pygame.mixer.Sound(file_path)
        sound.play()
        # Ждем завершения воспроизведения
        while pygame.mixer.get_busy():
            time.sleep(0.1)
    except Exception as e:
        print(f"Ошибка воспроизведения: {e}")

def play_pre_bell():
    play_sound(PRE_LESSON_SOUND)

def play_start_bell():
    play_sound(START_LESSON_SOUND)

def play_click():
    play_sound(CLICK_SOUND)

play_pre_bell()
play_pre_bell()