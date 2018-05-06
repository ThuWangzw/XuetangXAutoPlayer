from login import Loginer
from video import video
import os
import json
if(os.path.exists("conf.json")==False):
    print("conf.json不存在")
    os.system("pause")
f=open('conf.json','r',encoding='gb2312')
conf=json.load(f)
print(conf)
f.close()
username=''
password=''
course=''
chapter=''
driverpath=''
username=conf['username']
password=conf['password']
course=conf['coursename']
chapter=conf['chapter']
driverpath=conf['chromedriver']
log=Loginer()
log.login(username,password)
log.findcourse(course)
if(log.courseurl is not ''):
    video= video()
    video.Input(log.courseurl,log.cookielist,driverpath)
    video.Read(chapter)
    print("You have finished!Please thank coder wangzw and give him some money.")
os.system("pause")
