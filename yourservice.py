from datetime import datetime
from time import sleep
import subprocess


seconds = 5
#seconds = 60 * 60 * 24  # 60 seconds x 60 minutes x 24 hours = 1-day

current_directory = "/home/ubuntu/repos/intro/service/"

while True:
    print(f"{datetime.now()}")
    
    # Execute external Linux command here
    #command = ["/home/ubuntu/pyenv/bin/python", "chatshot.py"]  # Replace this with your actual command and arguments
    #subprocess.run(command, check=True)  # This will wait for the command to complete
    
    sleep(seconds)
