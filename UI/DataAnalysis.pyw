# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DataAnalysis.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from UI.AdvancedGraphs import Ui_AdvancedGraphs
from UI.Histogram import Ui_Histogram
from UI.LineChart import Ui_LineChart
from UI.ScatterPlot import Ui_Relation


class Ui_DataAnalysis(object):
    def jump_Frequency(self):
        self.Histogram = QtWidgets.QMainWindow()
        self.ui = Ui_Histogram()
        self.ui.setupUi(self.Histogram)
        self.Histogram.show()

    def jump_Relations(self):
        self.Relation = QtWidgets.QMainWindow()
        self.ui = Ui_Relation()
        self.ui.setupUi(self.Relation)
        self.Relation.show()
    def jump_Comparision(self):
        self.LineChart = QtWidgets.QMainWindow()
        self.ui = Ui_LineChart()
        self.ui.setupUi(self.LineChart)
        self.LineChart.show()
    def jump_Next(self):
        self.AdvancedGraphs = QtWidgets.QMainWindow()
        self.ui = Ui_AdvancedGraphs()
        self.ui.setupUi(self.AdvancedGraphs)
        self.AdvancedGraphs.show()

    def setupUi(self, DataAnalysis):
        DataAnalysis.setObjectName("DataAnalysis")
        DataAnalysis.resize(1920, 1080)
        DataAnalysis.setMinimumSize(QtCore.QSize(1920, 1080))
        DataAnalysis.setMaximumSize(QtCore.QSize(1920, 1080))
        DataAnalysis.setStyleSheet("background-color: rgb(255, 141, 114);")
        DataAnalysis.showMaximized()
        self.centralwidget = QtWidgets.QWidget(DataAnalysis)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(640, 60, 1920, 1080))
        self.label.setMinimumSize(QtCore.QSize(1920, 1080))
        self.label.setMaximumSize(QtCore.QSize(1920, 1080))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../Images/chart.png"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(130, 30, 1831, 131))
        self.label_2.setStyleSheet("font: 90pt \"Kokila\";")
        self.label_2.setObjectName("label_2")
        self.Frequency = QtWidgets.QPushButton(self.centralwidget)
        self.Frequency.setGeometry(QtCore.QRect(110, 340, 341, 131))
        self.Frequency.setStyleSheet("background-color: rgb(98, 213, 233);\n"
"font: 35pt \"Kokila\";")
        self.Frequency.setObjectName("Frequency")
        self.Relations = QtWidgets.QPushButton(self.centralwidget)
        self.Relations.setGeometry(QtCore.QRect(210, 570, 341, 131))
        self.Relations.setStyleSheet("font: 35pt \"Kokila\";\n"
"background-color: rgb(240, 239, 148);")
        self.Relations.setObjectName("Relations")
        self.Comparision = QtWidgets.QPushButton(self.centralwidget)
        self.Comparision.setGeometry(QtCore.QRect(110, 800, 341, 131))
        self.Comparision.setStyleSheet("font: 35pt \"Kokila\";\n"
"background-color: rgb(88, 249, 162);")
        self.Comparision.setObjectName("Comparision")
        self.Next = QtWidgets.QPushButton(self.centralwidget)
        self.Next.setGeometry(QtCore.QRect(1630, 940, 111, 61))
        self.Next.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 16pt \"Kokila\";\n"
"border-radius:30px\n"
"")
        self.Next.setObjectName("Next")
        DataAnalysis.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(DataAnalysis)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1920, 26))
        self.menubar.setObjectName("menubar")
        DataAnalysis.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(DataAnalysis)
        self.statusbar.setObjectName("statusbar")
        DataAnalysis.setStatusBar(self.statusbar)
####
        self.Frequency.clicked.connect(self.jump_Frequency)
        self.Comparision.clicked.connect(self.jump_Comparision)
        self.Relations.clicked.connect(self.jump_Relations)
        self.Next.clicked.connect(self.jump_Next)
####

        self.retranslateUi(DataAnalysis)
        QtCore.QMetaObject.connectSlotsByName(DataAnalysis)

    def retranslateUi(self, DataAnalysis):
        _translate = QtCore.QCoreApplication.translate
        DataAnalysis.setWindowTitle(_translate("DataAnalysis", "DataAnalysis"))
        self.label_2.setText(_translate("DataAnalysis", "Visualisation & Pattern Finding"))
        self.Frequency.setToolTip(_translate("DataAnalysis", "<html><head/><body><p><span style=\" font-size:16pt;\">Histograms</span></p></body></html>"))
        self.Frequency.setText(_translate("DataAnalysis", "Frequency"))
        self.Relations.setToolTip(_translate("DataAnalysis", "<html><head/><body><p><span style=\" font-size:16pt;\">ScatterPlots</span></p></body></html>"))
        self.Relations.setText(_translate("DataAnalysis", "Relations"))
        self.Comparision.setToolTip(_translate("DataAnalysis", "<html><head/><body><p><span style=\" font-size:16pt;\">Line Charts</span></p></body></html>"))
        self.Comparision.setText(_translate("DataAnalysis", "Comparisions"))
        self.Next.setText(_translate("DataAnalysis", "Next"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DataAnalysis = QtWidgets.QMainWindow()
    ui = Ui_DataAnalysis()
    ui.setupUi(DataAnalysis)
    DataAnalysis.show()
    sys.exit(app.exec_())

