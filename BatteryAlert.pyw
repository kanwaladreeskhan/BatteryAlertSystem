import psutil
import winsound
import tkinter as tk
import time

def show_overlay_message(message, sound_freq):
    winsound.Beep(sound_freq, 1000)  # Beep for 1 second

    overlay = tk.Tk()
    overlay.attributes('-topmost', True)  # Always on top
    overlay.overrideredirect(True)        # Remove borders
    overlay.geometry("+500+300")          # Position (adjust if needed)
    overlay.configure(bg='black')
    overlay.wm_attributes('-alpha', 0.8)  # Transparency

    label = tk.Label(overlay, text=message, fg='white', bg='black',
                     font=('Helvetica', 24, 'bold'))
    label.pack(ipadx=30, ipady=20)

    # Auto-close after 8 seconds
    overlay.after(8000, overlay.destroy)
    overlay.mainloop()

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
                show_overlay_message(f"⚠ Battery Low: {percent}%", 1000)
                already_alerted_low = True
                already_alerted_full = False  # Reset full alert
        elif percent >= 88 and plugged:
            if not already_alerted_full:
                show_overlay_message(f"✔ Battery Full: {percent}%", 1500)
                already_alerted_full = True
                already_alerted_low = False  # Reset low alert
        else:
            # Reset alerts if battery is in normal range
            already_alerted_low = False
            already_alerted_full = False

        # Wait for 2 minutes before next check
        time.sleep(120)

battery_monitor()
