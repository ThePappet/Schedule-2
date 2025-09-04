import tkinter as tk
from tkinter import ttk
import threading
import time
from config import CHECK_INTERVAL
from sound_manager import play_click

class ScheduleApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Расписание уроков")
        self.root.geometry("300x240")
        self.root.resizable(False, False)
        
        self.is_running = False
        self.scheduler_thread = None
        
        self.setup_ui()
        
    def setup_ui(self):
        style = ttk.Style()
        style.configure('TButton', font=('Arial', 12), padding=10)
        
        main_frame = ttk.Frame(self.root, padding=20)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        self.start_stop_button = ttk.Button(
            main_frame, 
            text="Запуск", 
            command=self.toggle_scheduler,
            style='TButton'
        )
        self.start_stop_button.pack(pady=10, fill=tk.X)
        
        schedule_button = ttk.Button(
            main_frame,
            text="Расписание",
            command=self.open_schedule,
            style='TButton'
        )
        schedule_button.pack(pady=10, fill=tk.X)
        
        settings_button = ttk.Button(
            main_frame,
            text="Настройки",
            command=self.open_settings,
            style='TButton'
        )
        settings_button.pack(pady=10, fill=tk.X)
        
        self.status_var = tk.StringVar(value="Готов к работе")
        status_bar = ttk.Label(
            self.root, 
            textvariable=self.status_var, 
            relief=tk.SUNKEN, 
            anchor=tk.W
        )
        status_bar.pack(side=tk.BOTTOM, fill=tk.X)
    
    def toggle_scheduler(self):
        if not self.is_running:
            self.start_scheduler()
        else:
            self.stop_scheduler()
    
    def start_scheduler(self):
        self.is_running = True
        self.start_stop_button.config(text="Стоп")
        self.status_var.set("Работает...")
        
        self.scheduler_thread = threading.Thread(target=self.scheduler_loop, daemon=True)
        self.scheduler_thread.start()
        
        print("Планировщик запущен")
    
    def stop_scheduler(self):
        self.is_running = False
        self.start_stop_button.config(text="Запуск")
        self.status_var.set("Остановлено")
        
        print("Планировщик остановлен")
    
    def scheduler_loop(self):
        while self.is_running:
            current_time = time.strftime("%H:%M:%S")
            print(f"[{current_time}] Проверяю расписание...")
            
            self.check_schedule()
            
            for _ in range(CHECK_INTERVAL):
                if not self.is_running:
                    return
                time.sleep(1)
    
    def check_schedule(self):
        pass
    
    def open_schedule(self):
        print("Открываю окно расписания")
        
    def open_settings(self):
        print("Открываю окно настроек")
    
    def on_closing(self):
        self.stop_scheduler()
        self.root.destroy()

def main():
    root = tk.Tk()
    app = ScheduleApp(root)
    
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    
    root.eval('tk::PlaceWindow . center')
    
    root.mainloop()

if __name__ == "__main__":
    main()