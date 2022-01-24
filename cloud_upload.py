#Hannah Lapp
#https://github.com/lapphe/raspberry_rat

# This script will upload all video in the Videos folder to the specified cloud location
#see rclone set up instructions

import os
import subprocess

os.system("rclone move /home/pi/Videos Cloud_location:directory/subdirectory --contimeout=4h")

# replace Cloud_location:directory/subdirectory with the information you set up using rclone
# e.g. Hannah_drive:recording_videos/day1
