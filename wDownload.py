from PyQt5.QtCore import pyqtSignal,QObject,QRunnable,pyqtSlot
from pytube import YouTube,Playlist
import datetime
import threading, queue

class ytDownloadSignals(QObject):
    ytDownload_Finish = pyqtSignal(bool)
    ytDownload_Log = pyqtSignal(str)

class ytDownload(QRunnable):
    """
    list_link: Yotube Video Links or Play List Links
    resolution : 1080p or 720p
    output_path : Video Save File Path
    playlist : True/False
    """
    def __init__(self,list_link,resolution,output_path,playlist):
        super(ytDownload, self).__init__()
        self.que = queue.Queue()
        self.signals = ytDownloadSignals()
        self.worker_count = 3
        self.list_link =list_link
        self.resolution = resolution
        self.output_path = output_path
        self.playlist = playlist

        self.error_link = []
        self.low_res_count = 0
        self.mid_res_count = 0
        self.high_res_count = 0
        self.low_res_title = []
        self.start_down_time = datetime.datetime.now()

    
    @pyqtSlot()
    def run(self):
        self.addQue()
        self.signals.ytDownload_Log.emit("İndirme Başladı")
        self.signals.ytDownload_Log.emit(50*"*")
        for i in range(self.worker_count):
            worker =threading.Thread(target=self.main,daemon=True)   
            worker.start()
        self.que.join()
        self.signals.ytDownload_Finish.emit(True)
        if len(self.error_link) !=0:
            self.signals.ytDownload_Log.emit(f"{self.error_link} linkleri indirilemedi.")
    
    def down1080p(self,link):
        try:
            YouTube(link).streams.get_by_itag(137).download(output_path=self.output_path)
            self.high_res_count += 1
            self.signals.ytDownload_Log.emit(f"{YouTube(link).title} isimli video 1080p indirildi.")
        except:
            self.down720p(link)
    
    def down720p(self,link):
        try:
            YouTube(link).streams.get_by_itag(22).download(output_path=self.output_path)
            self.mid_res_count += 1
            self.low_res_title.append(YouTube(link).title)
            self.signals.ytDownload_Log.emit(f"{YouTube(link).title} isimli video 720p indirildi.")
        except:
            self.down360p(link)

    def down360p(self,link):
        try:
            YouTube(link).streams.get_by_itag(18).download(output_path=self.output_path)
            self.low_res_count += 1
            self.low_res_title.append(YouTube(link).title)
            self.signals.ytDownload_Log.emit(f"{YouTube(link).title} isimli video 360p indirildi.")
        except:
            self.error_link.append(link)
            self.signals.ytDownload_Log.emit(f"{YouTube(link).title} isimli video indirilemedi.")   

    def addQue(self):
        if self.playlist:
            for link in self.list_link:
                for url in Playlist(link).video_urls:
                    self.que.put(url)    
        else:
            for link in self.list_link:
                self.que.put(link)

    def main(self):
        while not self.que.empty():
            data = self.que.get()
            if self.resolution == "1080p":
                self.down1080p(data)
            elif self.resolution == "720p":
                self.down720p(data)
            self.que.task_done()

