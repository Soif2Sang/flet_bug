import sys
import shutil
import os
from datetime import datetime

# Get the input argument
global_input = sys.argv[1] if len(sys.argv) > 1 else None

# Modify the current_date based on the input
if global_input is None:
    current_date = datetime.now().strftime("%Y-%m-%d")
else:
    current_date = "-br-" + datetime.now().strftime("%Y-%m-%d")

new_filename = f".\\auth compiled\\test environnement\\bot_executable_{current_date}\\bot-{current_date}.exe"

os.makedirs(f".\\auth compiled\\test environnement\\bot_executable_{current_date}", exist_ok=True)

shutil.move(".\\Bot.exe", new_filename)
shutil.copytree(".\\resources", f".\\auth compiled\\test environnement\\bot_executable_{current_date}\\resources", dirs_exist_ok=True)
shutil.copytree(".\\assets", f".\\auth compiled\\test environnement\\bot_executable_{current_date}\\assets", dirs_exist_ok=True)
