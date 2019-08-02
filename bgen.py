from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import *
from PyQt5.QtCore import QSize, QPropertyAnimation, QRect
from PyQt5.QtWidgets import *
import sys
import img1
import json
import random, time

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi('mainWindow.ui', self) # Load the .ui file
        self.show() # Show the GUI
        self.pushButton.clicked.connect(self.miror_pixmap)
        self.flag = False
        self.label_img.setPixmap(QPixmap("wof.png"))

    def miror_pixmap(self):
        pixmap = QPixmap("wof.png")
        transform = QTransform()
        i=0
        while i < 300:
         transform.rotate(i)
         self.label_img.setPixmap(QPixmap(pixmap.transformed(transform)))
         i=i+1



        #self.setGeometry(100,100,540,490)

        #oImage = QImage("PAPA.jpg")
        #sImage = oImage.scaled(QSize(540,490))                   # resize Image to widgets size
        #palette = QPalette()
        #palette.setBrush(10, QBrush(sImage))                     # 10 = Windowrole
        #self.setPalette(palette)

        #self.label = QLabel('Test', self)                        # test, if it's really backgroundimage
        #self.label.setGeometry(50,50,200,50)

        self.frame = QFrame(self)
        self.frame.setFrameStyle(QFrame.Panel | QFrame.Raised)
        self.frame.setGeometry(150, 30, 100, 100)
       
    def tira(self):
        if self.checkBox.isChecked():
          self.label_best.setText("Dio")
        elif self.checkBox_2.isChecked():
           self.label_best.setText("Gesù")
        elif self.checkBox_3.isChecked():
           self.label_best.setText("Madonna")
        elif self.checkBox.isChecked():
            self.label_best.setText("Santo")
        else:
            self.label_best.setText("Ciao")

        with open('animali.json', 'r') as f:
           animal_dict = json.load(f)


        if self.checkBox_5.isChecked():
        	caso=str(random.randint(1,515))
        	animale=animal_dict.get(caso)
        	self.label_santo.setText(animale)

    def onClicked(self):
        self.flag = True
        self.update()


    

    def paintEvent(self, e):
      qp = QPainter(self)
      pixmap = QPixmap("PAPA.jpg")
      #qp.drawPixmap(400,100, pixmap)
      if self.flag:
          qp.begin(self)
          self.drawText(qp)
          qp.end()
    
    def drawText(self, qp):
        qp=QPainter(self)
        qp.drawText(450,300,"CIAO")
        qp.restore() # restore the QPainter config            
        qp.drawRect(100, 150, 170, 170)

    def doAnimation(self):
        self.anim = QPropertyAnimation(self.frame, b"geometry")
        self.anim.setDuration(10000)
        self.anim.setStartValue(QRect(0, 0, 100, 30))
        self.anim.setEndValue(QRect(250, 250, 100, 30))
        self.anim.start()
       

    

app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()