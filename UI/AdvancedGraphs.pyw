# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AdvancedGraphs.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
import pymsgbox
from PyQt5 import QtCore, QtGui, QtWidgets
import UI.DataFrames as d

import plotly
import plotly.graph_objs as go
import plotly.express as px

from UI.ML import Ui_Predictor


class Ui_AdvancedGraphs(object):
    def show_Mean(self):
        fig, axs = d.plt.subplots(1,1)
        fig.canvas.set_window_title('Mean Happiness over Years')
        x = ['2015', '2016', '2017']
        y1 = d.desc_2015['HS']['mean']
        y2 = d.desc_2016['HS']['mean']
        y3 = d.desc_2017['HS']['mean']
        y = [y1, y2, y3]
        d.plt.plot(x, y, linestyle='-', marker='o', color='g')
        d.plt.xlabel("Year")
        d.plt.ylabel("Mean Happiness Score")
        d.plt.title("Mean Happiness vs Year")
        d.plt.show()

    def show_MaxMin(self):
        fig, axs = d.plt.subplots(1,1)
        fig.canvas.set_window_title('Maximum and Minimum scores over years')
        x = ['2015', '2016', '2017']
        ymax1 = d.desc_2015['HS']['max']
        ymax2 = d.desc_2016['HS']['max']
        ymax3 = d.desc_2017['HS']['max']
        ymax = [ymax1, ymax2, ymax3]

        ymin1 = d.desc_2015['HS']['min']
        ymin2 = d.desc_2016['HS']['min']
        ymin3 = d.desc_2017['HS']['min']
        ymin = [ymin1, ymin2, ymin3]

        d.plt.plot(x, ymax, linestyle='-', marker='o', color='b', label='Maximum HS')
        d.plt.plot(x, ymin, linestyle='-', marker='o', color='r', label='Minimum HS')

        for i, j in zip(x, ymax):
            d.plt.annotate(str(j), xy=(i, j), xytext=(-15, -15), textcoords='offset points')

        for i, j in zip(x, ymin):
            d.plt.annotate(str(j), xy=(i, j), xytext=(2, 15), textcoords='offset points')

        d.plt.xlabel("Year")
        d.plt.ylabel("Happiness Score")
        d.plt.title('Max/Min Happiness Scores Yearwise')
        d.plt.legend()
        d.plt.show()

    def show_World(self):
        var_2015 = d.pd.read_csv(r'D:\Projects\SDL_WHR\2015.csv')
        var_2015 = d.pd.DataFrame(var_2015)
        var_2015 = var_2015.rename({'Country': 'C',
                                    'Region': 'R',
                                    'Happiness Rank': 'HR',
                                    'Happiness Score': 'HS',
                                    'Standard Error': 'SE',
                                    'Economy (GDP per Capita)': 'EC',
                                    'Family': 'FA',
                                    'Health (Life Expectancy)': 'HE',
                                    'Freedom': 'FR',
                                    'Trust (Government Corruption)': 'TR',
                                    'Generosity': 'GN',
                                    'Dystopia Residual': 'DR'},
                                   axis=1)

        data = dict(type='choropleth',
                    locations=var_2015['C'],
                    locationmode='country names',
                    z=var_2015['HS'],
                    text=var_2015['C'],
                    colorbar={'title': 'Happiness'})
        layout = dict(title='Happiness Index 2015',
                      geo=dict(showframe=False,
                               projection={'type': 'mercator'}))
        choromap3 = go.Figure(data=[data], layout=layout)
        plotly.offline.plot(choromap3,filename=r'..\Saved\WHR_2015.html')

        var_2016 = d.pd.read_csv(r'D:\Projects\SDL_WHR\2016.csv')
        var_2016 = d.pd.DataFrame(var_2016)
        var_2016 = var_2016.rename({'Country': 'C',
                                    'Region': 'R',
                                    'Happiness Rank': 'HR',
                                    'Happiness Score': 'HS',
                                    'Lower Confidence Interval': 'LCI',
                                    'Upper Confidence Interval': 'UCI',
                                    'Economy (GDP per Capita)': 'EC',
                                    'Family': 'FA',
                                    'Health (Life Expectancy)': 'HE',
                                    'Freedom': 'FR',
                                    'Trust (Government Corruption)': 'TR',
                                    'Generosity': 'GN',
                                    'Dystopia Residual': 'DR'},
                                   axis=1)

        data = dict(type='choropleth',
                    locations=var_2016['C'],
                    locationmode='country names',
                    z=var_2016['HS'],
                    text=var_2016['C'],
                    colorbar={'title': 'Happiness'})
        layout = dict(title='Happiness Index 2016',
                      geo=dict(showframe=False,
                               projection={'type': 'mercator'}))
        choromap3 = go.Figure(data=[data], layout=layout)
        plotly.offline.plot(choromap3,filename=r'..\Saved\WHR_2016.html')

        var_2017 = d.pd.read_csv(r'D:\Projects\SDL_WHR\2017.csv')
        var_2017 = d.pd.DataFrame(var_2017)
        var_2017 = var_2017.rename({'Country': 'C',
                                    'Happiness.Rank': 'HR',
                                    'Happiness.Score': 'HS',
                                    'Whisker.high': 'WH',
                                    'Whisker.low': 'WL',
                                    'Economy..GDP.per.Capita.': 'EC',
                                    'Family': 'FA',
                                    'Health..Life.Expectancy.': 'HE',
                                    'Freedom': 'FR',
                                    'Trust..Government.Corruption.': 'TR',
                                    'Generosity': 'GN',
                                    'Dystopia.Residual': 'DR'},
                                   axis=1)

        data = dict(type='choropleth',
                    locations=var_2017['C'],
                    locationmode='country names',
                    z=var_2017['HS'],
                    text=var_2017['C'],
                    colorbar={'title': 'Happiness'})
        layout = dict(title='Happiness Index 2017',
                      geo=dict(showframe=False,
                               projection={'type': 'mercator'}))
        choromap3 = go.Figure(data=[data], layout=layout)
        plotly.offline.plot(choromap3,filename=r'..\Saved\WHR_2017.html')



    def show_ThreeD(self):
        features = ['EC','FA','HE','FR','TR','GN']
        x = self.Triple1.currentIndex()
        y = self.Triple2.currentIndex()
        z = self.Triple3.currentIndex()

        x = features[x]
        y = features[y]
        z = features[z]

        fig = px.scatter_3d(d.var_2015, x=x, y=y, z=z, color='HS', opacity=0.9)
        plotly.offline.plot(fig, filename=r'..\Saved\2015_3D.html')
        fig = px.scatter_3d(d.var_2016, x=x, y=y, z=z, color='HS', opacity=0.9)
        plotly.offline.plot(fig, filename=r'..\Saved\2016_3D.html')
        fig = px.scatter_3d(d.var_2017, x=x, y=y, z=z, color='HS', opacity=0.9)
        plotly.offline.plot(fig, filename=r'..\Saved\2017_3D.html')

    def jump_Predict(self):
        self.Predictor = QtWidgets.QMainWindow()
        self.ui = Ui_Predictor()
        self.ui.setupUi(self.Predictor)
        self.Predictor.show()


    def setupUi(self, AdvancedGraphs):
        AdvancedGraphs.setObjectName("AdvancedGraphs")
        AdvancedGraphs.resize(1920, 1080)
        AdvancedGraphs.setMinimumSize(QtCore.QSize(1920, 1080))
        AdvancedGraphs.setMaximumSize(QtCore.QSize(1920, 1080))
        AdvancedGraphs.showMaximized()
        AdvancedGraphs.setStyleSheet("background-color: rgb(255, 255, 255);")
        AdvancedGraphs.showMaximized()

        self.centralwidget = QtWidgets.QWidget(AdvancedGraphs)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(1350, 640, 551, 391))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../Images/analytics-1925495_1920.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 720, 311, 281))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../Images/3d.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(590, 20, 741, 141))
        self.label_3.setStyleSheet("font: 72pt \"Kokila\";\n"
"background-color: rgb(0, 176, 240);\n"
"")
        self.label_3.setObjectName("label_3")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(172, 196, 691, 93))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_4.setMaximumSize(QtCore.QSize(495, 91))
        self.label_4.setStyleSheet("font: 24pt \"Kokila\";")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_5.setMaximumSize(QtCore.QSize(91, 91))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("../Images/growth.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.label_7 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_7.setMinimumSize(QtCore.QSize(91, 91))
        self.label_7.setMaximumSize(QtCore.QSize(91, 91))
        self.label_7.setStyleSheet("font: 24pt \"Kokila\";")
        self.label_7.setObjectName("label_7")
        self.horizontalLayout.addWidget(self.label_7)
        self.label_6 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_6.setMaximumSize(QtCore.QSize(91, 91))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("../Images/decreasing.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.label_6)
        self.label_9 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_9.setMinimumSize(QtCore.QSize(91, 91))
        self.label_9.setMaximumSize(QtCore.QSize(91, 91))
        self.label_9.setStyleSheet("font: 24pt \"Kokila\";")
        self.label_9.setObjectName("label_9")
        self.horizontalLayout.addWidget(self.label_9)
        self.Mean = QtWidgets.QPushButton(self.centralwidget)
        self.Mean.setGeometry(QtCore.QRect(410, 310, 171, 71))
        self.Mean.setStyleSheet("background-color: rgb(0, 176, 240);\n"
"font: 75 22pt \"Kokila\";\n"
"border-radius : 30px\n"
"")
        self.Mean.setObjectName("Mean")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(103, 410, 791, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.MaxMin = QtWidgets.QPushButton(self.centralwidget)
        self.MaxMin.setGeometry(QtCore.QRect(408, 540, 171, 71))
        self.MaxMin.setStyleSheet("background-color: rgb(0, 176, 240);\n"
"font: 75 22pt \"Kokila\";\n"
"border-radius : 30px\n"
"")
        self.MaxMin.setObjectName("MaxMin")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(103, 640, 791, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.ThreeD = QtWidgets.QPushButton(self.centralwidget)
        self.ThreeD.setGeometry(QtCore.QRect(860, 933, 171, 71))
        self.ThreeD.setStyleSheet("background-color: rgb(0, 176, 240);\n"
"font: 75 22pt \"Kokila\";\n"
"border-radius : 30px\n"
"")
        self.ThreeD.setObjectName("ThreeD")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(216, 440, 590, 93))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_12 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_12.setMinimumSize(QtCore.QSize(91, 91))
        self.label_12.setMaximumSize(QtCore.QSize(91, 91))
        self.label_12.setText("")
        self.label_12.setPixmap(QtGui.QPixmap("../Images/rank.png"))
        self.label_12.setScaledContents(True)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_2.addWidget(self.label_12)
        self.label_8 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_8.setStyleSheet("font: 36pt \"Kokila\";")
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_2.addWidget(self.label_8)
        self.label_11 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_11.setMaximumSize(QtCore.QSize(91, 91))
        self.label_11.setText("")
        self.label_11.setPixmap(QtGui.QPixmap("../Images/iconfinder_trophy_1054950.png"))
        self.label_11.setScaledContents(True)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_2.addWidget(self.label_11)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(800, 700, 311, 95))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_10 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_10.setStyleSheet("font: 36pt \"Kokila\";")
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_3.addWidget(self.label_10)
        self.label_13 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_13.setMinimumSize(QtCore.QSize(91, 91))
        self.label_13.setMaximumSize(QtCore.QSize(91, 91))
        self.label_13.setText("")
        self.label_13.setPixmap(QtGui.QPixmap("../Images/3d (1).png"))
        self.label_13.setScaledContents(True)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_3.addWidget(self.label_13)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(1130, 196, 484, 95))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_18 = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.label_18.setStyleSheet("font: 36pt \"Kokila\";")
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_7.addWidget(self.label_18)
        self.label_19 = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.label_19.setMinimumSize(QtCore.QSize(91, 91))
        self.label_19.setMaximumSize(QtCore.QSize(91, 91))
        self.label_19.setText("")
        self.label_19.setPixmap(QtGui.QPixmap("../Images/worldwide.png"))
        self.label_19.setScaledContents(True)
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_7.addWidget(self.label_19)
        self.World = QtWidgets.QPushButton(self.centralwidget)
        self.World.setGeometry(QtCore.QRect(1290, 310, 171, 71))
        self.World.setStyleSheet("background-color: rgb(0, 176, 240);\n"
"font: 75 22pt \"Kokila\";\n"
"border-radius : 30px\n"
"")
        self.World.setObjectName("World")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(1020, 410, 781, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(1090, 440, 621, 93))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_20 = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        self.label_20.setStyleSheet("font: 36pt \"Kokila\";")
        self.label_20.setObjectName("label_20")
        self.horizontalLayout_8.addWidget(self.label_20)
        self.label_21 = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        self.label_21.setMinimumSize(QtCore.QSize(91, 91))
        self.label_21.setMaximumSize(QtCore.QSize(91, 91))
        self.label_21.setText("")
        self.label_21.setPixmap(QtGui.QPixmap("../Images/dice.png"))
        self.label_21.setScaledContents(True)
        self.label_21.setObjectName("label_21")
        self.horizontalLayout_8.addWidget(self.label_21)
        self.Predict = QtWidgets.QPushButton(self.centralwidget)
        self.Predict.setGeometry(QtCore.QRect(1280, 540, 171, 71))
        self.Predict.setStyleSheet("background-color: rgb(0, 176, 240);\n"
"font: 75 22pt \"Kokila\";\n"
"border-radius : 30px\n"
"")
        self.Predict.setObjectName("Predict")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(1020, 640, 781, 20))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(631, 834, 641, 61))
        self.widget.setObjectName("widget")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.Triple1 = QtWidgets.QComboBox(self.widget)
        self.Triple1.setStyleSheet("background-color: rgb(170, 0, 0,70%);\n"
"font: 16pt \"Kokila\";\n"
"color: rgb(255,255,255);\n"
"selection-background-color: rgb(0, 0, 0);\n"
"border : 1px solid black")
        self.Triple1.setObjectName("Triple1")
        self.Triple1.addItem("")
        self.Triple1.addItem("")
        self.Triple1.addItem("")
        self.Triple1.addItem("")
        self.Triple1.addItem("")
        self.Triple1.addItem("")
        self.horizontalLayout_6.addWidget(self.Triple1)
        self.Triple2 = QtWidgets.QComboBox(self.widget)
        self.Triple2.setStyleSheet("background-color: rgb(255, 145, 0);\n"
"font: 16pt \"Kokila\";\n"
"color: rgb(255,255,255);\n"
"selection-background-color: rgb(0, 0, 0);\n"
"border : 1px solid black")
        self.Triple2.setObjectName("Triple2")
        self.Triple2.addItem("")
        self.Triple2.addItem("")
        self.Triple2.addItem("")
        self.Triple2.addItem("")
        self.Triple2.addItem("")
        self.Triple2.addItem("")
        self.horizontalLayout_6.addWidget(self.Triple2)
        self.Triple3 = QtWidgets.QComboBox(self.widget)
        self.Triple3.setStyleSheet("background-color: rgb(170, 0, 0,70%);\n"
"font: 16pt \"Kokila\";\n"
"color: rgb(255,255,255);\n"
"selection-background-color: rgb(0, 0, 0);\n"
"border : 1px solid black")
        self.Triple3.setObjectName("Triple3")
        self.Triple3.addItem("")
        self.Triple3.addItem("")
        self.Triple3.addItem("")
        self.Triple3.addItem("")
        self.Triple3.addItem("")
        self.Triple3.addItem("")
        self.horizontalLayout_6.addWidget(self.Triple3)
        AdvancedGraphs.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AdvancedGraphs)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1920, 26))
        self.menubar.setObjectName("menubar")
        AdvancedGraphs.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AdvancedGraphs)
        self.statusbar.setObjectName("statusbar")
        AdvancedGraphs.setStatusBar(self.statusbar)
