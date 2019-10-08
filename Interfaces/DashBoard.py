# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\DashBoard.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from Interfaces.FrequencyDistribution1 import Ui_FD


class Ui_DashBoard(object):
    def jump_FDistribution(self):
        self.FD = QtWidgets.QDialog()
        self.ui = Ui_FD()
        self.ui.setupUi(self.FD)
        self.FD.show()

    def jump_Comparison(self):
        pass
    def jump_Relating(self):
        pass

    def setupUi(self, DashBoard):
        DashBoard.setObjectName("DashBoard")
        DashBoard.resize(961, 681)
        self.label = QtWidgets.QLabel(DashBoard)
        self.label.setGeometry(QtCore.QRect(0, 0, 961, 681))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../Images/girl.jpg"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(DashBoard)
        self.label_2.setGeometry(QtCore.QRect(190, 40, 591, 81))
        self.label_2.setObjectName("label_2")
        self.Frequency = QtWidgets.QPushButton(DashBoard)
        self.Frequency.setGeometry(QtCore.QRect(80, 190, 261, 71))
        self.Frequency.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 178, 78);\n"
"background-color: rgb(0, 0, 0);")
        self.Frequency.setObjectName("Frequency")
        self.Relating = QtWidgets.QPushButton(DashBoard)
        self.Relating.setGeometry(QtCore.QRect(180, 280, 261, 71))
        self.Relating.setStyleSheet("color: rgb(255, 178, 78);\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 0, 0);")
        self.Relating.setObjectName("Relating")
        self.Comparison = QtWidgets.QPushButton(DashBoard)
        self.Comparison.setGeometry(QtCore.QRect(80, 370, 261, 71))
        self.Comparison.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 0, 0);color: rgb(255, 178, 78);\n"
"")
        self.Comparison.setObjectName("Comparison")
###
        self.Frequency.clicked.connect(self.jump_FDistribution)
        self.Comparison.clicked.connect(self.jump_Comparison)
        self.Relating.clicked.connect(self.jump_Relating)
###
        self.retranslateUi(DashBoard)
        QtCore.QMetaObject.connectSlotsByName(DashBoard)

    def retranslateUi(self, DashBoard):
        _translate = QtCore.QCoreApplication.translate
        DashBoard.setWindowTitle(_translate("DashBoard", "DashBoard"))
        self.label_2.setText(_translate("DashBoard", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">World Happiness Report</span></p></body></html>"))
        self.Frequency.setToolTip(_translate("DashBoard", "Histograms"))
        self.Frequency.setText(_translate("DashBoard", "Frequency Distribution"))
        self.Relating.setToolTip(_translate("DashBoard", "ScatterPlots"))
        self.Relating.setText(_translate("DashBoard", "Relating the parameters"))
        self.Comparison.setToolTip(_translate("DashBoard", "LineCharts"))
        self.Comparison.setText(_translate("DashBoard", "Comparison"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DashBoard = QtWidgets.QDialog()
    ui = Ui_DashBoard()
    ui.setupUi(DashBoard)
    DashBoard.show()
    sys.exit(app.exec_())

