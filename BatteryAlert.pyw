import psutil
import winsound
import tkinter as tk
from tkinter import messagebox
import time
import ctypes
import os

def force_foreground():
    # Allow this process to bring windows to the foreground
    user32 = ctypes.windll.user32
    current_pid = os.getpid()
    user32.AllowSetForegroundWindow(current_pid)
    hwnd = user32.GetForegroundWindow()
    user32.SetForegroundWindow(hwnd)

def show_message(title, message, sound_freq):
    winsound.Beep(sound_freq, 1000)

    # Force popup to come in front even if startup background
    force_foreground()

    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo(title, message)
    root.destroy()

def battery_monitor():
    already_alerted_low = False
    already_alerted_full = False

    while True:
        battery = psutil.sensors_battery()
        if battery is None:
            break

        percent = battery.percent
        plugged = battery.power_plugged

        if percent <= 23 and not plugged:
            if not already_alerted_low:
                show_message("Battery Alert", f"⚠ Battery Low: {percent}%", 1000)
                already_alerted_low = True
                already_alerted_full = False
        elif percent >= 88 and plugged:
            if not already_alerted_full:
                show_message("Battery Alert", f"✔ Battery High: {percent}%", 1500)
                already_alerted_full = True
                already_alerted_low = False
        else:
            already_alerted_low = False
            already_alerted_full = False

        time.sleep(120)

battery_monitor()
