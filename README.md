BatteryAlertSystem

This Python script automatically monitors your laptop battery level and shows alerts when needed.

Key Features
- Alerts when battery is at or below 23 percent and charger is unplugged
- Alerts when battery is at or above 88 percent and charger is plugged in
- Runs silently in the background and checks the battery every 2 minutes
- Can be added to the Windows startup folder for automatic launch at system startup

Requirements
Python 3.x
psutil module
tkinter and winsound (these are included with Python on Windows)

To install psutil, use the following command:
pip install psutil

Usage
1. Save the script as BatteryGuard.pyw
2. Create a shortcut to the script
3. Place the shortcut in the Windows startup folder (Win + R, then type shell:startup)
4. The script will now start automatically with Windows and run in the background

Note
This script works only on Windows systems.
