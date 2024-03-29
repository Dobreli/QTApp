import datetime
import random
import time
import os
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PyQt5.QtCore import pyqtSignal,QObject,QRunnable,pyqtSlot
import sqlite3 as sql

class BrowserButton():
    def __init__(self,browser):
        self.browser = browser

    def nextPage(self):
        if WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.XPATH, "//ytcp-icon-button[@id='navigate-after']"))):
            self.browser.find_element(By.XPATH, " //ytcp-icon-button[@id='navigate-after']").click()
        else:
            raise Exception("Not Found: Next Page Button")
       
    def saveAndClose(self):
        if WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@class='close-button-area style-scope ytcp-uploads-dialog']//ytcp-icon-button[@id='close-button']"))):
            self.browser.find_element(By.XPATH, "//div[@class='close-button-area style-scope ytcp-uploads-dialog']//ytcp-icon-button[@id='close-button']").click()
        else:
            raise Exception("Not Found: Save and Close Button")

    def checkBox(self):
        if WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.XPATH, "//ytcp-checkbox-lit[@class='all-none-checkbox style-scope ytpp-self-certification-questionnaire']//div[@class='label style-scope ytcp-checkbox-lit']"))):
            self.browser.find_element(By.XPATH,"//ytcp-checkbox-lit[@class='all-none-checkbox style-scope ytpp-self-certification-questionnaire']//div[@class='label style-scope ytcp-checkbox-lit']").click()
        else:
            raise Exception("Not Found: Check Box Button")
        
    def nextButton(self):
        if WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.XPATH, "//ytcp-button[@id='next-button']"))):
            self.browser.find_element(By.XPATH, "//ytcp-button[@id='next-button']").click()
        else:
            raise Exception("Not Found: Next Button")

    def nextButton2(self):
        while True:
            try:
                if self.browser.find_element(By.XPATH, "//ytcp-button[@id='next-button']").get_attribute("aria-disabled") == "false":
                    if self.browser.find_element(By.XPATH, "//ytcp-button[@id='next-button']").get_attribute("hidden") == "true":
                        break
                    else:
                        self.nextButton()
            except:
                raise Exception("Not Found: Next Button")
    
    def planButton(self):
        if WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.XPATH, "//ytcp-button[@id='done-button']"))):
            self.browser.find_element(By.XPATH, "//ytcp-button[@id='done-button']").click()
        else:
            raise Exception("Not Found: Plan Button")

    def closeButton(self):
        if WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.XPATH, "//ytcp-button[@id='close-button']//div"))):
            self.browser.find_element(By.XPATH, "//ytcp-button[@id='close-button']//div").click()
        else:
            raise Exception("Not Found: Close Button")
    
    def moreShowButton(self):
        if WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.XPATH, "//ytcp-button[@id='toggle-button']"))):
            self.browser.find_element(By.XPATH, "//ytcp-button[@id='toggle-button']").click()
        else:
            raise Exception("Not Found: More Show Button")
    
    def sendAdsButton(self):
        if WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.XPATH, "//ytcp-button[@id='submit-questionnaire-button']"))):
            self.browser.find_element(By.XPATH, "//ytcp-button[@id='submit-questionnaire-button']").click()
        else:
            raise Exception("Not Found: Ads Send Button")
    
    def makeMoneyCheckBox(self):
        if WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.XPATH, "//ytcp-video-metadata-monetization//div[@id='child-input']"))):
            self.browser.find_element(By.XPATH, "//ytcp-video-metadata-monetization//div[@id='child-input']").click()
            if WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.XPATH, "//tp-yt-paper-radio-group//tp-yt-paper-radio-button[@id='radio-on']"))):
                self.browser.find_element(By.XPATH, "//tp-yt-paper-radio-group//tp-yt-paper-radio-button[@id='radio-on']").click()
                if WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.XPATH, "//ytcp-button[@id='save-button']"))):
                    self.browser.find_element(By.XPATH, "//ytcp-button[@id='save-button']").click()
                else:
                    raise Exception("Not Found: Make Money CheckBox Button -- 3 ")
            else:
                raise Exception("Not Found: Make Money CheckBox Button -- 2")
        else:
            raise Exception("Not Found: Make Money CheckBox Button -- 1")
    
    def selectPlanButtons(self):
        # while True:
        #     try:
        #         if WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//tp-yt-paper-radio-button[@id='schedule-radio-button']"))):
        #             browser.find_element(By.XPATH,"//tp-yt-paper-radio-button[@id='schedule-radio-button']").click()
        #             break
        #     except:
        #         # print("!!! Hata - 107 - Planlayın bulunamadı")
        #         continue
        if WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.XPATH, "//ytcp-icon-button[@id='second-container-expand-button']"))):
            self.browser.find_element(By.XPATH,"//ytcp-icon-button[@id='second-container-expand-button']").click()
            if WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.XPATH,"//ytcp-text-dropdown-trigger[@class='style-scope ytcp-datetime-picker']//div[@class='left-container style-scope ytcp-dropdown-trigger']"))):
                self.browser.find_element(By.XPATH,"//ytcp-text-dropdown-trigger[@class='style-scope ytcp-datetime-picker']//div[@class='left-container style-scope ytcp-dropdown-trigger']").click()
            else:
                raise Exception("Not Found: Plan Button -- 2")
        else:
            raise Exception("Not Found: Plan Button -- 1")

