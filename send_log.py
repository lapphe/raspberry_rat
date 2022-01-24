#Hannah Lapp
#https://github.com/lapphe/raspberry_rat

#This script will email an attachment containing the ip address to the specificed email address

#Note: before running this script, you will need to make sure your email account allows thrid party access
#for gmail, see more info here: https://support.google.com/accounts/answer/3466521?hl=en

from picamera import PiCamera
from time import sleep
import os
import subprocess
from datetime import datetime
import logging
import glob

this_pi = 'XX'  #enter the name/number of this pi computer here (helpful if you have multiple pis)

log = glob.glob('/home/pi/Documents/Logs/*.txt')
log_file = '\n'.join(log)

today = datetime.now()
d1 = today.strftime("%m_%d_%Y")

name = this_pi + '_' +'_'+ d1
file = name + '.h264'
path = '/home/pi/Videos/' + file
file2 = name + '.mp4'
path2 = '/home/pi/Videos/' + file2

print("Emailing log file...")

email_user = 'XXXXX@gmail.com' #enter your email address here
email_password = '123XYZ' #enter your email pasword here
email_send = 'XXXXX@gmail.com' #enter your email address again here
subject = this_pi + '_' +'_'+ d1
body = 'Recording:' + name

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

msg = MIMEMultipart()
msg['From'] = email_user
msg['To'] = email_send
msg['Subject'] = subject

msg = MIMEMultipart()
msg['From'] = email_user
msg['To'] = email_send
msg['Subject'] = subject

msg.attach(MIMEText(body,'plain'))

filename = log_file
attachment = open(filename,'rb')

part = MIMEBase('application','octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition',"attachment; filename= "+filename)

msg.attach(part)
text = msg.as_string()
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(email_user,email_password)
try:
    server.sendmail(email_user,email_send,text)
    server.quit()
except:
    logging.exception("Email failed")
    raise

print('Done')
