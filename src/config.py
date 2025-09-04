import json
import os

SCHEDULE_FILE = "data/schedule.json"
PRE_LESSON_SOUND = "sounds/pre_bell.wav"
START_LESSON_SOUND = "sounds/start_bell.wav"
CLICK_SOUND = "sound/click.wav"
PRE_LESSON_MINUTES = 5
CHECK_INTERVAL = 60
LANGUAGE = "ru"

CONFIG_FILE = "config.json"

def load_config():
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
                config_data = json.load(f)
            
            globals().update(config_data)
            print("Настройки загружены из config.json")
            
        except Exception as e:
            print(f"Ошибка загрузки конфига: {e}. Использую значения по умолчанию")
    else:
        print("Файл конфига не найден. Использую значения по умолчанию")
        save_config()

def save_config():
    config_data = {
        'SCHEDULE_FILE': SCHEDULE_FILE,
        'PRE_LESSON_SOUND': PRE_LESSON_SOUND,
        'START_LESSON_SOUND': START_LESSON_SOUND,
        'PRE_LESSON_MINUTES': PRE_LESSON_MINUTES,
        'CLICK_SOUND' : CLICK_SOUND,
        'CHECK_INTERVAL': CHECK_INTERVAL,
        'LANGUAGE': LANGUAGE
    }
    
    try:
        with open(CONFIG_FILE, 'w', encoding='utf-8') as f:
            json.dump(config_data, f, indent=2, ensure_ascii=False)
        print("Настройки сохранены в config.json")
    except Exception as e:
        print(f"Ошибка сохранения конфига: {e}")

def update_config(setting_name, new_value):
    global SCHEDULE_FILE, PRE_LESSON_SOUND, START_LESSON_SOUND, CLICK_SOUND
    global PRE_LESSON_MINUTES, CHECK_INTERVAL, LANGUAGE
    
    if setting_name in globals():
        globals()[setting_name] = new_value
        save_config()
        print(f"Настройка {setting_name} изменена на {new_value}")
    else:
        print(f"Настройка {setting_name} не найдена")

load_config()