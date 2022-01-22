# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 13:59:27 2021

@author: med
"""
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QPushButton, \
                            QVBoxLayout, QFormLayout, QLineEdit
from PyQt5.QtCore import Qt, QThread
import sys
import worker

class Obitobot(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.NAVIG_PATH= 'a'
        
        self.resize(400,100)
        self.setWindowTitle('Obitobot')
        
        
        self.layout = QVBoxLayout()
        self.formLayout = QFormLayout()
        self.formLayout.addWidget(QLabel())
        self.mmpwd = QLineEdit()
        self.mmpwd.setEchoMode(QLineEdit.Password)
        self.formLayout.addRow('MetaMask:', self.mmpwd)
        self.formLayout.addWidget(QLabel())
        self.layout.addLayout(self.formLayout)

        self.msg = QLabel()        
        self.layout.addWidget(self.msg, alignment=Qt.AlignCenter)
        
        self.start_btn = QPushButton('Lancer', self)
        self.start_btn.clicked.connect(self.start_f)        
        self.layout.addWidget(QLabel())
        self.layout.addWidget(self.start_btn , alignment=Qt.AlignCenter)
        
        self.setLayout(self.layout)

    def start_f(self):
        self.msg.setText("<h2>Le Bot est actif<\h2>")
        try:
            self.start_btn.setEnabled(False)
            self.mmpwd.setEnabled(False)
            #worker.setPwd(self.mmpwd.text())
            #worker.dayMode()

            # 1 - create Worker and Thread inside the Form
            self.worker = worker.Worker()  # no parent!
            self.thread = QThread()  # no parent!
            # 2 - Connect Worker`s Signals to Form method slots to post data.
            #self.worker.intReady.connect(self.onIntReady)
            # 3 - Move the Worker object to the Thread object
            self.worker.moveToThread(self.thread)
            # 4 - Connect Worker Signals to the Thread slots
            self.worker.finished.connect(self.thread.quit)
            # 5 - Connect Thread started signal to Worker operational slot method
            self.thread.started.connect(self.worker.runscript)
            # * - Thread finished signal will close the app if you want!
            #self.thread.finished.connect(app.exit)
            # 6 - Start the thread
            self.thread.start()


        except FileNotFoundError:
            self.msg.setText("<h3>Navigateur introuvable<\h3>") 
        except Exception as e:
            self.msg.setText("<h3>Erreur windows<\h3>") 
            print(e)
            
"""    def radio_state(self, rb):
        if rb.text() =='Chrome 32bit':
            self.NAVIG_PATH='C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe'
        if rb.text() =='Chrome 64bit':
            self.NAVIG_PATH='C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'              
        if rb.text() =='Firefox 32bit':
            self.NAVIG_PATH='C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe'
        if rb.text() =='Firefox 64bit':
            self.NAVIG_PATH='C:\\Program Files\\Mozilla Firefox\\firefox.exe'
                
       # print(self.NAVIG_PATH)
       # print(nv)
"""           
                
        
def Start():
    m = Obitobot()
    m.show()
    return m

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Start()

    sys.exit(app.exec_())