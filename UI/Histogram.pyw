# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Histogram.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

import pymsgbox
from PyQt5 import QtCore, QtGui, QtWidgets
import UI.DataFrames as d

class Ui_Histogram(object):
    def plot_histogram(self):

        buttons = ['EC', 'FA', 'HE', 'FR', 'TR', 'GN']
        features = [self.EC.isChecked(), self.FA.isChecked(), self.HE.isChecked(), self.FR.isChecked(),
                    self.TR.isChecked(), self.GN.isChecked()]

        which = ""

        for i in range(len(features)):
            if features[i]:
                which = buttons[i]
                break;

        if self.y2015.isChecked():
            df = d.var_2015
            p = df[which]
            fig, axs = d.plt.subplots(1,2)
            fig.canvas.set_window_title('2015  [%s]'%which)
            axs[0].hist(x=p, bins='auto', color='#0504aa',alpha=0.7, rwidth=0.85)
            axs[0].set(xlabel="%s" % which, ylabel='No. of Countries',
                       title='Frequency Distribution over %s' % which)

            d.sns.set_style('darkgrid')
            d.sns.distplot(p)
            d.plt.title("KDE over %s" %which)
            d.plt.show()

        elif self.y2016.isChecked():
            df = d.var_2016
            p = df[which]
            fig, axs = d.plt.subplots(1, 2)
            fig.canvas.set_window_title('2016  [%s]' % which)
            axs[0].hist(x=p, bins='auto', color='#0504aa', alpha=0.7, rwidth=0.85)
            axs[0].set(xlabel="%s" % which, ylabel='No. of Countries',
                       title='Frequency Distribution over %s' % which)

            d.sns.set_style('darkgrid')
            d.sns.distplot(p)
            d.plt.title("KDE over %s" % which)
            d.plt.show()

        elif self.y2017.isChecked():
            df = d.var_2017
            p = df[which]
            fig, axs = d.plt.subplots(1, 2)
            fig.canvas.set_window_title('2017  [%s]' % which)
            axs[0].hist(x=p, bins='auto', color='#0504aa', alpha=0.7, rwidth=0.85)
            axs[0].set(xlabel="%s" % which, ylabel='No. of Countries',
                       title='Frequency Distribution over %s' % which)

            d.sns.set_style('darkgrid')
            d.sns.distplot(p)
            d.plt.title("KDE over %s" % which)
            d.plt.show()


    def setupUi(self, Histogram):
        Histogram.setObjectName("Histogram")
        Histogram.resize(1920, 1080)
        Histogram.setMinimumSize(QtCore.QSize(1920, 1080))
        Histogram.setMaximumSize(QtCore.QSize(1920, 1080))
        Histogram.showMaximized()
        self.centralwidget = QtWidgets.QWidget(Histogram)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, -30, 1920, 1080))
        self.label.setMinimumSize(QtCore.QSize(1920, 1080))
        self.label.setMaximumSize(QtCore.QSize(1920, 1080))
        self.label.setStyleSheet("background-color: rgb(12, 13, 22);")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../Images/histogram.png"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(90, 150, 541, 141))
        self.label_2.setStyleSheet("font: 90pt \"Kokila\";\n"
"color: rgb(240, 240, 240);")
        self.label_2.setObjectName("label_2")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(1456, 81, 291, 281))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.verticalLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 24pt \"Kokila\";")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.y2015 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.y2015.setStyleSheet("font: 75 26pt \"Kokila\";\n"
"color: rgb(255, 255, 255);")
        self.y2015.setObjectName("y2015")
        self.gridLayout.addWidget(self.y2015, 1, 0, 1, 1)
        self.y2016 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.y2016.setStyleSheet("font: 75 26pt \"Kokila\";\n"
"color: rgb(255, 255, 255);")
        self.y2016.setObjectName("y2016")
        self.gridLayout.addWidget(self.y2016, 2, 0, 1, 1)
        self.y2017 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.y2017.setStyleSheet("font: 75 26pt \"Kokila\";\n"
"color: rgb(255, 255, 255);")
        self.y2017.setObjectName("y2017")
        self.gridLayout.addWidget(self.y2017, 3, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(1320, 435, 561, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(1340, 524, 531, 311))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.verticalLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.EC = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.EC.setStyleSheet("font: 75 26pt \"Kokila\";\n"
"color: rgb(255, 255, 255);")
        self.EC.setObjectName("EC")
        self.gridLayout_2.addWidget(self.EC, 1, 0, 1, 1)
        self.HE = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.HE.setStyleSheet("font: 75 26pt \"Kokila\";\n"
"color: rgb(255, 255, 255);")
        self.HE.setObjectName("HE")
        self.gridLayout_2.addWidget(self.HE, 3, 0, 1, 1)
        self.FA = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.FA.setStyleSheet("font: 75 26pt \"Kokila\";\n"
"color: rgb(255, 255, 255);")
        self.FA.setObjectName("FA")
        self.gridLayout_2.addWidget(self.FA, 2, 0, 1, 1)
        self.FR = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.FR.setStyleSheet("font: 75 26pt \"Kokila\";\n"
"color: rgb(255, 255, 255);")
        self.FR.setObjectName("FR")
        self.gridLayout_2.addWidget(self.FR, 1, 1, 1, 1)
        self.TR = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.TR.setStyleSheet("font: 75 26pt \"Kokila\";\n"
"color: rgb(255, 255, 255);")
        self.TR.setObjectName("TR")
        self.gridLayout_2.addWidget(self.TR, 2, 1, 1, 1)
        self.GN = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.GN.setStyleSheet("font: 75 26pt \"Kokila\";\n"
"color: rgb(255, 255, 255);")
        self.GN.setObjectName("GN")
        self.gridLayout_2.addWidget(self.GN, 3, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 24pt \"Kokila\";")
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 2)
        self.Plot = QtWidgets.QPushButton(self.centralwidget)
        self.Plot.setGeometry(QtCore.QRect(1470, 910, 291, 71))
        self.Plot.setStyleSheet("background-color: rgb(50, 197, 17);\n"
"font: 36pt \"Kokila\";\n"
"border-radius: 30px")
        self.Plot.setObjectName("Plot")
        Histogram.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Histogram)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1920, 26))
        self.menubar.setObjectName("menubar")
        Histogram.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Histogram)
        self.statusbar.setObjectName("statusbar")
        Histogram.setStatusBar(self.statusbar)

