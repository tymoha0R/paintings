import os
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui

app = QApplication([])

win = QWidget()
win.resize(700,700)
win.setWindowTitle('Картини художників')
#win.setWindowIcon()

label_caption = QLabel('Iнформатор про картини')

label_t = QLabel('')
label_t.setFixedSize(500,400)
label_t.setStyleSheet(  '''
                            font-size:20px;
                            color:maroon;
                            background-color:lightblue
                        '''    )

label_p = QLabel('')
label_p.setFixedSize(500,500)

left = QPushButton('<<<')
right = QPushButton('>>>')

button = QHBoxLayout()
button.addWidget(left)
button.addWidget(right)

row_label = QHBoxLayout()
row_label.addWidget(label_t)
row_label.addWidget(label_p)
h = QVBoxLayout()
h.addWidget(label_caption,alignment=Qt.AlignCenter)
h.addLayout(row_label)
h.addLayout(button)
win.setLayout(h)

m = os.path.abspath("1.txt")
t = open(m,encoding='utf-8')
label_t.setText(t.read())
label_p.hide()
pixmapimage = QPixmap("1.jpg")
w,h = label_p.width(),label_p.height()
pixmapimage = pixmapimage.scaled(500,700,Qt.KeepAspectRatio)
label_p.setPixmap(pixmapimage)
label_p.show()



i = 1
def button_right():
    global i
    i=i+1
    if i == 5:
        i=1
    t=open(str(i)+'.txt',encoding='utf-8')
    label_t.setText(t.read())
    label_p.hide()
    pixmapimage = QPixmap(str(i)+'.jpg')
    w,h = label_p.width(),label_p.height()
    pixmapimage = pixmapimage.scaled(500,700,Qt.KeepAspectRatio)
    label_p.setPixmap(pixmapimage)
    label_p.show()
def button_left():
    global i
    i=i-1
    if i == 0:
        i=4
    t=open(str(i)+'.txt',encoding='utf-8')
    label_t.setText(t.read())

    
    label_p.hide()
    pixmapimage = QPixmap(str(i)+'.jpg')
    w,h = label_p.width(),label_p.height()
    pixmapimage = pixmapimage.scaled(500,700,Qt.KeepAspectRatio)
    label_p.setPixmap(pixmapimage)
    label_p.show()
right.clicked.connect(button_right)
left.clicked.connect(button_left)

win.show()
app.exec_()
