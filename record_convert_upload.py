#Hannah Lapp
#https://github.com/lapphe/raspberry_rat

#this script records a video for the specified time, converts the video to mp4 format, then uploads the video to a specified  cloud location.
#It also creates a log file documenting each step in the script.

#-------------------------------------------------------------------------------------------------------
#Variables- update as needed
this_pi = 'XX' #Enter identifying info for recording here (e.g. subject ID). Appears in file name and annotation text
brightness = 50 #integer between 1-100. 50 is usually a good place to start
contrast = 50 #integer between 1-100. 50 is usually a good place to start
recording_length = 5 #number of secs. 1 hour = 3600 secs, 5 minutes = 300 secs
rclone_config = 'XXXX'
#---------------------------------------------------------------------------------------------------

from picamera import PiCamera
from time import sleep
import os
import subprocess
from datetime import datetime
import logging

today = datetime.now()
d1 = today.strftime("%d_%m_%Y")
d2 = today.strftime("%d_%m_%Y__%H_%M_%S")
d3 = today.strftime("%d_%m_%Y__%H_%M")

name = this_pi +'_'+ d3
file = name + '.h264'
path = '/home/pi/Videos/' + file
file2 = name + '.mp4'
path2 = '/home/pi/Videos/' + file2

camera = PiCamera()

log_file = '/home/pi/Documents/Logs/'+ name + '.txt'
logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')
logging.info(this_pi + ' ' + ' ' + d1)

print("Starting recording")
logging.info("Starting recording")

try:
    camera.resolution=(1280,768) #change to lower resolution to reduce video file size
    camera.framerate= 30
    camera.brightness= brightness
    camera.contrast= contrast
    camera.color_effects=(128,128) #comment this line out to record in color
    sleep(2)
    camera.annotate_text = this_pi + ' ' + d2
    camera.annotate_background = False
    camera.start_recording(path)
    sleep(recording_length)
    camera.stop_preview()
    camera.stop_recording()
    print("Finished recording")

except:
    logging.exception('Recording error found')
    new_log_file = '/home/pi/Documents/Logs/'+ 'FAILED_recording' + name + '.txt'
    os.rename(log_file, new_log_file)
    raise

print("Beginning coversion to MP4")
logging.info("Beginning coversion to MP4")
    
#Covert file to MP4 format. Requires command line subprocess
from subprocess import CalledProcessError
command = "MP4Box -fps 30 -add {} {}".format(path, path2)
try:
    output = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)
except subprocess.CalledProcessError as e:
    logging.info('MP4 conversion FAIL:\ncmd:{}\noutput:{}'.format(e.cmd, e.output))
    new_log_file = '/home/pi/Documents/Logs/'+ 'FAILED_mp4_conversion' + name + '.txt'
    os.rename(log_file, new_log_file)
    raise

print("Coversion finished... Starting MP4 upload")
logging.info("Conversion finished... Starting MP4 upload")

#upload MP4 to cloud
upload = "rclone move " + path2 + " " + rclone_config + " --contimeout=40m"
os.system (upload)

print("Removing H264 file")
logging.info("Removing H264 file")

try:
    os.remove(path)
    print("H264 video moved to trash")
    logging.info("Videos moved to trash")
except:
    logging.exception("H264 removal error")
    new_log_file = '/home/pi/Documents/Logs/'+ 'FAILED_delete' + name + '.txt'
    os.rename(log_file, new_log_file)
    raise

#print remaining files in Video directory
vids_list = os.listdir('/home/pi/Videos/')
vids = '\n'.join(vids_list)
print("Remaining videos:" + vids)
logging.info('Remaining videos:' + vids)


© 2022 GitHub, Inc.
Terms
Privacy
Security
Status
Docs
Contact GitHub
Pricing
API
Training
Blog
About
