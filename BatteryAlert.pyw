import psutil
import winsound
from tkinter import messagebox, Tk
import time

def show_alert(title, message, sound_freq):
    winsound.Beep(sound_freq, 1000)  # Beep for 1 second
    root = Tk()
    root.withdraw()
    messagebox.showinfo(title, message)

def battery_monitor():
    already_alerted_low = False
    already_alerted_full = False

    while True:
        battery = psutil.sensors_battery()
        if battery is None:
            break  # No battery found, exit script

        percent = battery.percent
        plugged = battery.power_plugged

        if percent <= 23 and not plugged:
            if not already_alerted_low:
                show_alert("Battery Low", f"Battery is at {percent}%. Please plug in the charger.", 1000)
                already_alerted_low = True
                already_alerted_full = False  # Reset full alert
        elif percent >= 88 and plugged:
            if not already_alerted_full:
                show_alert("Battery Full", f"Battery is at {percent}%. You may unplug the charger.", 1500)
                already_alerted_full = True
                already_alerted_low = False  # Reset low alert
        else:
            # Reset alerts if battery is in normal range
            already_alerted_low = False
            already_alerted_full = False

        # Wait for 2 minutes before next check
        time.sleep(120)

battery_monitor()
