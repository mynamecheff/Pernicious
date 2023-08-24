import os
import platform
import psutil
import GPUtil as GPU
from screeninfo import get_monitors
import locale
from PIL import ImageGrab
import cv2

#hardware
print("Machine Name:", platform.node())
print("OS Version:", platform.platform())
print("Processor Count:", os.cpu_count())
print("System Directory:", os.path.abspath(os.sep))
print("User Domain Name:", os.environ.get('USERDOMAIN'))
print("User Interactive:", os.environ.get('USERINTERACTIVE'))
print("User Name:", os.environ.get('USERNAME'))
print()
#user/hostname
print("Current Username:", os.getlogin())
print("Current Hostname:", platform.node())

print()
# CPU
print("CPU Information:")
cpu_name = platform.processor()
cpu_cores = psutil.cpu_count(logical=False)
cpu_threads = psutil.cpu_count(logical=True)
print("CPU Name:", cpu_name)
print("CPU Cores:", cpu_cores)
print("CPU Threads:", cpu_threads)
print()
# GPU
print("\nGPU Information:")
gpus = GPU.getGPUs()
for gpu in gpus:
    print("GPU Name:", gpu.name)
    print("GPU Driver:", gpu.driver)
    print("GPU Memory Total:", round(gpu.memoryTotal / 1024, 2), "MB")
    print("GPU Memory Free:", round(gpu.memoryFree / 1024, 2), "MB")
    print("GPU Memory Used:", round(gpu.memoryUsed / 1024, 2), "MB")
    print("GPU GPU ID:", gpu.id)
print()
# RAM
print("\nRAM Information:")
ram_info = psutil.virtual_memory()
total_physical_memory_gb = ram_info.total / (1024 ** 3)
print("Total Physical Memory:", round(total_physical_memory_gb, 2), "GB")
print()
# battery
battery = psutil.sensors_battery()
if battery is not None:
    battery_status = "Charging" if battery.power_plugged else "Discharging"
    estimated_charge_remaining = battery.percent
    estimated_run_time = battery.secsleft / 60 if battery.secsleft >= 0 else "N/A"

    print("Battery Status:", battery_status)
    print("Estimated Charge Remaining:", estimated_charge_remaining, "%")
    print("Estimated Run Time:", estimated_run_time, "minutes")

print()
# screen info
monitors = get_monitors()
if monitors:
    primary_monitor = monitors[0]
    screen_width = primary_monitor.width
    screen_height = primary_monitor.height

    print("Screen Resolution:", screen_width, "x", screen_height)
print()
# OS language
default_language = locale.getdefaultlocale()[0]
print("Default Language:", default_language)

print()

#configurations
print("System Configuration Info:\n")
print("Boot Device:", os.getenv('SystemDrive'))
print("System Directory:", os.path.abspath(os.path.join(os.getenv('SystemRoot'), 'system32')))
print("Windows Directory:", os.getenv('SystemRoot'))

print()

# Capture the screenshot
screenshot = ImageGrab.grab()

# Save the screenshot
screenshot.save("desktop_screenshot.png", "PNG")
print("Desktop screenshot saved")

print()

# Initialize the webcam
cap = cv2.VideoCapture(0)

# Check if the webcam is opened successfully
if not cap.isOpened():
    print("No webcam found.")
else:
    # Capture a frame
    ret, frame = cap.read()

    if ret:
        # Save the frame as an image
        cv2.imwrite("webcam_screenshot.jpg", frame)
        print("Webcam screenshot saved")
    else:
        print("Failed to capture frame")

    # Release the webcam
    cap.release()