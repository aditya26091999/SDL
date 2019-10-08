# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\FrequencyDistribution1.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_FD(object):
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
        self.label.raise_()
        self.gridLayoutWidget.raise_()

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


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FD = QtWidgets.QDialog()
    ui = Ui_FD()
    ui.setupUi(FD)
    FD.show()
    sys.exit(app.exec_())