#####
        self.Mean.clicked.connect(self.show_Mean)
        self.MaxMin.clicked.connect(self.show_MaxMin)
        self.ThreeD.clicked.connect(self.show_ThreeD)
        self.Predict.clicked.connect(self.jump_Predict)
        self.World.clicked.connect(self.show_World)


#####
        self.retranslateUi(AdvancedGraphs)
        QtCore.QMetaObject.connectSlotsByName(AdvancedGraphs)

    def retranslateUi(self, AdvancedGraphs):
        _translate = QtCore.QCoreApplication.translate
        AdvancedGraphs.setWindowTitle(_translate("AdvancedGraphs", "Advanced Graphs"))
        self.label_3.setText(_translate("AdvancedGraphs", "<html><head/><body><p align=\"center\">Complex Analysis</p></body></html>"))
        self.label_4.setText(_translate("AdvancedGraphs", "<html><head/><body><p><span style=\" font-size:36pt;\">Did Happiness</span></p></body></html>"))
        self.label_7.setText(_translate("AdvancedGraphs", "<html><head/><body><p align=\"center\"><span style=\" font-size:36pt;\">Or</span></p></body></html>"))
        self.label_9.setText(_translate("AdvancedGraphs", "<html><head/><body><p align=\"center\"><span style=\" font-size:36pt;\">?</span></p></body></html>"))
        self.Mean.setText(_translate("AdvancedGraphs", "CHECK!"))
        self.MaxMin.setText(_translate("AdvancedGraphs", "CHECK!"))
        self.ThreeD.setText(_translate("AdvancedGraphs", "CHECK!"))
        self.label_8.setText(_translate("AdvancedGraphs", "Winners and Losers?"))
        self.label_10.setText(_translate("AdvancedGraphs", "<html><head/><body><p align=\"center\">3D Check!</p></body></html>"))
        self.label_18.setText(_translate("AdvancedGraphs", "<html><head/><body><p align=\"center\">The BIG PICTURE!</p></body></html>"))
        self.World.setText(_translate("AdvancedGraphs", "CHECK!"))
        self.label_20.setText(_translate("AdvancedGraphs", "<html><head/><body><p align=\"center\">PREDICT YOUR SCORE?</p></body></html>"))
        self.Predict.setText(_translate("AdvancedGraphs", "CHECK!"))
        self.Triple1.setItemText(0, _translate("AdvancedGraphs", "Economy"))
        self.Triple1.setItemText(1, _translate("AdvancedGraphs", "Family"))
        self.Triple1.setItemText(2, _translate("AdvancedGraphs", "Health"))
        self.Triple1.setItemText(3, _translate("AdvancedGraphs", "Freedom"))
        self.Triple1.setItemText(4, _translate("AdvancedGraphs", "Trust"))
        self.Triple1.setItemText(5, _translate("AdvancedGraphs", "Generosity"))
        self.Triple2.setItemText(0, _translate("AdvancedGraphs", "Economy"))
        self.Triple2.setItemText(1, _translate("AdvancedGraphs", "Family"))
        self.Triple2.setItemText(2, _translate("AdvancedGraphs", "Health"))
        self.Triple2.setItemText(3, _translate("AdvancedGraphs", "Freedom"))
        self.Triple2.setItemText(4, _translate("AdvancedGraphs", "Trust"))
        self.Triple2.setItemText(5, _translate("AdvancedGraphs", "Generosity"))
        self.Triple3.setItemText(0, _translate("AdvancedGraphs", "Economy"))
        self.Triple3.setItemText(1, _translate("AdvancedGraphs", "Family"))
        self.Triple3.setItemText(2, _translate("AdvancedGraphs", "Health"))
        self.Triple3.setItemText(3, _translate("AdvancedGraphs", "Freedom"))
        self.Triple3.setItemText(4, _translate("AdvancedGraphs", "Trust"))
        self.Triple3.setItemText(5, _translate("AdvancedGraphs", "Generosity"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AdvancedGraphs = QtWidgets.QMainWindow()
    ui = Ui_AdvancedGraphs()
    ui.setupUi(AdvancedGraphs)
    AdvancedGraphs.show()
    sys.exit(app.exec_())

