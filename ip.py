#Hannah Lapp
#https://github.com/lapphe/raspberry_rat

#This script will email an attachment containing the ip address to the specificed email address

#Note: before running this script, you will need to make sure your email account allows thrid party access
#for gmail, see more info here: https://support.google.com/accounts/answer/3466521?hl=en

from time import sleep
import os
import subprocess
from datetime import datetime
import logging

this_pi = 'XX' #enter the name/number of this pi computer here (helpful if you have multiple pis)

#setting up log file
log_file = '/home/pi/Documents/'+ this_pi + '_ip.txt'
logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')
ip_info = subprocess.check_output('ifconfig')
logging.info(ip_info)

email_user = 'XXXXX@gmail.com' #enter your email address here
email_password = '123XYZ' #enter your email pasword here
email_send = 'XXXXX@gmail.com' #enter your email address again here
subject = this_pi + '_ip'
body = "ip"

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

filename= log_file
attachment  =open(filename,'rb')

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
mydir = '/home/pi/Documents/'

for f in os.listdir(mydir):
    if not f.endswith(".txt"):
        continue
    os.remove(os.path.join(mydir,f))

print('Done')
