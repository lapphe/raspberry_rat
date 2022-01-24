#Hannah Lapp
#https://github.com/lapphe/raspberry_rat

#This script records a short 10 sec video and then deletes the video. This allows you to test the camera view.
#Run as many times as needed to get the right camera angle.
#If you do not have a display attached, comment out the last line of code. this will prevent the 
#recording form being deleted so you can see the recording in the "Videos" folder

this_pi = 'screen check' #used in name of video file created 
frame_rate= 30 #frames per sec for recording
brightness = 50 #integer from 1-100
contrast = 50 #integer from 1-100 
recording_length = 10 #number of secs. 1 hour = 3600 secs
s
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

camera.resolution=(1280,768) #adjust camera resolution as needed
camera.framerate= frame_rate
camera.brightness= brightness
camera.contrast= contrast
camera.start_preview() #this allows you to see camera view, but takes up whole screen while recording is in progress
sleep(2)
camera.annotate_text = this_pi + ' ' + d3
camera.annotate_background = False
camera.start_recording(path)
sleep(recording_length)
camera.stop_preview()
os.remove(path) # comment out this line to prevent the video from being deleted (e.g with remote access to pis)
