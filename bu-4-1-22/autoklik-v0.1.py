# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 13:59:27 2021

@author: med
"""
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QPushButton, \
                            QVBoxLayout, QFormLayout, QLineEdit, QRadioButton, \
                            QButtonGroup, QGridLayout
from PyQt5.QtCore import Qt
import subprocess
import sys
import subprocess

class AutoKlik(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.NAVIG_PATH= 'a'
        
        self.resize(400,100)
        self.setWindowTitle('AutoKlik')
        
        self.chrome32 = QRadioButton("Chrome 32bit")
        self.chrome32.toggled.connect(lambda:self.radio_state(self.chrome32))
        self.firefox32 = QRadioButton("Firefox 32bit")  
        self.firefox32.toggled.connect(lambda:self.radio_state(self.firefox32))
        self.chrome64 = QRadioButton("Chrome 64bit")
        self.chrome64.toggled.connect(lambda:self.radio_state(self.chrome64))
        self.firefox64 = QRadioButton("Firefox 64bit")  
        self.firefox64.toggled.connect(lambda:self.radio_state(self.firefox64))
        self.navtype = QButtonGroup(self)
        self.navtype.addButton(self.chrome32)
        self.navtype.addButton(self.firefox32)
        self.navtype.addButton(self.chrome64)
        self.navtype.addButton(self.firefox64)        
        
        self.layout = QVBoxLayout()
        
        self.gridLayout = QGridLayout()
        self.gridLayout.addWidget(self.chrome32,0,0)
        self.gridLayout.addWidget(self.firefox32,0,1)
        self.gridLayout.addWidget(self.chrome64,1,0)
        self.gridLayout.addWidget(self.firefox64,1,1)
        
        self.layout.addLayout(self.gridLayout)
        #self.layout.addStretch()
        
        self.formLayout = QFormLayout()
        self.formLayout.addWidget(QLabel())
        self.mmpwd = QLineEdit()
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
            subprocess.call([self.NAVIG_PATH, 'app.bombcrypto.io'])
            self.start_btn.setEnabled(False)
            for b in self.navtype.buttons():
                b.setEnabled(False)

        except FileNotFoundError:
            self.msg.setText("<h3>Navigateur introuvable<\h3>") 
            
    def radio_state(self, rb):
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
            
                
        


if __name__ == '__main__':
    app = QApplication(sys.argv)
    AKK = AutoKlik()
    AKK.show()
    
    sys.exit(app.exec_())