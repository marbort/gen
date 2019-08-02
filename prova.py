from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtCore
import sys, time, random, json

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "PyQt5 Scroll Bar"
        self.top = 200
        self.left = 500
        self.width = 400
        self.height = 300
        self.label=QLabel(self)

        text="Ciao"

        pixmap = QPixmap("PAPA.jpg")
        painter = QPainter()
        painter.begin(pixmap)
#painter.setFont(font)
        painter.drawText(100,100, text)
        painter.end()
        
        self.label.setPixmap(pixmap)
        self.show()


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())