class BrowserSendInput():
    def __init__(self,browser) -> None:
        self.browser = browser
        
    def writeComment(self,shorts = True,com="comment "):
        if WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.XPATH,"//ytcp-video-description[@id='description-wrapper']//div[@id='textbox']"))):
            if shorts == False:
                self.browser.find_element(By.XPATH,"//ytcp-video-description[@id='description-wrapper']//div[@id='textbox']").send_keys(Keys.CONTROL + "a")
                self.browser.find_element(By.XPATH,"//ytcp-video-description[@id='description-wrapper']//div[@id='textbox']").send_keys(Keys.ARROW_LEFT)
                self.browser.find_element(By.XPATH,"//ytcp-video-description[@id='description-wrapper']//div[@id='textbox']").send_keys(com)
            else:
                self.browser.find_element(By.XPATH,"//ytcp-video-description[@id='description-wrapper']//div[@id='textbox']").send_keys(Keys.CONTROL + "a")
                self.browser.find_element(By.XPATH,"//ytcp-video-description[@id='description-wrapper']//div[@id='textbox']").send_keys(Keys.DELETE)
        else:
            raise Exception("Not Found: Comment Input Line")

    def writeHead(self,head="head"):
        if WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.XPATH,"(//div[@id='textbox'])[1]"))):
            self.browser.execute_script("arguments[0].innerHTML = '{}'".format(head),self.browser.find_element(By.XPATH,"(//div[@id='textbox'])[1]"))
            self.browser.find_element(By.XPATH,"(//div[@id='textbox'])[1]").send_keys(".")
            self.browser.find_element(By.XPATH,"(//div[@id='textbox'])[1]").send_keys(Keys.BACKSPACE)
            if self.browser.find_element(By.XPATH,"(//div[@id='textbox'])[1]").text != head:
                return self.writeHead(head)
        else:
            raise Exception("Not Found: Head Input Line")

    def writeTime(self, dtime="17:00"):
        if WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.XPATH, "//form[@class='style-scope ytcp-datetime-picker']//input"))):
            self.browser.find_element(By.XPATH,"//form[@class='style-scope ytcp-datetime-picker']//input").clear()
            self.browser.find_element(By.XPATH,"//form[@class='style-scope ytcp-datetime-picker']//input").send_keys(dtime)
            self.browser.find_element(By.XPATH,"//form[@class='style-scope ytcp-datetime-picker']//input").send_keys(Keys.ENTER)
        else:
            raise Exception("Not Found: Time Input Line")


    def writeDate(self, date="30 Eki 2024"):
        if WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.XPATH, "//form[@class='style-scope ytcp-date-picker']//input"))):
            self.browser.find_element(By.XPATH, "//form[@class='style-scope ytcp-date-picker']//input").clear()
            self.browser.find_element(By.XPATH, "//form[@class='style-scope ytcp-date-picker']//input").send_keys(date)
            self.browser.find_element(By.XPATH, "//form[@class='style-scope ytcp-date-picker']//input").send_keys(Keys.ENTER)
        else:
            raise Exception("Not Found: Date Input Line")
        
    def uploadPicture(self,fileloc):
        if WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@id='file-loader']"))):
            self.browser.find_element(By.XPATH, "//input[@id='file-loader']").send_keys(fileloc)
        else:
            raise Exception("Not Found: Picture Upload Input")

    def writeTag(self,taglist):
        if WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.XPATH, "//ytcp-free-text-chip-bar[@class='style-scope ytcp-video-metadata-editor-advanced']//input[@id='text-input']"))):
            self.browser.find_element(By.XPATH, "//ytcp-free-text-chip-bar[@class='style-scope ytcp-video-metadata-editor-advanced']//input[@id='text-input']").send_keys(taglist)
            self.browser.find_element(By.XPATH, "//ytcp-free-text-chip-bar[@class='style-scope ytcp-video-metadata-editor-advanced']//input[@id='text-input']").send_keys(Keys.ENTER)
        else:
            raise Exception("Not Found: Tag Input Line")

