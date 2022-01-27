#Hannah Lapp
#https://github.com/lapphe/raspberry_rat

# This script will upload all videos in the Videos folder to the specified cloud location
# see rclone set up instructions

rclone_config = 'your_rclone_here' #edit to specify your rclone configurated cloud storage location

import os
import subprocess

upload = "rclone move /home/pi/Videos " + rclone_config + " --contimeout=4h"
os.system(upload)

