import pyautogui
import time

# Simulate a key press and release
pyautogui.press('a')

# Simulate a mouse click
pyautogui.click()

# Simulate mouse movement
pyautogui.moveTo(100, 100, duration=1)  # Move to (100, 100) over 1 second

# Pause for a moment
time.sleep(1)
