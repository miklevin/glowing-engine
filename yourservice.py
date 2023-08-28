from datetime import datetime
from time import sleep
import subprocess


# seconds = 30
seconds = 60 * 5  # 5 minutes
#seconds = 60 * 60 * 24  # 60 seconds x 60 minutes x 24 hours = 1-day

current_directory = "/home/ubuntu/repos/intro/service/"

while True:
    print(f"{datetime.now()}")
    
    # Un-edit the below lines and change number of seconds above.
    
    command = ["/home/ubuntu/pyenv/bin/python", "chatshot.py"]  # Replace with your command.
    subprocess.run(command, cwd=current_directory, check=True)  # Runs command and returns to parent script.
    
    sleep(seconds)
