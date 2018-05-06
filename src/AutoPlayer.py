from login import Loginer
from video import video
import os

if(os.path.exists("user.conf")==False):
    print("user.conf不存在")
    os.system("pause")
f=open('user.conf','r')
username=''
password=''
course=''
chapter=''
f.readline()
username=f.readline().strip('\n')
f.readline()
password=f.readline().strip('\n')
f.readline()
course=f.readline().strip('\n')
f.readline()
chapter=f.readline().strip('\n')
f.readline()
driverpath=f.readline().strip('\n')
f.close()
log=Loginer()
log.login(username,password)
log.findcourse(course)
if(log.courseurl is not ''):
    video= video()
    video.Input(log.courseurl,log.cookielist,driverpath)
    video.Read(chapter)
    print("You have finished!Please thank coder wangzw and give him some money.")
os.system("pause")
