# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FrequencyDistribution1.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from Code.Visualisation import var_2015, var_2016, var_2017
import pymsgbox

class Ui_FD(object):
    yr = [var_2015,var_2016,var_2017]
    ft = ['EC','FA','HE','TR','FR','GN']
    year=""
    feat=""

    def plothisto(self):
        pymsgbox.alert(self.feat)

    def select_yr(self,df):
        if df == 0:
            self.year = self.yr[0]
        elif df == 1:
            self.year = self.yr[1]
        elif df == 2:
            self.year = self.yr[2]


    def select_ft(self,ft1):
        if ft1 == 0:
            self.feat = self.ft[0]
        elif ft1 == 1:
            self.feat = self.ft[1]
        elif ft1 == 2:
            self.feat = self.ft[2]
        elif ft1 == 3:
            self.feat = self.ft[3]
        elif ft1 == 4:
            self.feat = self.ft[4]
        elif ft1 == 5:
            self.feat = self.ft[5]

    def setupUi(self, FD):
        FD.setObjectName("FD")
        FD.resize(958, 463)
        FD.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.gridLayoutWidget = QtWidgets.QWidget(FD)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 30, 581, 411))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.Economy = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.Economy.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";color: rgb(255, 255, 255);")
        self.Economy.setObjectName("Economy")
        self.gridLayout_2.addWidget(self.Economy, 0, 0, 1, 1)
        self.Family = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.Family.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";color: rgb(255, 255, 255);")
        self.Family.setObjectName("Family")
        self.gridLayout_2.addWidget(self.Family, 1, 0, 1, 1)
        self.Health = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.Health.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";color: rgb(255, 255, 255);\n"
"")
        self.Health.setObjectName("Health")
        self.gridLayout_2.addWidget(self.Health, 0, 1, 1, 1)
        self.Trust = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.Trust.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.Trust.setObjectName("Trust")
        self.gridLayout_2.addWidget(self.Trust, 2, 0, 1, 1)
        self.Freedom = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.Freedom.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";color: rgb(255, 255, 255);")
        self.Freedom.setObjectName("Freedom")
        self.gridLayout_2.addWidget(self.Freedom, 1, 1, 1, 1)
        self.Generosity = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.Generosity.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";color: rgb(255, 255, 255);")
        self.Generosity.setObjectName("Generosity")
        self.gridLayout_2.addWidget(self.Generosity, 2, 1, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 5, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.y2015 = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.y2015.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 14pt \"MS Shell Dlg 2\";")
        self.y2015.setObjectName("y2015")
        self.verticalLayout.addWidget(self.y2015)
        self.y2016 = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.y2016.setStyleSheet("color: rgb(255, 255, 255);font: 14pt \"MS Shell Dlg 2\";")
        self.y2016.setObjectName("y2016")
        self.verticalLayout.addWidget(self.y2016)
        self.y2017 = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.y2017.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.y2017.setObjectName("y2017")
        self.verticalLayout.addWidget(self.y2017)
        self.gridLayout.addLayout(self.verticalLayout, 3, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setStyleSheet("color: rgb(88, 254, 208);")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setStyleSheet("color: rgb(70, 246, 208);")
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setStyleSheet("color: rgb(70, 246, 208);")
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(FD)
        self.label.setGeometry(QtCore.QRect(370, 10, 581, 441))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../Images/frequency.jpg"))
        self.label.setObjectName("label")
        self.go = QtWidgets.QPushButton(FD)
        self.go.setGeometry(QtCore.QRect(720, 380, 131, 41))
        self.go.setStyleSheet("background-color: rgb(84, 251, 205);\n"
"font: 16pt \"MS Shell Dlg 2\";")
        self.go.setObjectName("go")
        self.label.raise_()
        self.gridLayoutWidget.raise_()
        self.go.raise_()
######

        self.go.clicked.connect(self.plothisto)

        #####
        self.Economy.clicked.connect(self.select_ft,0)
        self.Family.clicked.connect(self.select_ft,1)
        self.Health.clicked.connect(self.select_ft,2)
        self.Trust.clicked.connect(self.select_ft,3)
        self.Freedom.clicked.connect(self.select_ft,4)
        self.Generosity.clicked.connect(self.select_ft,5)
        ####

        ####
        self.y2015.clicked.connect(self.select_yr,0)
        self.y2016.clicked.connect(self.select_yr,1)
        self.y2017.clicked.connect(self.select_yr,2)
        ####

######
        self.retranslateUi(FD)
        QtCore.QMetaObject.connectSlotsByName(FD)

    def retranslateUi(self, FD):
        _translate = QtCore.QCoreApplication.translate
        FD.setWindowTitle(_translate("FD", "Dialog"))
        self.Economy.setText(_translate("FD", "Economy"))
        self.Family.setText(_translate("FD", "Family"))
        self.Health.setText(_translate("FD", "Health"))
        self.Trust.setText(_translate("FD", "Trust on Government"))
        self.Freedom.setText(_translate("FD", "Freedom"))
        self.Generosity.setText(_translate("FD", "Generosity"))
        self.y2015.setText(_translate("FD", "2015"))
        self.y2016.setText(_translate("FD", "2016"))
        self.y2017.setText(_translate("FD", "2017"))
        self.label_2.setText(_translate("FD", "<html><head/><body><p align=\"center\"><span style=\" font-size:36pt;\">Histogram</span></p></body></html>"))
        self.label_4.setText(_translate("FD", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600;\">Select the parameter</span></p></body></html>"))
        self.label_5.setText(_translate("FD", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600;\">Select the year</span></p></body></html>"))
        self.go.setText(_translate("FD", "GO!"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FD = QtWidgets.QDialog()
    ui = Ui_FD()
    ui.setupUi(FD)
    FD.show()
    sys.exit(app.exec_())

