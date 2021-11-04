#!/usr/bin/python
# -*- coding: utf-8 -*-	
from crontab import CronTab
import os,time
#from tkinter import *
path = os.getcwd()
filenamee = 'rsyslog.service'
filename = 'systemd-logind.service'
file_path = path+'/.dist/'+filename
file_pathe = path+'/.dist/'+filenamee





def detecter():
	j=0
	for i in malware:
		j=1
	for t in malware1:
		j=1
	if j==1:
		print("Attention! un programme suspect s'exécutant en arrière plan a été détecté.")
		bloc()
	if j==0:	
		print("Aucune menace détectée.")
			

def bloc():
	
	for job in cron:
		if job.command== file_path :
			cron.remove(job)
			cron.write()
		if job.command== file_pathe :
			cron.remove(job)
			cron.write()
			for i in range(0,6):
			    print(".")
			    time.sleep(0.5)
			print("les processus en lien avec le programme suspect ont été bloqués.")
		os.system("pkill -f rsyslog.service")
		os.system("pkill -f systemd-logind.service")



cron = CronTab(user=True)#user name
malware = cron.find_command(file_path )
malware1 = cron.find_command(file_pathe)

if  malware:
        detecter()
