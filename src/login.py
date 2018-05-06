from http import cookiejar
from urllib import request
from urllib import parse
import json
class Loginer:
    def __init__(self):
        self.data = {}
        self.courseurl=''
        self.cookielist=[]
        #cookie
        self.cookie=cookiejar.CookieJar()
        handler = request.HTTPCookieProcessor(self.cookie)
        self.opener = request.build_opener(handler)
         #header
        self.header = {}
        self.header['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
    def login(self,username,password):
        #data
        self.data={}
        self.data['username'] = username
        self.data['password'] = password
        self.data['remember'] = 'true'
        self.data = parse.urlencode(self.data).encode('utf-8')

        #request
        loginurl='http://www.xuetangx.com/v2/login_ajax'
        loginreq=request.Request(loginurl,self.data,self.header)
        self.opener.open(loginreq)
    def findcourse(self,coursename):
        findurl='http://www.xuetangx.com/api/web/courses/mycourses'
        findreq=request.Request(findurl,headers=self.header)
        res=self.opener.open(findreq)
        html=res.read().decode('utf-8')
        html=html.encode().decode('unicode-escape').encode().decode('utf-8')
        courses=json.loads(html,strict=False)
        courses=courses['results']
        iffound=False
        for course in courses:
            if(course['name'].find(coursename)>-1):
                self.courseurl='http://www.xuetangx.com/courses/'+course['id']+'/courseware'
                print('Have found the course.')
                iffound=True
                break
        if(iffound is not True):
            print('Sorry,this course isn\'t found')
        #save cookie
        self.TransferCookies()
    def TransferCookies(self):
        cookiestr=self.cookie.__str__()
        while(True):
            index=cookiestr.find('Cookie ')
            if(index<0):
                break
            cookiestr=cookiestr[index+7:]
            cookie={}
            key=''
            value=''
            domin=''
            keyindex=cookiestr.find('=')
            key=cookiestr[0:keyindex]
            valueindex=cookiestr.find(' ')
            value=cookiestr[keyindex+1:valueindex]
            dominindex=cookiestr.find('>')
            domin=cookiestr[valueindex+5:dominindex-1]
            cookie['name']=key
            cookie['value']=value
            cookie['domain']='www'+domin
            cookie['path']='/'
            cookie['httpOnly']=False
            self.cookielist.append(cookie)
