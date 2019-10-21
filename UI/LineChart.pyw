# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LineChart.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
import pymsgbox
from PyQt5 import QtCore, QtGui, QtWidgets
import UI.DataFrames as d

class Ui_LineChart(object):

    def Load1fn(self):
        if self.y2015.isChecked():
            self.Single.clear()
            cl = d.var_2015.index.values.tolist()
            for i in cl:
                self.Single.addItem(i)
            pymsgbox.alert('Loaded 2015 dataset','Success')
        elif self.y2016.isChecked():
            self.Single.clear()
            cl = d.var_2016.index.values.tolist()
            for i in cl:
                self.Single.addItem(i)
            pymsgbox.alert('Loaded 2016 dataset', 'Success')

        elif self.y2017.isChecked():
            self.Single.clear()
            cl = d.var_2017.index.values.tolist()
            for i in cl:
                self.Single.addItem(i)
            pymsgbox.alert('Loaded 2017 dataset', 'Success')

    def Load2fn(self):
        if self.y2015.isChecked():
            self.Double1.clear()
            self.Double2.clear()
            cl = d.var_2015.index.values.tolist()
            for i in cl:
                self.Double1.addItem(i)
                self.Double2.addItem(i)
            pymsgbox.alert('Loaded 2015 dataset', 'Success')

        elif self.y2016.isChecked():
            self.Double1.clear()
            self.Double2.clear()
            cl = d.var_2016.index.values.tolist()
            for i in cl:
                self.Double1.addItem(i)
                self.Double2.addItem(i)
            pymsgbox.alert('Loaded 2016 dataset', 'Success')

        elif self.y2017.isChecked():
            self.Double1.clear()
            self.Double2.clear()
            cl = d.var_2017.index.values.tolist()
            for i in cl:
                self.Double1.addItem(i)
                self.Double2.addItem(i)
            pymsgbox.alert('Loaded 2017 dataset', 'Success')

    def Plot1fn(self):

        fig,axs = d.plt.subplots(1,1)
        fig.canvas.set_window_title('%s'%self.Single.currentText())
        c1 = d.var_2015.loc[self.Single.currentText()]
        c2 = d.var_2016.loc[self.Single.currentText()]
        c3 = d.var_2017.loc[self.Single.currentText()]

        leg = ['Economy', 'Family', 'Health', 'Freedom', 'Trust', 'Generosity']

        c1 = [c1['HR'], c1['EC'], c1['FA'], c1['HE'], c1['FR'], c1['TR'], c1['GN']]
        c2 = [c2['HR'], c2['EC'], c2['FA'], c2['HE'], c2['FR'], c2['TR'], c2['GN']]
        c3 = [c3['HR'], c3['EC'], c3['FA'], c3['HE'], c3['FR'], c3['TR'], c3['GN']]

        for i in range(1, 6):
            d.plt.plot(['2015', '2016', '2017'], [c1[i], c2[i], c3[i]], marker='o', label=leg[i])

        d.plt.title('Country level analysis of : %s' % self.Single.currentText())
        d.plt.xlabel('Year')
        d.plt.ylabel('Units')
        d.plt.legend()
        d.plt.show()


    def Plot2fn(self):
        fig, axs = d.plt.subplots(1, 2,figsize = (10,10))
        fig.canvas.set_window_title('%s vs %s'%(self.Double1.currentText(),self.Double2.currentText()))
        f = [self.Double1.currentText(),self.Double2.currentText()]
        for j in range(2):
            c1 = d.var_2015.loc[f[j]]
            c2 = d.var_2016.loc[f[j]]
            c3 = d.var_2017.loc[f[j]]

            leg = ['Economy', 'Family', 'Health', 'Freedom', 'Trust', 'Generosity']

            c1 = [c1['HR'], c1['EC'], c1['FA'], c1['HE'], c1['FR'], c1['TR'], c1['GN']]
            c2 = [c2['HR'], c2['EC'], c2['FA'], c2['HE'], c2['FR'], c2['TR'], c2['GN']]
            c3 = [c3['HR'], c3['EC'], c3['FA'], c3['HE'], c3['FR'], c3['TR'], c3['GN']]
            for i in range(1, 6):
                axs[j].plot(['2015', '2016', '2017'], [c1[i], c2[i], c3[i]], marker='o', label=leg[i])
                axs[j].legend()
            axs[j].set_title("%s" % f[j])
        for axs in axs.flat:
            axs.set(xlabel='Years', ylabel='Units')

        fig.show()

    def setupUi(self, LineChart):
        LineChart.setObjectName("LineChart")
        LineChart.resize(1920, 1080)
        LineChart.setMinimumSize(QtCore.QSize(1920, 1080))
        LineChart.setMaximumSize(QtCore.QSize(1920, 1080))
        LineChart.showMaximized()
        LineChart.setStyleSheet("background-color: rgb(230, 230, 230);\n"
"background-color: rgb(242, 242, 242);")
        self.centralwidget = QtWidgets.QWidget(LineChart)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(630, 310, 1621, 731))
        self.label.setMinimumSize(QtCore.QSize(0, 0))
        self.label.setMaximumSize(QtCore.QSize(1920, 1080))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../Images/data-3314284_1280.png"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, -10, 1941, 241))
        self.label_2.setStyleSheet("font: 72pt \"Kokila\";\n"
"background-color: rgb(218, 218, 218);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(70, 320, 731, 101))
        self.label_3.setStyleSheet("font: 48pt \"Kokila\";")
        self.label_3.setObjectName("label_3")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(80, 430, 701, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(70, 660, 731, 101))
        self.label_4.setStyleSheet("font: 48pt \"Kokila\";")
        self.label_4.setObjectName("label_4")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(80, 770, 701, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.Single = QtWidgets.QComboBox(self.centralwidget)
        self.Single.setGeometry(QtCore.QRect(200, 470, 471, 41))
        self.Single.setStyleSheet("background-color: rgb(85, 153, 255);\n"
"font: 16pt \"Kokila\";\n"
"color: rgb(255,255,255);\n"
"selection-background-color: rgb(0, 0, 0);\n"
"border : 1px solid black")
        self.Single.setObjectName("Single")
        self.Double1 = QtWidgets.QComboBox(self.centralwidget)
        self.Double1.setGeometry(QtCore.QRect(80, 870, 261, 41))
        self.Double1.setStyleSheet("background-color: rgb(85, 153, 255);\n"
"font: 16pt \"Kokila\";\n"
"color: rgb(255,255,255);\n"
"selection-background-color: rgb(0, 0, 0);\n"
"border : 1px solid black")
        self.Double1.setObjectName("Double1")
        self.Double2 = QtWidgets.QComboBox(self.centralwidget)
        self.Double2.setGeometry(QtCore.QRect(520, 870, 261, 41))
        self.Double2.setStyleSheet("background-color: rgb(85, 153, 255);\n"
"font: 16pt \"Kokila\";\n"
"color: rgb(255,255,255);\n"
"selection-background-color: rgb(0, 0, 0);\n"
"border : 1px solid black")
        self.Double2.setObjectName("Double2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(400, 860, 71, 71))
        self.label_5.setStyleSheet("font: 75 36pt \"Kokila\";")
        self.label_5.setObjectName("label_5")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(140, 230, 651, 81))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.horizontalLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.y2015 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_3)
        self.y2015.setStyleSheet("font: 24pt \"Kokila\";")
        self.y2015.setObjectName("y2015")
        self.gridLayout_3.addWidget(self.y2015, 0, 0, 1, 1)
        self.y2016 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_3)
        self.y2016.setStyleSheet("font: 24pt \"Kokila\";")
        self.y2016.setObjectName("y2016")
        self.gridLayout_3.addWidget(self.y2016, 0, 1, 1, 1)
        self.y2017 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_3)
        self.y2017.setStyleSheet("font: 24pt \"Kokila\";")
        self.y2017.setObjectName("y2017")
        self.gridLayout_3.addWidget(self.y2017, 0, 2, 1, 1)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(310, 550, 241, 41))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Load1 = QtWidgets.QPushButton(self.widget)
        self.Load1.setStyleSheet("font: 20pt \"Kokila\";\n"
"background-color: rgb(50, 197, 17);\n"
"border-radius : 30px")
        self.Load1.setObjectName("Load1")
        self.horizontalLayout.addWidget(self.Load1)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.Plot1 = QtWidgets.QPushButton(self.widget)
        self.Plot1.setStyleSheet("font: 20pt \"Kokila\";\n"
"background-color: rgb(50, 197, 17);\n"
"border-radius : 30px")
        self.Plot1.setObjectName("Plot1")
        self.horizontalLayout.addWidget(self.Plot1)
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(310, 950, 241, 41))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Load2 = QtWidgets.QPushButton(self.widget1)
        self.Load2.setStyleSheet("font: 20pt \"Kokila\";\n"
"background-color: rgb(50, 197, 17);\n"
"border-radius : 30px")
        self.Load2.setObjectName("Load2")
        self.horizontalLayout_2.addWidget(self.Load2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 18, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.Plot2 = QtWidgets.QPushButton(self.widget1)
        self.Plot2.setStyleSheet("font: 20pt \"Kokila\";\n"
"background-color: rgb(50, 197, 17);\n"
"border-radius : 30px")
        self.Plot2.setObjectName("Plot2")
        self.horizontalLayout_2.addWidget(self.Plot2)
        LineChart.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(LineChart)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1920, 26))
        self.menubar.setObjectName("menubar")
        LineChart.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(LineChart)
        self.statusbar.setObjectName("statusbar")
        LineChart.setStatusBar(self.statusbar)
