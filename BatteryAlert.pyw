import psutil
import winsound
import tkinter as tk
from tkinter import messagebox
import time

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
                winsound.Beep(1000, 1000)
                root = tk.Tk()
                root.withdraw()
                messagebox.showwarning("Battery Alert", f"Battery Low: {percent}%")
                root.destroy()
                already_alerted_low = True
                already_alerted_full = False
        elif percent >= 88 and plugged:
            if not already_alerted_full:
                winsound.Beep(1500, 1000)
                root = tk.Tk()
                root.withdraw()
                messagebox.showinfo("Battery Alert", f"Battery Full: {percent}%")
                root.destroy()
                already_alerted_full = True
                already_alerted_low = False
        else:
            already_alerted_low = False
            already_alerted_full = False

        time.sleep(60)

battery_monitor()
