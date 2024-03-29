from PyQt5.QtCore import pyqtSignal,QObject,QRunnable,pyqtSlot
import threading, queue
import cv2
import os

class ssSignals(QObject):
    ss_Finish = pyqtSignal(bool)
    ss_Log = pyqtSignal(str)


class ssWorker(QRunnable):
    """
    SS For the Yotube Picture.
    video_path: Video File Path
    save_path : SS Save File Path
    high : SS High Resulation
    width : SS Width Resulation
    outro : True/False (-10 Second)
    """
    def __init__(self,video_path,save_path,high=720,width=1280,outro=False):
        super(ssWorker, self).__init__()
        self.video_path = video_path
        self.save_path = save_path
        self.high = high
        self.width = width
        self.outro = outro
        self.signals = ssSignals()
        self.que = queue.Queue()
        self.worker_count = 3


    @pyqtSlot()
    def run(self):
        self.addQue()
        for i in range(self.worker_count):
            worker =threading.Thread(target=self.main,daemon=True)   
            worker.start()
        self.que.join()
        self.signals.ss_Finish.emit(True)
    
    def addQue(self):
        for i in os.listdir(os.chdir(self.video_path)):
            if (".mp4") in i:
                self.que.put(i)

    def main(self):
        while not self.que.empty():
            data = self.que.get()
            self.SS(data,self.outro)
            self.que.task_done()

    def SS(self,video_path,outro):
        name,num = video_path.split(' ')
        cap = cv2.VideoCapture(video_path)
        if outro:
            outro_ms = cap.get(cv2.CAP_PROP_FPS)*10 # Second Per Picture * outro second
            cap.set(1,cap.get(7)-(outro_ms+20)) # cap.get(7): return millisecond video length. If we remove "outro_ms" we are left with the last frame without outro.
        else:
            cap.set(1,cap.get(7)-1)
        ret, frame = cap.read()
        frame = cv2.resize(frame, (int(self.width), int(self.high)))
        cv2.imwrite(f"{self.save_path}{name} {num.split('.')[0]}.png", frame) 
        self.signals.ss_Log.emit(f"{video_path} isimli videonun SS alındı.")
