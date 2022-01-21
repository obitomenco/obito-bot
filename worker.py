# worker.py
from PyQt5.QtCore import QObject, pyqtSignal
import core 

class Worker(QObject):
    finished = pyqtSignal()
    intReady = pyqtSignal(int)

    def setPwd(self, pwd):
        core.setPwd(pwd)

    def runscript(self): # A slot takes no params
        core.dayMode()
        self.finished.emit()