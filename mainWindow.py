# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(578, 507)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.checkBox_4 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_4.setObjectName("checkBox_4")
        self.buttonGroup = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.checkBox_4)
        self.gridLayout.addWidget(self.checkBox_4, 1, 3, 1, 1)
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setObjectName("checkBox_2")
        self.buttonGroup.addButton(self.checkBox_2)
        self.gridLayout.addWidget(self.checkBox_2, 1, 1, 1, 1)
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setObjectName("checkBox")
        self.buttonGroup.addButton(self.checkBox)
        self.gridLayout.addWidget(self.checkBox, 1, 0, 1, 1)
        self.checkBox_5 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_5.setObjectName("checkBox_5")
        self.buttonGroup_2 = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup_2.setObjectName("buttonGroup_2")
        self.buttonGroup_2.addButton(self.checkBox_5)
        self.gridLayout.addWidget(self.checkBox_5, 5, 0, 1, 2)
        self.checkBox_3 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_3.setObjectName("checkBox_3")
        self.buttonGroup.addButton(self.checkBox_3)
        self.gridLayout.addWidget(self.checkBox_3, 1, 2, 1, 1)
        self.checkBox_6 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_6.setObjectName("checkBox_6")
        self.buttonGroup_2.addButton(self.checkBox_6)
        self.gridLayout.addWidget(self.checkBox_6, 5, 2, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 8, 0, 1, 4)
        self.checkBox_7 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_7.setObjectName("checkBox_7")
        self.buttonGroup_2.addButton(self.checkBox_7)
        self.gridLayout.addWidget(self.checkBox_7, 5, 3, 1, 1)
        self.label_img = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_img.setFont(font)
        self.label_img.setAlignment(QtCore.Qt.AlignCenter)
        self.label_img.setObjectName("label_img")
        self.gridLayout.addWidget(self.label_img, 0, 1, 1, 1)
        self.dial = QtWidgets.QDial(self.centralwidget)
        self.dial.setMinimumSize(QtCore.QSize(200, 200))
        self.dial.setObjectName("dial")
        self.gridLayout.addWidget(self.dial, 0, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 578, 22))
        self.menubar.setObjectName("menubar")
        self.menuBlasphemy_Generator = QtWidgets.QMenu(self.menubar)
        self.menuBlasphemy_Generator.setObjectName("menuBlasphemy_Generator")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuBlasphemy_Generator.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.checkBox, self.checkBox_2)
        MainWindow.setTabOrder(self.checkBox_2, self.checkBox_5)
        MainWindow.setTabOrder(self.checkBox_5, self.pushButton)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.checkBox_4.setText(_translate("MainWindow", "Un Santo a caso"))
        self.checkBox_2.setText(_translate("MainWindow", "Gesù"))
        self.checkBox.setText(_translate("MainWindow", "Dio"))
        self.checkBox_5.setText(_translate("MainWindow", "Animali"))
        self.checkBox_3.setText(_translate("MainWindow", "La Madonna"))
        self.checkBox_6.setText(_translate("MainWindow", "Oggetti"))
        self.pushButton.setText(_translate("MainWindow", "Generate Blasphemy"))
        self.checkBox_7.setText(_translate("MainWindow", "Espressioni cololrite"))
        self.label_img.setText(_translate("MainWindow", "Ciao"))
        self.menuBlasphemy_Generator.setTitle(_translate("MainWindow", "Blasphemy Generator"))


import img1_rc
import img2_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