#####
        self.Plot.clicked.connect(self.plot_histogram)
#####

        self.retranslateUi(Histogram)
        QtCore.QMetaObject.connectSlotsByName(Histogram)

    def retranslateUi(self, Histogram):
        _translate = QtCore.QCoreApplication.translate
        Histogram.setWindowTitle(_translate("Histogram", "Frequency Distribution"))
        self.label_2.setText(_translate("Histogram", "Histogram"))
        self.label_3.setText(_translate("Histogram", "<html><head/><body><p align=\"center\"><span style=\" font-size:28pt;\">Select Year</span></p></body></html>"))
        self.y2015.setText(_translate("Histogram", "         2015"))
        self.y2016.setText(_translate("Histogram", "         2016"))
        self.y2017.setText(_translate("Histogram", "         2017"))
        self.EC.setText(_translate("Histogram", "         Economy"))
        self.HE.setText(_translate("Histogram", "         Health"))
        self.FA.setText(_translate("Histogram", "         Family"))
        self.FR.setText(_translate("Histogram", "         Freedom"))
        self.TR.setText(_translate("Histogram", "         Trust"))
        self.GN.setText(_translate("Histogram", "         Generosity"))
        self.label_4.setText(_translate("Histogram", "<html><head/><body><p align=\"center\"><span style=\" font-size:28pt;\">Select the feature</span></p></body></html>"))
        self.Plot.setText(_translate("Histogram", "PLOT"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Histogram = QtWidgets.QMainWindow()
    ui = Ui_Histogram()
    ui.setupUi(Histogram)
    Histogram.show()
    sys.exit(app.exec_())