class ytPlanSignals(QObject):
    ytPlan_Log = pyqtSignal(str)
    ytPlan_Finish = pyqtSignal(dict)

class ytOtoPost(QRunnable):
    def __init__(self,data):
        super(ytOtoPost, self).__init__()
        self.signals = ytPlanSignals()

        self.BasePath = data["BasePath"]

        self.browser= ""
        self.BrowserUserDataLocation=""
        self.BrowserExeLocation=""

        self.cHeadList= []
        self.cCommentList = []
        self.TagList = []
        self.picFileList =[]

        #Browser
        self.BrowserType =str(data["BrowserType"])
        self.Language =str(data["Language"])
        self.YtStudioLink =data["link"]
        self.cMony = data["monyCheck"]
        
        # Post 
        self.PostType = str(data["PostType"])
        self.DayLimit = int(data["DayLimit"])
        self.PostLimit = int(data["PostLimit"])
        self.PerDay = int(data["PerDay"])
        self.PerMin = int(data["PerMin"])
        self.Datetime = self.convertDatetime(data["DateTime"])
        self.Datetime2 =  self.convertDatetime(data["DateTime"])
        self.cHead = data["Head"]
        self.cComment = data["Coment"]
        self.cTags = data["Tag"]
        self.cPic=data["Pic"]
        self.LimitControl = 0
        self.cHeadList=[]
        
        self.WaitPage = 3 
        self.VideoName =""
        self.VideoCellNo = 0
        self.Head ="" 
        self.PageTotalVideo =0
        self.TotalVideo = 0
        self.CompletedTotalVideo =0
        
    def browserDriver(self):       
        options = webdriver.ChromeOptions()
        options.headless = False
        options.binary_location = (rf"{self.BrowserExeLocation}")
        options.add_argument("--enable-chrome-browser-cloud-management")
        options.add_argument(rf"user-data-dir={self.BrowserUserDataLocation}")
        self.browser = webdriver.Chrome(options=options)

    def selectVideo(self):
        if WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.XPATH,"//a[@id='video-title']"))):
            self.VideoName = self.browser.find_element(By.XPATH, f"(//a[@id='video-title'])[{self.VideoCellNo}]").text
            self.convertVideoName(self.VideoName)
            self.browser.find_element(By.XPATH, f"(//a[@id='video-title'])[{self.VideoCellNo}]").click()
        else:
            raise Exception("Not Found: Video")
   
    def getTotalVideo(self):
        if WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.XPATH,"//span[@class='page-description style-scope ytcp-table-footer']"))):
            self.TotalVideo=int(self.browser.find_element(By.XPATH,"//span[@class='page-description style-scope ytcp-table-footer']").text.split("/")[1])
        else:
            raise Exception ("Not Found: Total Video Span")

    def getPageTotalVideo(self):
        if WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.XPATH,"(//span[@class='dropdown-trigger-text style-scope ytcp-text-dropdown-trigger'])[4]"))):
            self.PageTotalVideo=int(self.browser.find_element(By.XPATH,"(//span[@class='dropdown-trigger-text style-scope ytcp-text-dropdown-trigger'])[4]").text)
        else:
            raise Exception ("Not Found: Page Total Video Span")
    
    def getVideoCellNo(self):
        self.VideoCellNo +=1
        if self.VideoCellNo > self.PageTotalVideo:
            if  self.TotalVideo > self.CompletedTotalVideo:
                BrowserButton(self.browser).nextPage()
                time.sleep(self.WaitPage)
                self.VideoCellNo = 1
    """ 
        Convert and Another Process
    
    """
    def convertVideoName(self,videoname):
        try:
            videoname = videoname.split(" ")
            self.VideoName = f"{videoname[0]}"+" "+f"({videoname[1]})"
        except:
            raise Exception("Video Name Not Convert. Like a : 'videoname 1'")

    def getHead(self,c=10):
        reelslist =[]
        if "shorts" == self.PostType:
            for i in self.cHeadList:
                if "reels" in i or "shorts" in i:
                    reelslist.append(i[0])
            if type(self.cHeadList) != str:  
                while True:
                    head = random.choice(reelslist)
                    if len(self.cHeadList) == c + 1:
                        break
                    else:
                        if head not in self.cHeadList:
                            self.cHeadList.append(head)
                head = self.cHeadList[-1]
                self.cHeadList = self.cHeadList[1:]
                return head
        else:
            for head in self.cHeadList:
                if self.VideoName in head:
                    return head[0]
        return ""

    def getTagList(self):
        reelsList =[]
        nList =""
        normalList =[]
        for taglist in self.TagList:
            if "reels" in taglist or "shorts" in taglist:
                reelsList.append(taglist[0])
            elif self.VideoName in taglist:
                nList = taglist[0]
        if len(nList) !=0:
            for i in nList.split(","):
                normalList.append(f"{i},")
            return normalList
        else:
            return reelsList

    def PostLimitControl(self):
        if self.LimitControl < self.DayLimit+1:
            if self.LimitControl !=1:
                self.Datetime2 = self.timeAdd(self.Datetime2,self.PerMin)
            return [self.convertYtDate(self.Datetime2),self.convertYtTime(self.Datetime2)]
        else:
            self.LimitControl = 1
            self.Datetime = self.dateAdd(self.Datetime,self.PerDay)
            self.Datetime2 = self.Datetime
            return [self.convertYtDate(self.Datetime),self.convertYtTime(self.Datetime)]
   
    def convertDatetime(self,dt):
        d=dt.split(" ")[0]
        t=dt.split(" ")[1]
        hour=int(t.split(":")[0])
        minute=int(t.split(":")[1])
        day=int(d.split(".")[0])
        month=int(d.split(".")[1])
        year=int(d.split(".")[2])
        return datetime.datetime(hour=hour,minute=minute,year=year,day=day,month=month)

    def convertYtDate(self, dtime):
        mname = ["","Oca","Şub","Mar","Nis","May","Haz","Tem","Ağu","Eyl","Eki","Kas","Ara",]
        yt_date = f"{dtime.day} {mname[int(dtime.month)]} {dtime.year}"
        return yt_date
    
    def convertYtTime(self, time):
        yt_time = f"{time.hour}:{time.minute}"
        return yt_time

    def dateAdd(self, date, day=1):
        date = date + datetime.timedelta(days=day)
        return date
 
    def timeAdd(self,time,min=0):
        time = time + datetime.timedelta(minutes=int(min))
        return time
    
    def conDb(self):
        db_path = rf"{self.BasePath}\appdb.sqlite"
        if os.path.exists(db_path):
            return sql.connect(db_path)
        else:
            raise Exception ("Database Connect Error")
        
    def getDb(self):
        db = self.conDb()
        cursor = db.cursor()
        try:
            cursor.execute(f"SELECT Head, Secondid FROM Heads where Language={self.Language}")
            for i in cursor.fetchall():
                self.cHeadList.append(i)

            cursor.execute(f"SELECT Tag,Secondid FROM Tags where Language={self.Language}")
            for i in cursor.fetchall():
                self.TagList.append(i)
            
            cursor.execute(f"SELECT Comment FROM Comments where Language={self.Language}")
            for i in cursor.fetchall():
                self.cCommentList.append(i[0])
            
            cursor.execute(f"SELECT Picture FROM Pictures")
            for i in cursor.fetchall():
                self.picFileList.append(i[0])

            cursor.execute(f"SELECT Setting FROM Browsers where SettingType=2 and Browsername=(?)",(self.BrowserType,))
            self.BrowserUserDataLocation = cursor.fetchall()[0][0]
            cursor.execute(f"SELECT Setting FROM Browsers where SettingType=1 and Browsername=(?)",(self.BrowserType,))
            self.BrowserExeLocation = cursor.fetchall()[0][0]

            db.close()
        except:
            raise Exception("Database Process Error")

    def getPicFilePath(self):
        for pfile in self.picFileList:
            for file in os.listdir(pfile):
                if self.VideoName in file:
                    return f"{pfile}\{file}"
    
    """
    
        Run 

    """

    @pyqtSlot()
    def run(self):
        try:
            self.getDb()
            self.browserDriver()
            try:
                self.browser.get(self.YtStudioLink)
                time.sleep(self.WaitPage)
            except:
                raise Exception("Link Not Is True. Check Have 'https:'")
            
            if self.PostLimit ==0:
                self.getTotalVideo()
            else:
                self.TotalVideo = self.PostLimit    
            self.getPageTotalVideo()

            while True:
                if self.CompletedTotalVideo == self.TotalVideo:
                    self.signals.ytPlan_Log.emit(f"Tüm Videolar Ayarlandı.\n Yapılan İşlemler:\n Başlık : {self.cHead}\n Comment : {self.cComment}\n Tag : {self.cTags}\n Picture : {self.cPic}\n Tamamlanan Video : {self.CompletedTotalVideo}")
                    self.signals.ytPlan_Finish.emit({"browser":f"{self.BrowserType}"})
                    break
                else:
                    self.getVideoCellNo()
                    self.selectVideo()
                    time.sleep(self.WaitPage)
                    self.Post()
                    self.signals.ytPlan_Log.emit(f"{self.BrowserType} : {self.VideoName} isimli video işlemleri bitirildi...")
                    self.CompletedTotalVideo +=1

        except Exception as ex:
            self.signals.ytPlan_Log.emit(f"{self.BrowserType} : {ex}")
            self.signals.ytPlan_Finish.emit({"browser":f"{self.BrowserType}"})
    
    def Post(self):
        BrowserSend = BrowserSendInput(self.browser)
        BrowserBtn = BrowserButton(self.browser)

        if self.cHead  == True:
            self.Head = self.getHead()
            if len(self.Head) !=0:
                BrowserSend.writeHead(head=self.Head)
                time.sleep(self.WaitPage)
            else:
                self.signals.ytPlan_Log.emit(f"{self.BrowserType}---{self.VideoName} isimli videoya ait başlık bulunamadı.")

        if self.cComment == True:
            if len(self.Head) !=0:
                BrowserSend.writeComment(shorts=False,com=f"{self.Head} ")
                time.sleep(self.WaitPage)
        
        if self.PostType == "normal":
            if self.cPic == True:
                if len(self.picFileList) ==0:
                    self.signals.ytPlan_Log.emit(f"{self.BrowserType}---Kayıtlı kapak resim yolu bulunmamaktadır.!!")
                else:
                    file = self.getPicFilePath()
                    if file != None:
                        BrowserSend.uploadPicture(fileloc=file)
                        time.sleep(10)
                    else:
                        self.signals.ytPlan_Log.emit(f"{self.BrowserType}---{self.VideoName} isimli videonun kapak resmi bulunamadı.")

        if self.cTags == True:
            BrowserBtn.moreShowButton()
            time.sleep(self.WaitPage)
            BrowserSend.writeTag(self.getTagList())
            time.sleep(self.WaitPage)
        
        if self.PerDay == 0 or self.DayLimit == 0:
            BrowserBtn.saveAndClose()
            time.sleep(self.WaitPage)

        else:
            self.LimitControl+=1
            date=self.PostLimitControl()
            time.sleep(self.WaitPage)
            BrowserBtn.nextButton()
            time.sleep(self.WaitPage)
            if self.cMony:
                if self.PostType == "normal":
                    BrowserBtn.makeMoneyCheckBox()
                    time.sleep(self.WaitPage)

                    BrowserBtn.nextButton()
                    time.sleep(self.WaitPage)

                    BrowserBtn.checkBox()
                    time.sleep(self.WaitPage)

                    BrowserBtn.sendAdsButton()
                    time.sleep(self.WaitPage)
                else:
                    BrowserBtn.checkBox()
                    time.sleep(self.WaitPage)

                    BrowserBtn.sendAdsButton()
                    time.sleep(self.WaitPage)

            BrowserBtn.nextButton2()
            time.sleep(self.WaitPage)

            BrowserBtn.selectPlanButtons()
            time.sleep(self.WaitPage)

            BrowserSend.writeDate(date[0])
            time.sleep(self.WaitPage)

            BrowserSend.writeTime(date[1])
            time.sleep(self.WaitPage)

            BrowserBtn.planButton() 
            time.sleep(self.WaitPage)
                
            BrowserBtn.closeButton()
            time.sleep(self.WaitPage)