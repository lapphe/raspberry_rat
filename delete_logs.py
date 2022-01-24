#Hannah Lapp
#https://github.com/lapphe/raspberry_rat

#This script will delete previous log files from "Logs" folder
import os

mydir = '/home/pi/Documents/Logs/'

for f in os.listdir(mydir):
    if not f.endswith(".txt"):
        continue
    os.remove(os.path.join(mydir,f))
