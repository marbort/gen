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
        self.size=QtCore.QSize(120,100)
        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        vbox = QVBoxLayout()
        grid = QGridLayout()
        self.flag=False
        #grid.setRowStretch(4,3)
        #grid.setRowStretch(5,3)
        self.label = QLabel(self)
        self.label.setFont(QtGui.QFont("Sanserif", 15))
        self.label_an = QLabel(self)
        self.label_an.setFont(QtGui.QFont("Sanserif", 15))
        self.label_an.setAlignment(QtCore.Qt.AlignCenter)
        self.dial = QDial()
        self.dial.setMinimum(0)
        self.dial.setMaximum(515)
        self.dial.setValue(0)
        self.dial.setMinimumSize(QtCore.QSize(150, 150))
        self.dial.valueChanged.connect(self.dialer_changed)
        #self.dial.setAlignment(QtCore.Qt.AlignCenter)
        self.spin=QPushButton(self)
        self.spin.setText("Choose Expression")
        self.draw=QPushButton(self)
        self.draw.setText("Draw")
        self.img1=QLabel(self)
        self.img1.setText("1")
        self.img1.setAlignment(QtCore.Qt.AlignCenter)
        self.movie1 = QtGui.QMovie("gatto-attento.gif")
        self.img1.setMovie(self.movie1)
        self.movie1.setScaledSize(self.size)
        self.movie1.start()
        self.img2=QLabel(self)
        self.img2.setText("2")
        self.img2.setAlignment(QtCore.Qt.AlignCenter)
        self.movie2 = QtGui.QMovie("72.gif")
        self.img2.setMovie(self.movie2)
        self.movie2.setScaledSize(self.size)
        self.movie2.start()
        self.img3=QLabel(self)
        self.img3.setText("3")
        self.img3.setAlignment(QtCore.Qt.AlignCenter)
        self.movie3 = QtGui.QMovie("GoldenBrilliantHartebeest-small.gif")
        self.img3.setMovie(self.movie3)
        self.movie3.setScaledSize(self.size)
        self.movie3.start()
        self.img4=QLabel(self)
        self.img4.setText("4")
        self.img4.setAlignment(QtCore.Qt.AlignCenter)
        self.movie4 = QtGui.QMovie("leone.gif")
        self.img4.setMovie(self.movie4)
        self.movie4.setScaledSize(self.size)
        self.movie4.start()
        self.img5=QLabel(self)
        self.img5.setText("5")
        self.img5.setAlignment(QtCore.Qt.AlignCenter)
        self.movie5 = QtGui.QMovie("suricati.gif")
        self.img5.setMovie(self.movie5)
        self.movie5.setScaledSize(self.size)
        self.movie5.start()
        self.img6=QLabel(self)
        self.img6.setText("6")
        self.img6.setAlignment(QtCore.Qt.AlignCenter)
        self.movie6 = QtGui.QMovie("lemure.gif")
        self.img6.setMovie(self.movie6)
        self.movie6.setScaledSize(self.size)
        self.movie6.start()
        self.img7=QLabel(self)
        self.img7.setText("7")
        self.movie7 = QtGui.QMovie("armadillo.gif")
        self.img7.setMovie(self.movie7)
        self.movie7.setScaledSize(self.size)
        self.movie7.start()
        self.img7.setAlignment(QtCore.Qt.AlignCenter)
        self.img8=QLabel(self)
        self.img8.setText("8")
        self.img8.setAlignment(QtCore.Qt.AlignCenter)
        self.movie8 = QtGui.QMovie("coniglio.gif")
        self.img8.setMovie(self.movie8)
        self.movie8.setScaledSize(self.size)
        self.movie8.start()

        self.Dio=QCheckBox(self)
        self.Dio.setText("Dio")
        self.Madonna=QCheckBox(self)
        self.Madonna.setText("La Madonna")
        self.Santo=QCheckBox(self)
        self.Santo.setText("Un santo a caso")
        #for i in range(1,9):
         #   self.label2="img"+str(i)
          #  self.label2.setAlignment(QtCore.Qt.AlignCenter)
           # print(label)
        self.santo_group=QButtonGroup(self)
        self.santo_group.addButton(self.Dio)
        self.santo_group.addButton(self.Madonna)
        self.santo_group.addButton(self.Santo)

        self.papa=QLabel(self)
        self.pixmap=QPixmap("PAPA.jpg")
        self.papa.setPixmap(self.pixmap)



        grid.addWidget(self.img1,1,1)
        grid.addWidget(self.img2,1,2)
        grid.addWidget(self.img3,1,3)
        grid.addWidget(self.img4,2,1)
        grid.addWidget(self.img5,2,3)
        grid.addWidget(self.img6,3,1)
        grid.addWidget(self.img7,3,2)
        grid.addWidget(self.img8,3,3)
        grid.addWidget(self.dial,2,2)
        grid.addWidget(self.label,4,1,1,1)
        grid.addWidget(self.label_an,4,2,1,2)
        grid.addWidget(self.spin,6,1,1,3)
        grid.addWidget(self.Dio,5,1)
        grid.addWidget(self.Madonna,5,2)
        grid.addWidget(self.Santo,5,3)
        grid.addWidget(self.papa,1,4,3,3)
        grid.addWidget(self.draw,6,4,1,3)
        self.setLayout(grid)
        #grid.setAlignment(QtCore.Qt.AlignCenter)
        self.show()

        with open('animali.json', 'r') as f:
           self.animal_dict = json.load(f)

        self.spin.clicked.connect(self.change_value)
        self.draw.clicked.connect(self.onClicked)

    def dialer_changed(self):
        getValue = self.dial.value()
        self.label.setText("Value: " + str(getValue))
        osac=str(random.randint(1,515))
        self.animale=self.animal_dict.get(osac)
        self.label_an.setText(self.animale)

    def change_value(self):
           caso=random.randint(1,515)
           self.dial.setValue(caso)
    def onClicked(self):
        self.flag = True
        #self.papa.setPixmap(self.pixmap)
        self.update()

    def paintEvent(self, paint_event):
      if self.flag:
        pixmap2=QPixmap("PAPA.jpg")
        painter = QtGui.QPainter()
        painter.begin(pixmap2)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        painter.setFont(font)
        if self.Dio.isChecked():
           painter.drawText(330, 60, "Dio "+self.animale)
        elif self.Madonna.isChecked():
            painter.drawText(300, 60, "Madonna " +self.animale)
        
        painter.end()
        self.papa.setPixmap(pixmap2)
        
       
           


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())