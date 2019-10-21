# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DatasetExplore.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
import pymsgbox
import os
from PyQt5 import QtCore, QtGui, QtWidgets

from UI.DataAnalysis import Ui_DataAnalysis


class Ui_DatasetExplore(object):
    def jump_showexcel(self,which):
        if which == 1:
           os.startfile(r'D:\Projects\SDL_WHR\2015.csv')
        elif which == 2:
            os.startfile(r'D:\Projects\SDL_WHR\2016.csv')
        elif which == 3:
            os.startfile(r'D:\Projects\SDL_WHR\2017.csv')

    def jump_DataAnalysis(self):
        self.DataAnalysis = QtWidgets.QMainWindow()
        self.ui = Ui_DataAnalysis()
        self.ui.setupUi(self.DataAnalysis)
        self.DataAnalysis.show()

    def setupUi(self, DatasetExplore):
        DatasetExplore.setObjectName("DatasetExplore")
        DatasetExplore.resize(1920, 1080)
        DatasetExplore.setMinimumSize(QtCore.QSize(1920, 1080))
        DatasetExplore.setMaximumSize(QtCore.QSize(1920, 1080))
        DatasetExplore.showMaximized()
        self.centralwidget = QtWidgets.QWidget(DatasetExplore)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1920, 1080))
        self.label.setMinimumSize(QtCore.QSize(1920, 1080))
        self.label.setMaximumSize(QtCore.QSize(1920, 1080))
        self.label.setToolTip("")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../Images/world.jpg"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(590, 60, 791, 101))
        self.label_2.setStyleSheet("font: 75 90pt \"Kokila\";\n"
"background-color: rgb(255, 255, 255,5%);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(550, 720, 121, 91))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("../Images/location.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(330, 380, 121, 91))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("../Images/location.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(970, 670, 121, 91))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("../Images/location.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(1540, 720, 121, 91))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("../Images/location.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(1230, 420, 121, 91))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("../Images/location.png"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(930, 260, 121, 91))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("../Images/location.png"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(270, 340, 201, 31))
        self.label_9.setStyleSheet("font: 75 18pt \"MS Shell Dlg 2\";")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(500, 680, 201, 31))
        self.label_10.setStyleSheet("font: 75 18pt \"MS Shell Dlg 2\";")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(960, 630, 91, 31))
        self.label_11.setStyleSheet("font: 75 18pt \"MS Shell Dlg 2\";")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(1520, 690, 131, 31))
        self.label_12.setStyleSheet("font: 75 18pt \"MS Shell Dlg 2\";")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(1250, 380, 61, 31))
        self.label_13.setStyleSheet("font: 75 18pt \"MS Shell Dlg 2\";")
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(910, 210, 131, 51))
        self.label_14.setStyleSheet("font: 75 18pt \"MS Shell Dlg 2\";")
        self.label_14.setObjectName("label_14")
        self.button2015 = QtWidgets.QPushButton(self.centralwidget)
        self.button2015.setGeometry(QtCore.QRect(120, 710, 141, 61))
        self.button2015.setAcceptDrops(False)
        self.button2015.setStatusTip("")
        self.button2015.setWhatsThis("")
        self.button2015.setStyleSheet("font: 24pt \"Kokila\";\n"
"background-color: rgb(6, 139, 214);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 30px;\n"
"border-color: black;\n"
"padding: 4px;")
        self.button2015.setFlat(False)
        self.button2015.setObjectName("button2015")
        self.button2016 = QtWidgets.QPushButton(self.centralwidget)
        self.button2016.setGeometry(QtCore.QRect(620, 470, 141, 61))
        self.button2016.setStyleSheet("font: 24pt \"Kokila\";\n"
"background-color: rgb(6, 139, 214);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 30px;\n"
"border-color: black;\n"
"padding: 4px;")
        self.button2016.setFlat(False)
        self.button2016.setObjectName("button2016")
        self.button2017 = QtWidgets.QPushButton(self.centralwidget)
        self.button2017.setGeometry(QtCore.QRect(1260, 670, 141, 61))
        self.button2017.setStyleSheet("font: 24pt \"Kokila\";\n"
"background-color: rgb(6, 139, 214);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 30px;\n"
"border-color: black;\n"
"padding: 4px;")
        self.button2017.setFlat(False)
        self.button2017.setObjectName("button2017")
        self.DataAnalysis = QtWidgets.QPushButton(self.centralwidget)
        self.DataAnalysis.setGeometry(QtCore.QRect(1070, 920, 441, 91))
        self.DataAnalysis.setStyleSheet("font: 24pt \"Kokila\";\n"
"background-color: rgb(176, 176, 176);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 30px;\n"
"border-color: black;\n"
"padding: 4px;")
        self.DataAnalysis.setFlat(False)
        self.DataAnalysis.setObjectName("DataAnalysis")
        DatasetExplore.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(DatasetExplore)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1920, 26))
        self.menubar.setObjectName("menubar")
        DatasetExplore.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(DatasetExplore)
        self.statusbar.setObjectName("statusbar")
        DatasetExplore.setStatusBar(self.statusbar)
####
        self.button2015.clicked.connect(lambda : self.jump_showexcel(1))
        self.button2016.clicked.connect(lambda : self.jump_showexcel(2))
        self.button2017.clicked.connect(lambda : self.jump_showexcel(3))
        self.DataAnalysis.clicked.connect(self.jump_DataAnalysis)
####
        self.retranslateUi(DatasetExplore)
        QtCore.QMetaObject.connectSlotsByName(DatasetExplore)

    def retranslateUi(self, DatasetExplore):
        _translate = QtCore.QCoreApplication.translate
        DatasetExplore.setWindowTitle(_translate("DatasetExplore", "DatasetExplore"))
        self.label_2.setText(_translate("DatasetExplore", "Worldwide Data"))
        self.label_9.setText(_translate("DatasetExplore", "North America"))
        self.label_10.setText(_translate("DatasetExplore", "South America"))
        self.label_11.setText(_translate("DatasetExplore", "Africa"))
        self.label_12.setText(_translate("DatasetExplore", "Australia"))
        self.label_13.setText(_translate("DatasetExplore", "Asia"))
        self.label_14.setText(_translate("DatasetExplore", "Europe"))
        self.button2015.setToolTip(_translate("DatasetExplore", "<html><head/><body><p><span style=\" font-size:16pt; font-style:italic; color:#ffffff;\">2015 World Happiness Report dataset </span></p></body></html>"))
        self.button2015.setText(_translate("DatasetExplore", "2015"))
        self.button2016.setToolTip(_translate("DatasetExplore", "<html><head/><body><p><span style=\" font-size:16pt; font-style:italic; color:#ffffff;\">2016 World Happiness Report dataset </span></p></body></html>"))
        self.button2016.setText(_translate("DatasetExplore", "2016"))
        self.button2017.setToolTip(_translate("DatasetExplore", "<html><head/><body><p><span style=\" font-size:16pt; font-style:italic; color:#ffffff;\">2017 World Happiness Report dataset </span></p></body></html>"))
        self.button2017.setText(_translate("DatasetExplore", "2017"))
        self.DataAnalysis.setToolTip(_translate("DatasetExplore", "<html><head/><body><p><span style=\" font-size:16pt; font-style:italic;\">Visualisation and Analysis</span></p></body></html>"))
        self.DataAnalysis.setText(_translate("DatasetExplore", "Data Analysis"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DatasetExplore = QtWidgets.QMainWindow()
    ui = Ui_DatasetExplore()
    ui.setupUi(DatasetExplore)
    DatasetExplore.show()
    sys.exit(app.exec_())

