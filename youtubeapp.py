from PyQt5.QtCore import QThreadPool
from PyQt5.QtWidgets import QApplication,QMainWindow,QFileDialog,QMessageBox,QAction,QTableWidgetItem

import sqlite3 as sql
import sys,os
import threading

from App_ui import Ui_Youtube
from wDownload import ytDownload
from wSS import ssWorker
from wYtOtoPost import ytOtoPost


class YoutubeApp(QMainWindow):
    def __init__(self):
        super(YoutubeApp,self).__init__()
        self.BasePath = sys.path[0]
        self.ui = Ui_Youtube()
        self.ui.setupUi(self)
        self.i = 0
        self.YtPlanRow = -1
        self.YtPlanColumn = -1
        self.YtPlanid = -1
        self.threadpool = QThreadPool()
        self.PlanMenuButtonName = ""
        self.PostType = "normal"
        self.BrowserType = ""
        self.BrowserMem = {
                "opera":{
                    "button":True
                },"brave":{
                    "button":True
                },"chrome":{
                    "button":True
                }
        }
        quit = QAction("Quit", self)
        quit.triggered.connect(self.close)
        # Main Menu
        self.ui.MenuDownloadButton.clicked.connect(self.menuDownload)
        self.ui.MenuSSButton.clicked.connect(self.menuSS)
        self.ui.MenuyYtPlanButton.clicked.connect(self.menuYtPlan)
        
        # Video SS
        self.ui.SSGetPathButton.clicked.connect(self.getVideoPath)
        self.ui.SSGetSavePathButton.clicked.connect(self.getSSPath)
        self.ui.SSRunButton.clicked.connect(self.ssRun)
        
        # Yt Video Download
        self.ui.DownloadGetSavePathButton.clicked.connect(self.getDownloadPath)
        self.ui.DownloadRun.clicked.connect(self.downloadRun)

        # Yt Plan Main Menu
        self.ui.YtPlanMenuInputSettingsButton.clicked.connect(self.YtMenuInputSettingsButton)
        self.ui.YtPlanMenuShareButton.clicked.connect(self.YtMenuShareButton)
        
        # Yt Plan Share 
        self.ui.BraveButton.clicked.connect(self.menuBrave)
        self.ui.ChromeButton.clicked.connect(self.menuChrome)
        self.ui.OperaButton.clicked.connect(self.menuOpera)

        self.ui.NormalMenuButton.clicked.connect(self.menuNormal)
        self.ui.ShortsMenuButton.clicked.connect(self.menuShorts)

        self.ui.YtPlanRunButton.clicked.connect(self.runYtPlan)
        self.ui.BrowserExeButton.clicked.connect(self.BrowserExeGetFile)

        # Yt Plan Settings
        
        self.ui.HeadButton.clicked.connect(self.headList)
        self.ui.CommentButton.clicked.connect(self.commentList)
        self.ui.TagButton.clicked.connect(self.tagList)
        self.ui.BrowserButton.clicked.connect(self.browserList)
        self.ui.PicturesButton.clicked.connect(self.picList)

        self.ui.TrRadioButton.clicked.connect(self.TrRadioButton)
        self.ui.EngRadioButton.clicked.connect(self.EngRadioButton)

        self.ui.tableWidget.cellClicked.connect(self.getRow)

        self.ui.InputAddButton.clicked.connect(self.addRow)
        self.ui.InputDeleteButton.clicked.connect(self.delRow)
        self.ui.InputUpdateButton.clicked.connect(self.updateRow)


    """-----  Main Menu  ----------"""

    def checkMenuButton(self,ss=True,download=True,ytplan=True):
        self.ui.MenuSSButton.setEnabled(ss)
        self.ui.MenuDownloadButton.setEnabled(download)
        self.ui.MenuyYtPlanButton.setEnabled(ytplan)

    def menuSS(self):
        self.checkMenuButton(ss=False)
        self.ui.groupBoxSS.show()
        self.ui.groupBoxSSLog.show()
        self.ui.groupBoxDownload.hide()   
        self.ui.groupBoxDownloadLog.hide()
        self.ui.YtPlanGroupBox.hide()
        self.ui.groupBoxYtPlanLog.hide()
    
    def menuDownload(self):
        self.checkMenuButton(download=False)
        self.ui.groupBoxSS.hide()
        self.ui.groupBoxSSLog.hide()
        self.ui.groupBoxDownload.show()  
        self.ui.groupBoxDownloadLog.show()
        self.ui.YtPlanGroupBox.hide()
        self.ui.groupBoxYtPlanLog.hide()
    
    def menuYtPlan(self):
        if self.conDb() !=False:
            self.checkMenuButton(ytplan=False)
            self.ui.groupBoxSS.hide()
            self.ui.groupBoxSSLog.hide()
            self.ui.groupBoxDownload.hide()  
            self.ui.groupBoxDownloadLog.hide()
            self.ui.YtPlanGroupBox.show()
            self.ui.groupBoxYtPlanLog.show()
            self.BrowserCheck()

    """-------- Another Process ----------""" 
    
    def closeEvent(self, event):
        self.threadpool.clear()
        threading.Event().set()

    def getFilePath(self,onlydirs=True, startfile =""):
        file =""
        if onlydirs:
            file = QFileDialog.getExistingDirectory(self, "Open Directory", startfile,
                                        QFileDialog.ShowDirsOnly
                                        |QFileDialog.DontResolveSymlinks)
        else:
            file = QFileDialog.getOpenFileName(self,"Open File", startfile, "*")
        return file    
    
    def messageBox(self,title,text):
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setIcon(QMessageBox.Icon.Warning)
        msg.setText(text)
        return msg.exec()
    
    """-----------YT PLAN --------------"""

    """-----Browser Menu----------"""
    def BrowserCheck(self):
        db = self.conDb()
        listbrowser = db.cursor().execute(f"select Browsername from Browsers").fetchall()

        for brw in listbrowser:
            if "brave" in brw:
                self.ui.BraveButton.setVisible(True)
            elif "opera" in brw:
                self.ui.OperaButton.setVisible(True)
            elif "chrome" in brw:
                self.ui.ChromeButton.setVisible(True)
    
    def browserMenuCheck(self,chrm=True,opera=True,brave=True):
        self.ui.OperaButton.setEnabled(opera)
        self.ui.BraveButton.setEnabled(brave)
        self.ui.ChromeButton.setEnabled(chrm)
    
    def menuChrome(self):
        self.browserMenuCheck(chrm=False)
        self.BrowserType ="chrome"
        if self.BrowserMem["chrome"]["button"] == False:
            self.ui.YtPlanRunButton.setEnabled(False)
        else:
            self.ui.YtPlanRunButton.setEnabled(True)

    def menuOpera(self):
        self.browserMenuCheck(opera=False)
        self.BrowserType ="opera"
        if self.BrowserMem["opera"]["button"] == False:
            self.ui.YtPlanRunButton.setEnabled(False)
        else:
            self.ui.YtPlanRunButton.setEnabled(True)

    def menuBrave(self):
        self.browserMenuCheck(brave=False)
        self.BrowserType ="brave"
        if self.BrowserMem["brave"]["button"] == False:
            self.ui.YtPlanRunButton.setEnabled(False)
        else:
            self.ui.YtPlanRunButton.setEnabled(True)
    
    """----- Post Type Menu----------"""
    
    def postMenuCheck(self,normal=True,shorts=True):
        self.ui.NormalMenuButton.setEnabled(normal)
        self.ui.ShortsMenuButton.setEnabled(shorts)
    
    def menuNormal(self):
        self.postMenuCheck(normal=False)
        self.PostType = "normal"

    def menuShorts(self):
        self.postMenuCheck(shorts=False)
        self.PostType = "shorts"

    
    """ ----Yt Post Menu---"""

    def ytPlanMenuButtonCheck(self,share = True,set = True):
        self.ui.YtPlanMenuInputSettingsButton.setEnabled(set)
        self.ui.YtPlanMenuShareButton.setEnabled(share)

    def YtMenuInputSettingsButton(self):
        self.ui.YtPlanItemGroupBox.show()
        self.ui.YtPlanShareGroupBox.hide()
        self.ytPlanMenuButtonCheck(set=False)

    def YtMenuShareButton(self):
        self.ui.YtPlanItemGroupBox.hide()
        self.ui.YtPlanShareGroupBox.show()
        self.ytPlanMenuButtonCheck(share=False)

    """-------------- YT PLAN RUN ------------------"""

    def YtPlanFinish(self,data):
        self.BrowserMem[data["browser"]]["button"]=True
        self.ui.YtPlanRunButton.setEnabled(True)

    def YtPlanWriteLog(self,data):
        self.ui.YtPlanLogtextBrowser.append(data)

    def runYtPlan(self):
        lang = 2
        if self.ui.TrChannelRadioButton.isChecked():
            lang = 1
        link = self.ui.LinkLineEdit.text()

        monyCheck = self.ui.MonyCbox.isChecked()
        Head = self.ui.HeadCbox.isChecked()
        Coment = self.ui.CommentCbox.isChecked()
        Pic = self.ui.PicCbox.isChecked()
        Tag = self.ui.TagCbox.isChecked()
        
        PerDay =  self.ui.PPerDay.text()
        PerMin =  self.ui.PPerMin.text()
        DayLimit =  self.ui.PDayLimit.text()
        PostLimit =  self.ui.PLimit.text()
        DateTime =  self.ui.PDateTime.text()

        data ={
            "BrowserType":self.BrowserType,
            "PostType":self.PostType,
            "Language":lang,
            "link":link,
            "monyCheck" : monyCheck,
            "Head" :Head,
            "Coment" : Coment,
            "Pic" :Pic,
            "Tag" :Tag,
            "PerDay" : PerDay,
            "PerMin" : PerMin,
            "PostLimit" : PostLimit,
            "DayLimit": DayLimit,
            "DateTime" :  DateTime,
            "BasePath":self.BasePath,
        }

        PostNullCheck = bool(int(PerDay)==0)+bool(int(PostLimit)==0)
        PostNullCheck2 = Head+Coment+Pic+Tag

        if self.BrowserType == "":
            self.YtPlanWriteLog("Not Select The Browser")
            self.messageBox(title="Dikkat !!!",text="Browser Seçmedin.")
        elif "studio" not in link:
            self.YtPlanWriteLog("Link Is Null or Not True")
            self.messageBox(title="Dikkat !!!",text="Link Koymadın veya Yanlış.")
        elif PostNullCheck == 0 or PostNullCheck2>0:
            worker = ytOtoPost(data)
            worker.signals.ytPlan_Log.connect(self.YtPlanWriteLog)
            worker.signals.ytPlan_Finish.connect(self.YtPlanFinish)
            self.threadpool.start(worker)
            self.ui.YtPlanRunButton.setEnabled(False)
            self.BrowserMem[self.BrowserType]["button"]=False
        else:
            self.YtPlanWriteLog("Some Selections Cannot Be Left Empty")
            self.messageBox(title="Dikkat !!!",text="Gerekli Seçimler Yapılmadı.")

        
    def BrowserExeGetFile(self):
        file = self.getFilePath(onlydirs=False)
        if file[0] !="":
            self.ui.BrowserExelineEdit.setText(file[0])

    """-----------YT PLAN HEAD/TAG... SETTİNGS--------------"""
    
    def loadTable(self):
        self.ui.tableWidget.clear()
        self.ui.tableWidget.setRowCount(0)
        lang=2
        if self.ui.TrRadioButton.isChecked():
            lang=1
        if self.PlanMenuButtonName != "":
            if self.PlanMenuButtonName == "Browsers" or self.PlanMenuButtonName =="Pictures" :
                self.load_initial_data(f"{self.PlanMenuButtonName}")
            else:
                self.load_initial_data(f"{self.PlanMenuButtonName}",f"Language={lang};")
                
    def addRow(self):
        if self.ui.InputlineEdit.text() == '':
            if self.PlanMenuButtonName !="Browsers" and self.ui.InputlineEdit2.text() == '':
                self.messageBox(title="Dikkat !!!",text="Alanları Boş Bıraktın.")
            else:
                self.messageBox(title="Dikkat !!!",text="Alanları Boş Bıraktın.")
        else:
            lang=2
            if self.ui.TrRadioButton.isChecked():
                lang=1
            db = self.conDb()
            if self.PlanMenuButtonName =="Browsers":
                settingtype = 2
                browsernamelist = ["chrome","opera","brave"]
                browsername = ""
                for i in browsernamelist:
                    if i in self.ui.InputlineEdit.text().lower():
                        browsername = i
                if "exe" in self.ui.InputlineEdit.text().lower():
                    settingtype = 1
                if browsername !="":
                    db.cursor().execute(f"INSERT INTO {self.PlanMenuButtonName} (Setting,SettingType,BrowserName) VALUES (?,?,?)",(str(self.ui.InputlineEdit.text()),str(settingtype),str(browsername)))
                else:
                    self.messageBox(title="Dikkat !!!",text="Verilen Dosya Yolu Hatalı.")
            elif self.PlanMenuButtonName == "Comments":
                db.cursor().execute(f"INSERT INTO {self.PlanMenuButtonName} ({self.PlanMenuButtonName[:-1]},Language) VALUES (?,?)",(str(self.ui.InputlineEdit.text()),str(lang)))
            elif self.PlanMenuButtonName == "Pictures":
                db.cursor().execute(f"INSERT INTO {self.PlanMenuButtonName} ({self.PlanMenuButtonName[:-1]}) VALUES (?)",(str(self.ui.InputlineEdit.text()),))
            else:
                db.cursor().execute(f"INSERT INTO {self.PlanMenuButtonName} ({self.PlanMenuButtonName[:-1]},Language,Secondid) VALUES (?,?,?)",(str(self.ui.InputlineEdit.text()),str(lang),str(self.ui.InputlineEdit2.text())))
            db.commit()
            db.close()
            self.loadTable()

    def updateRow(self):
        if self.YtPlanid == -1:
            self.messageBox(title="Dikkat !!!",text="Tablo Üzerinden Seçim Yapın.")
        else:
            db = self.conDb()
            if self.PlanMenuButtonName =="Browsers":
                db.cursor().execute(f"UPDATE {self.PlanMenuButtonName} SET Setting='{self.ui.InputlineEdit.text()}' WHERE {self.PlanMenuButtonName[:-1]}id={self.YtPlanid}")
            elif self.PlanMenuButtonName == "Comments" or self.PlanMenuButtonName == "Pictures":
                db.cursor().execute(f"UPDATE {self.PlanMenuButtonName} SET {self.PlanMenuButtonName[:-1]}='{self.ui.InputlineEdit.text()}' WHERE {self.PlanMenuButtonName[:-1]}id={self.YtPlanid}")
            else:
                db.cursor().execute(f"UPDATE {self.PlanMenuButtonName} SET {self.PlanMenuButtonName[:-1]}='{self.ui.InputlineEdit.text()}',Secondid = '{self.ui.InputlineEdit2.text()}' WHERE {self.PlanMenuButtonName[:-1]}id={self.YtPlanid}")
            db.commit()
            db.close()
            self.loadTable()

    def delRow(self):
        if self.YtPlanid == -1:
            self.messageBox(title="Dikkat !!!",text="Tablo Üzerinden Seçim Yapın.")
        else:
            db = self.conDb()
            db.cursor().execute(f"DELETE FROM {self.PlanMenuButtonName} WHERE {self.PlanMenuButtonName[:-1]}id ='{self.YtPlanid}'")
            db.commit()
            db.close()
            self.loadTable()

    def getRow(self):
        self.YtPlanRow =self.ui.tableWidget.currentRow()
        self.YtPlanColumn =self.ui.tableWidget.currentColumn()
        self.YtPlanid = self.ui.tableWidget.item(self.YtPlanRow,1).text()

        if self.PlanMenuButtonName in ("Heads","Tags"):
            self.ui.InputlineEdit.setText(self.ui.tableWidget.item(self.YtPlanRow,0).text())
            self.ui.InputlineEdit2.setText(self.ui.tableWidget.item(self.YtPlanRow,2).text())
        else:
            self.ui.InputlineEdit.setText(self.ui.tableWidget.item(self.YtPlanRow,0).text())
            self.ui.InputlineEdit2.setText(self.ui.tableWidget.item(self.YtPlanRow,1).text())

    def conDb(self):
        db_path = rf"{self.BasePath}\appdb.sqlite"
        if os.path.exists(db_path):
            return sql.connect(db_path)
        else:
            self.messageBox("Dikkat !!","Veritabanı bulunamadı.")
            return False
        
    def customizeTable(self,len):
        if self.PlanMenuButtonName =="Pictures":
            self.ui.tableWidget.setColumnCount(len)
        else:
            self.ui.tableWidget.setColumnCount(len-1)
        self.ui.tableWidget.setColumnWidth(0,420)
        for i in range(1,len):
            self.ui.tableWidget.setColumnWidth(i,30)       

    def load_initial_data(self,frm,whr ="",slct="*"):
        cursor = self.conDb().cursor()
        if whr != "":
            cursor.execute(f"SELECT {slct} FROM {frm} where {whr}")
        else:
            cursor.execute(f"SELECT {slct} FROM {frm}")

        rows = cursor.fetchall()
        if len(rows) !=0:
            self.customizeTable(len(rows[0]))
        for row in rows:
            inx = rows.index(row)
            self.ui.tableWidget.insertRow(inx)
            self.ui.tableWidget.setItem(inx, 0, QTableWidgetItem(row[1]))
            if len(row) == 4:
                self.ui.tableWidget.setItem(inx, 2, QTableWidgetItem(str(row[3])))
            self.ui.tableWidget.setItem(inx, 1, QTableWidgetItem(str(row[0])))
   
    def TrRadioButton(self):
        self.ui.tableWidget.clear()
        self.ui.tableWidget.setRowCount(0)
        self.YtPlanItemClear()
        self.loadTable()

    def EngRadioButton(self):
        self.ui.tableWidget.clear()
        self.ui.tableWidget.setRowCount(0)
        self.YtPlanItemClear()
        self.loadTable()
    
    def YtPlanItemClear(self):
        self.YtPlanRow = -1
        self.YtPlanColumn = -1
        self.YtPlanid = -1
        self.ui.InputlineEdit.clear()
        self.ui.InputlineEdit2.clear()
    """------------ YT SETTİNGS BUTTON  ------------"""

    def checkButton(self,head=True,comment=True,tag=True,browser=True,pictures=True):
        self.ui.HeadButton.setEnabled(head)
        self.ui.CommentButton.setEnabled(comment)
        self.ui.TagButton.setEnabled(tag)
        self.ui.BrowserButton.setEnabled(browser)
        self.ui.PicturesButton.setEnabled(pictures)

    def headList(self):
        self.PlanMenuButtonName = "Heads"
        self.checkButton(head=False)
        self.ui.TrRadioButton.setChecked(True)
        self.TrRadioButton()

        self.ui.InputlineLabel.setText("Başlık")
        self.ui.InputlineLabel2.setText("Özel Tanım")
        self.ui.InputlineLabel2.setVisible(True)
        self.ui.InputlineEdit2.setVisible(True)

    def commentList(self):
        self.PlanMenuButtonName = "Comments"
        self.checkButton(comment=False)
        self.ui.TrRadioButton.setChecked(True)
        self.TrRadioButton()
  
    def tagList(self):
        self.PlanMenuButtonName = "Tags"
        self.checkButton(tag=False)
        self.ui.TrRadioButton.setChecked(True)
        self.TrRadioButton()
        self.ui.InputlineLabel.setText("Etiket")
        self.ui.InputlineLabel2.setText("Özel Tanım")
        self.ui.InputlineLabel2.setVisible(True)
        self.ui.InputlineEdit2.setVisible(True)
    
    def browserList(self):
        self.PlanMenuButtonName = "Browsers"
        self.checkButton(browser=False)
        self.loadTable()
        self.ui.InputlineLabel.setText("Exe/User Data")
        self.ui.InputlineLabel2.setVisible(False)       
        self.ui.InputlineEdit2.setVisible(False)
        self.YtPlanItemClear()

    def picList(self):
        self.PlanMenuButtonName = "Pictures"
        self.checkButton(pictures=False)
        self.loadTable()
        self.ui.InputlineLabel.setText("Resim Dosya Yolu")
        self.ui.InputlineLabel2.setVisible(False)
        self.ui.InputlineEdit2.setVisible(False)
        self.YtPlanItemClear()
    
    """-------- Video SS App ----------"""
    
    def getVideoPath(self):
        file = self.getFilePath()
        self.ui.SSGetPathLine.setText(file)

    def getSSPath(self):
        file = self.getFilePath()
        self.ui.SSGetSavePathLine.setText(file+"/")
    
    def ssWriteLog(self,log_data):
        self.ui.SSLogtextBrowser.append(log_data)

    def ssFinish(self,c):
        if c:
            self.ui.SSLogtextBrowser.append(50*"-")
            self.ui.SSLogtextBrowser.append("İşlem Tamamlandı.")
            self.ui.SSLogtextBrowser.append(50*"-")
            self.messageBox("Dikkat !","İşlem Tamamlandı.")
            self.threadpool.clear()
            self.ui.SSRunButton.setEnabled(True)

    def ssRun(self):
        video_path = self.ui.SSGetPathLine.text()
        save_path = self.ui.SSGetSavePathLine.text()
        outro = self.ui.SSOutroCheckBox.isChecked()
        h = self.ui.SSHeightLine.text()
        w = self.ui.SSWidthLine.text()
        if len(h) == 0 or len(w) == 0:
            h = 720
            w = 1280
        if len(video_path) == 0 or len(save_path) == 0:
            self.messageBox("Dikkat !","Dosya Yollarını Boş Bıraktın.")
        else:
            self.ui.SSRunButton.setEnabled(False)
            worker = ssWorker(video_path=video_path,save_path=save_path,outro=outro,high=h,width=w)
            worker.signals.ss_Log.connect(self.ssWriteLog)
            worker.signals.ss_Finish.connect(self.ssFinish)
            # Execute
            self.threadpool.start(worker)
   
    """-------- Youtube Download App ----------"""

    def getDownloadPath(self):
        file = self.getFilePath()
        self.ui.DownloadGetSavePathLine.setText(file+"/")

    def downloadFinish(self,c):
        if c:
            self.ui.DownloadLogtextBrowser.append(50*"-")
            self.ui.DownloadLogtextBrowser.append("İşlem Tamamlandı.")
            self.ui.DownloadLogtextBrowser.append(50*"-")
            self.messageBox("Dikkat !","İşlem Tamamlandı.")
            self.threadpool.clear()
            self.ui.DownloadRun.setEnabled(True)
    
    def downloadWriteLog(self,log_data):
        self.ui.DownloadLogtextBrowser.append(log_data)

    def downloadRun(self):
        output_path = self.ui.DownloadGetSavePathLine.text()
        link_list = self.ui.DownloadTextEdit.toPlainText()
        playlist = self.ui.PlayListCheck.isChecked()
        resolution ='720p'
        
        if self.ui.FullHdRadio.isChecked():
            resolution = '1080p'

        if len(link_list)==0:
            self.messageBox("Dikkat !", "Link Koymadın.")
        else:
            link = []
            for i in link_list.split(","):
                if len(i) != 0:
                    link.append(i)
            if len(output_path)==0:
                self.messageBox("Dikkat !", "Kayıt Yerini Seçmedin.")
            else:
                worker = ytDownload(list_link=link,resolution=resolution,output_path=output_path,playlist=playlist)
                worker.signals.ytDownload_Log.connect(self.downloadWriteLog)
                worker.signals.ytDownload_Finish.connect(self.downloadFinish)
                # Execute
                self.ui.DownloadRun.setEnabled(False)
                self.threadpool.start(worker)   


if __name__=="__main__":
    app = QApplication(sys.argv)
    win =YoutubeApp()
    win.show()
    sys.exit(app.exec())
