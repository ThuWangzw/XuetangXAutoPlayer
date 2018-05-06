from selenium import webdriver
from  selenium.webdriver.support.ui import  WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
class video:
    def __init__(self):
        self.tagname=''
        self.browser=webdriver.Chrome('F:\chromedriver\chromedriver.exe')
    def Input(self,url,list):
        self.browser.get(url)
        for cookie in list:
            self.browser.add_cookie(cookie)
        self.browser.get(url)
    def Read(self,name):
        xpath='//h3[contains(@aria-label,"'+name+'")]'
        tar = self.browser.find_element_by_xpath(xpath)
        tar.click()
        tar=self.browser.find_element_by_css_selector("[class='chapter is-open']")
        tars = tar.find_elements_by_tag_name('li')
        i=0
        len=tars.__len__()
        for i in range(0,len):
            tars[i].click()
            self.browser.refresh()
            tar=self.browser.find_element_by_css_selector("[class='chapter is-open']")
            tars = tar.find_elements_by_tag_name('li')

            videolist=self.browser.find_element_by_xpath('//ol[@role="tablist"]').find_elements_by_tag_name('li')
            for videopage in videolist:
                videopage.click()
                #check if have video
                time.sleep(3)
                ifhave=self.browser.find_elements_by_tag_name('video')
                if(ifhave.__len__()==0):
                    continue
                #start
                video=WebDriverWait(self.browser,30,0.5).until(EC.presence_of_element_located((By.XPATH,"//video")))

                self.browser.execute_script("return arguments[0].play()",video)
                while(self.browser.execute_script("return arguments[0].ended;",video) is False):
                    True