####
        self.Load1.clicked.connect(self.Load1fn)
        self.Load2.clicked.connect(self.Load2fn)
        self.Plot1.clicked.connect(self.Plot1fn)
        self.Plot2.clicked.connect(self.Plot2fn)
####
        self.retranslateUi(LineChart)
        QtCore.QMetaObject.connectSlotsByName(LineChart)

    def retranslateUi(self, LineChart):
        _translate = QtCore.QCoreApplication.translate
        LineChart.setWindowTitle(_translate("LineChart", "Comparision of Countries"))
        self.label_2.setText(_translate("LineChart", "<html><head/><body><p align=\"center\">Country Level Analysis &amp; Comparision</p></body></html>"))
        self.label_3.setText(_translate("LineChart", "<html><head/><body><p align=\"center\"><span style=\" font-size:36pt; font-style:italic;\">Find Your Country Statistics</span></p></body></html>"))
        self.label_4.setText(_translate("LineChart", "<html><head/><body><p align=\"center\"><span style=\" font-size:36pt; font-style:italic;\">Compare 2 Countries</span></p></body></html>"))
        self.label_5.setText(_translate("LineChart", "<html><head/><body><p align=\"center\"><span style=\" font-style:italic;\">VS</span></p></body></html>"))
        self.y2015.setText(_translate("LineChart", "2015"))
        self.y2016.setText(_translate("LineChart", "2016"))
        self.y2017.setText(_translate("LineChart", "2017"))
        self.Load1.setText(_translate("LineChart", "Load"))
        self.Plot1.setText(_translate("LineChart", "Plot"))
        self.Load2.setText(_translate("LineChart", "Load"))
        self.Plot2.setText(_translate("LineChart", "Plot"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LineChart = QtWidgets.QMainWindow()
    ui = Ui_LineChart()
    ui.setupUi(LineChart)
    LineChart.show()
    sys.exit(app.exec_())

