# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 13:19:01 2021

@author: med
"""

#import numpy as np
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QPushButton, QVBoxLayout
import subprocess
import sys

NAVIG_PATH= 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'

# open navigator

# activate Meta Mask

# open app.bombcrypto.io 
#subprocess.call([NAVIG_PATH, 'app.bombcrypto.io'])

# connect wallet


def start():
    msg.setText("Bot active")


app = QApplication([])
window = QWidget()

window.setWindowTitle('AutoKliK')
window.resize(300,100)


layout = QVBoxLayout()

close_btn = QPushButton('Lancer')
close_btn.clicked.connect(start)  # Connect clicked to greeting()

msg = QLabel()

layout.addWidget(close_btn)
layout.addWidget(msg)

window.setLayout(layout)
window.show()

app.exec_()