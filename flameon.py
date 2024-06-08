import time
import subprocess
import os

# Directory to save screenshots
save_directory = input("Directory to save to: ")

# Part of the filename specified by the user
filename_part = input("Enter the base part of the filename (e.g., 'screencap'): ")

# Screenshot interval specified by the user (in seconds)
try:
    screenshot_interval = int(input("Enter the interval between screenshots in seconds: "))
except ValueError:
    print("Invalid input for interval. Please enter an integer.")
    exit(1)

# Ensure the save directory exists
if not os.path.exists(save_directory):
    os.makedirs(save_directory)
    print(f"Created directory: {save_directory}")

while True:
    try:
        # Generate a unique filename based on the current timestamp
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        filename = f"{save_directory}/{filename_part}_{timestamp}.png"
        
        # Debug: Print the file path where the screenshot will be saved
        print(f"Saving screenshot to: {filename}")

        # Capture the screenshot using flameshot
        result = subprocess.run(["flameshot", "full", "-p", filename], capture_output=True, text=True)
        
        # Check if the command was successful
        if result.returncode == 0:
            print(f"Screenshot saved as {filename}")
        else:
            print(f"Failed to capture screenshot: {result.stderr}")
        
        # Wait for 9 seconds before taking the next screenshot
        time.sleep(screenshot_interval)
    except Exception as e:
        print(f"Exception occurred: {e}")
        break
