# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ML.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

import numpy as np
import pymsgbox
from PyQt5 import QtCore, QtGui, QtWidgets
import UI.DataFrames as d


class Ui_Predictor(object):
    def rank_finder(self,which,predi):
        # Rank finder
        a = np.array(which['HS'])
        r = -1
        for count, i in enumerate(a, start=1):
            if i < predi:
                r = count
                break

        if r == -1:
            return(a.size + 1)
        else:
            return(r)

    def Predict_fn(self):
        parameters = [self.EC_SB.value(), self.FA_SB.value(), self.HA_SB.value(),
                      self.FR_SB.value(), self.TR_SB.value(), self.GN_SB.value()]
        parameters = d.pd.DataFrame(parameters)
        parameters = parameters.T

        #### MACHINE LEARNING ####

        import numpy as np
        import pandas as pd
        import matplotlib.pyplot as plt
        import seaborn as sns
        from sklearn.model_selection import train_test_split
        from sklearn.linear_model import LinearRegression
        from sklearn.metrics import r2_score

        # reading the dataset into DataFrame
        data = pd.read_csv(r'D:\Projects\SDL_WHR\MLDataset.csv')
        data = pd.DataFrame(data)

        # data preprocessing and cleaning
        data.isnull().any()
        data = data.fillna(method='ffill')

        # Correlation Heatmap for checking the Strong Predictors

        # fig ,axs = plt.subplots(figsize=(10,7))
        # axs = sns.heatmap(data.corr(),cmap = "YlGnBu",linewidths = .9,annot = True)

        # setting the predictor DataFrame as X
        # setting the response DataFrame as Y
        X = data.iloc[:, 1:]
        Y = data.iloc[:, 0:1]

        # splitting the X and Y in corresponding
        # Train and Test dataFrames

        X_train, X_test, Y_train, Y_test = train_test_split(X, Y,
                                                            test_size=0.25, random_state=0)

        # Training the model

        regressor = LinearRegression()
        regressor.fit(X_train, Y_train)

        # predicting on the basis of X_test value
        Y_pred = regressor.predict(X_test)
        mypred = regressor.predict(parameters)
        self.Result.setText('\tPrediction : %f' % mypred)

        r1 = self.rank_finder(d.var_2015,mypred)
        r2 = self.rank_finder(d.var_2016,mypred)
        r3 = self.rank_finder(d.var_2017,mypred)

        self.Rank1.setText('2015\t: %dth Rank'%r1)
        self.Rank2.setText('2016\t: %dth Rank'%r2)
        self.Rank3.setText('2017\t: %dth Rank'%r3)

        # pymsgbox.alert('Prediction : %f' % mypred)

        co = regressor.coef_
        incp = regressor.intercept_[0]
        acc = r2_score(Y_test, Y_pred)

        pymsgbox.alert("\n"
                       "MULTIPLE LINEAR REGRESSION MODEL\n"
                       "---------------------------------------------------------------------\n"
                       "\t*Coefficients*\n"
                       "-------------------------------------------------------------------\n"
                       " Economy\t\t: %f\n"
                       " Family\t\t: %f\n"
                       " Health\t\t: %f\n"
                       " Freedom\t\t: %f\n"
                       " Trust\t\t: %f\n"
                       " Generosity\t: %f\n"
                       "-------------------------------------------------------------------\n\n"
                       "\t*Intercept*\n"
                       "-------------------------------------------------------------------\n"
                       " C\t\t: %f\n"
                       "-------------------------------------------------------------------\n\n"
                       "\t*Accuracy*\n"
                       "-------------------------------------------------------------------\n"
                       " Value\t\t: %f\n"
                       "-------------------------------------------------------------------\n\n"
                       % (co[0][0],co[0][1],co[0][2],co[0][3],co[0][4],co[0][5],incp,acc),'Model Analysis')


    def setupUi(self, Predictor):
        Predictor.setObjectName("Predictor")
        Predictor.resize(1920, 1080)
        Predictor.setMinimumSize(QtCore.QSize(1920, 1080))
        Predictor.setMaximumSize(QtCore.QSize(1920, 1080))
        Predictor.showMaximized()
        Predictor.setStyleSheet("background-color: rgb(223, 223, 223);")
        self.centralwidget = QtWidgets.QWidget(Predictor)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(570, 390, 801, 421))
        self.widget.setStyleSheet("background-color: rgb(211, 211, 211);")
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label_10 = QtWidgets.QLabel(self.widget)
        self.label_10.setStyleSheet("font: 16pt \"Kokila\";")
        self.label_10.setObjectName("label_10")
        self.verticalLayout_13.addWidget(self.label_10)
        self.HA_SB = QtWidgets.QDoubleSpinBox(self.widget)
        self.HA_SB.setMinimumSize(QtCore.QSize(60, 50))
        self.HA_SB.setMaximumSize(QtCore.QSize(60, 50))
        self.HA_SB.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.HA_SB.setDecimals(3)
        self.HA_SB.setMaximum(1.0)
        self.HA_SB.setSingleStep(0.001)
        self.HA_SB.setObjectName("HA_SB")
        self.verticalLayout_13.addWidget(self.HA_SB)
        self.HE_SL = QtWidgets.QSlider(self.widget)
        self.HE_SL.setMinimumSize(QtCore.QSize(35, 300))
        self.HE_SL.setMaximum(1)
        self.HE_SL.setOrientation(QtCore.Qt.Vertical)
        self.HE_SL.setObjectName("HE_SL")
        self.verticalLayout_13.addWidget(self.HE_SL)
        self.gridLayout_2.addLayout(self.verticalLayout_13, 0, 4, 1, 1)
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_13 = QtWidgets.QLabel(self.widget)
        self.label_13.setStyleSheet("font: 16pt \"Kokila\";")
        self.label_13.setObjectName("label_13")
        self.verticalLayout_12.addWidget(self.label_13)
        self.FA_SB = QtWidgets.QDoubleSpinBox(self.widget)
        self.FA_SB.setMinimumSize(QtCore.QSize(50, 50))
        self.FA_SB.setMaximumSize(QtCore.QSize(60, 50))
        self.FA_SB.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.FA_SB.setDecimals(3)
        self.FA_SB.setMaximum(2.0)
        self.FA_SB.setSingleStep(0.001)
        self.FA_SB.setObjectName("FA_SB")
        self.verticalLayout_12.addWidget(self.FA_SB)
        self.FA_SL = QtWidgets.QSlider(self.widget)
        self.FA_SL.setMinimumSize(QtCore.QSize(35, 300))
        self.FA_SL.setMaximum(2)
        self.FA_SL.setSingleStep(1)
        self.FA_SL.setOrientation(QtCore.Qt.Vertical)
        self.FA_SL.setObjectName("FA_SL")
        self.verticalLayout_12.addWidget(self.FA_SL)
        self.gridLayout_2.addLayout(self.verticalLayout_12, 0, 2, 1, 1)
        self.verticalLayout_14 = QtWidgets.QVBoxLayout()
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.label_9 = QtWidgets.QLabel(self.widget)
        self.label_9.setStyleSheet("font: 16pt \"Kokila\";")
        self.label_9.setObjectName("label_9")
        self.verticalLayout_14.addWidget(self.label_9)
        self.FR_SB = QtWidgets.QDoubleSpinBox(self.widget)
        self.FR_SB.setMinimumSize(QtCore.QSize(60, 50))
        self.FR_SB.setMaximumSize(QtCore.QSize(60, 50))
        self.FR_SB.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.FR_SB.setDecimals(3)
        self.FR_SB.setMaximum(1.0)
        self.FR_SB.setSingleStep(0.001)
        self.FR_SB.setObjectName("FR_SB")
        self.verticalLayout_14.addWidget(self.FR_SB)
        self.FR_SL = QtWidgets.QSlider(self.widget)
        self.FR_SL.setMinimumSize(QtCore.QSize(35, 300))
        self.FR_SL.setMaximum(1)
        self.FR_SL.setOrientation(QtCore.Qt.Vertical)
        self.FR_SL.setObjectName("FR_SL")
        self.verticalLayout_14.addWidget(self.FR_SL)
        self.gridLayout_2.addLayout(self.verticalLayout_14, 0, 6, 1, 1)
        self.verticalLayout_15 = QtWidgets.QVBoxLayout()
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.label_12 = QtWidgets.QLabel(self.widget)
        self.label_12.setStyleSheet("font: 16pt \"Kokila\";")
        self.label_12.setObjectName("label_12")
        self.verticalLayout_15.addWidget(self.label_12)
        self.TR_SB = QtWidgets.QDoubleSpinBox(self.widget)
        self.TR_SB.setMinimumSize(QtCore.QSize(60, 50))
        self.TR_SB.setMaximumSize(QtCore.QSize(60, 50))
        self.TR_SB.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.TR_SB.setDecimals(3)
        self.TR_SB.setMaximum(1.0)
        self.TR_SB.setSingleStep(0.001)
        self.TR_SB.setObjectName("TR_SB")
        self.verticalLayout_15.addWidget(self.TR_SB)
        self.TR_SL = QtWidgets.QSlider(self.widget)
        self.TR_SL.setMinimumSize(QtCore.QSize(35, 300))
        self.TR_SL.setMaximum(1)
        self.TR_SL.setOrientation(QtCore.Qt.Vertical)
        self.TR_SL.setObjectName("TR_SL")
        self.verticalLayout_15.addWidget(self.TR_SL)
        self.gridLayout_2.addLayout(self.verticalLayout_15, 0, 8, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.widget)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_2.addWidget(self.line_2, 0, 3, 1, 1)
        self.verticalLayout_16 = QtWidgets.QVBoxLayout()
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.label_11 = QtWidgets.QLabel(self.widget)
        self.label_11.setStyleSheet("font: 16pt \"Kokila\";")
        self.label_11.setObjectName("label_11")
        self.verticalLayout_16.addWidget(self.label_11)
        self.GN_SB = QtWidgets.QDoubleSpinBox(self.widget)
        self.GN_SB.setMinimumSize(QtCore.QSize(60, 50))
        self.GN_SB.setMaximumSize(QtCore.QSize(60, 50))
        self.GN_SB.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.GN_SB.setDecimals(3)
        self.GN_SB.setMaximum(1.0)
        self.GN_SB.setSingleStep(0.001)
        self.GN_SB.setObjectName("GN_SB")
        self.verticalLayout_16.addWidget(self.GN_SB)
        self.GN_SL = QtWidgets.QSlider(self.widget)
        self.GN_SL.setMinimumSize(QtCore.QSize(35, 300))
        self.GN_SL.setMaximum(1)
        self.GN_SL.setOrientation(QtCore.Qt.Vertical)
        self.GN_SL.setObjectName("GN_SL")
        self.verticalLayout_16.addWidget(self.GN_SL)
        self.gridLayout_2.addLayout(self.verticalLayout_16, 0, 10, 1, 1)
        self.line_3 = QtWidgets.QFrame(self.widget)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout_2.addWidget(self.line_3, 0, 5, 1, 1)
        self.line = QtWidgets.QFrame(self.widget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_2.addWidget(self.line, 0, 1, 1, 1)
        self.line_4 = QtWidgets.QFrame(self.widget)
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.gridLayout_2.addWidget(self.line_4, 0, 7, 1, 1)
        self.line_5 = QtWidgets.QFrame(self.widget)
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.gridLayout_2.addWidget(self.line_5, 0, 9, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setStyleSheet("font: 16pt \"Kokila\";")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.EC_SB = QtWidgets.QDoubleSpinBox(self.widget)
        self.EC_SB.setMinimumSize(QtCore.QSize(60, 50))
        self.EC_SB.setMaximumSize(QtCore.QSize(60, 50))
        self.EC_SB.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.EC_SB.setDecimals(3)
        self.EC_SB.setMaximum(2.0)
        self.EC_SB.setSingleStep(0.001)
        self.EC_SB.setObjectName("EC_SB")
        self.verticalLayout.addWidget(self.EC_SB)
        self.EC_SL = QtWidgets.QSlider(self.widget)
        self.EC_SL.setMinimumSize(QtCore.QSize(35, 300))
        self.EC_SL.setStyleSheet("")
        self.EC_SL.setMaximum(2)
        self.EC_SL.setOrientation(QtCore.Qt.Vertical)
        self.EC_SL.setObjectName("EC_SL")
        self.verticalLayout.addWidget(self.EC_SL)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.GO = QtWidgets.QPushButton(self.centralwidget)
        self.GO.setGeometry(QtCore.QRect(840, 860, 251, 91))
        self.GO.setStyleSheet("background-color: rgb(0, 176, 240);\n"
"font: 75 22pt \"Kokila\";\n"
"border :1px solid black;\n"
"border-radius : 30px;\n"
"\n"
"")
        self.GO.setObjectName("GO")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(481, 41, 982, 142))
        self.label_3.setStyleSheet("font: 72pt \"Kokila\";\n"
"background-color: rgb(0, 176, 240);\n"
"")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 40, 191, 941))
        self.label_4.setStyleSheet("background-color: rgb(0, 176, 240);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(1705, 39, 191, 941))
        self.label_5.setStyleSheet("background-color: rgb(0, 176, 240);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 980, 1876, 31))
        self.label_6.setStyleSheet("background-color: rgb(0, 176, 240);")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.line_7 = QtWidgets.QFrame(self.centralwidget)
        self.line_7.setGeometry(QtCore.QRect(230, 39, 20, 941))
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.line_8 = QtWidgets.QFrame(self.centralwidget)
        self.line_8.setGeometry(QtCore.QRect(1660, 39, 20, 941))
        self.line_8.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.Result = QtWidgets.QLabel(self.centralwidget)
        self.Result.setEnabled(True)
        self.Result.setGeometry(QtCore.QRect(480, 180, 704, 142))
        self.Result.setStyleSheet("background-color: rgb(158, 158, 158);\n"
"font: 75 italic 36pt \"Kokila\";")
        self.Result.setText("")
        self.Result.setObjectName("Result")
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(1160, 182, 20, 141))
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(1183, 176, 281, 151))
        self.widget1.setObjectName("widget1")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.Rank1 = QtWidgets.QLabel(self.widget1)
        self.Rank1.setEnabled(True)
        self.Rank1.setMinimumSize(QtCore.QSize(279, 39))
        self.Rank1.setMaximumSize(QtCore.QSize(279, 39))
        self.Rank1.setStyleSheet("background-color: rgb(158, 158, 158);\n"
"font: italic 24pt \"Kokila\";")
        self.Rank1.setText("")
        self.Rank1.setObjectName("Rank1")
        self.verticalLayout_3.addWidget(self.Rank1)
        self.Rank2 = QtWidgets.QLabel(self.widget1)
        self.Rank2.setEnabled(True)
        self.Rank2.setMinimumSize(QtCore.QSize(279, 39))
        self.Rank2.setMaximumSize(QtCore.QSize(279, 39))
        self.Rank2.setStyleSheet("background-color: rgb(158, 158, 158);\n"
"font: italic 24pt \"Kokila\";")
        self.Rank2.setText("")
        self.Rank2.setObjectName("Rank2")
        self.verticalLayout_3.addWidget(self.Rank2)
        self.Rank3 = QtWidgets.QLabel(self.widget1)
        self.Rank3.setEnabled(True)
        self.Rank3.setMinimumSize(QtCore.QSize(279, 39))
        self.Rank3.setMaximumSize(QtCore.QSize(279, 39))
        self.Rank3.setStyleSheet("background-color: rgb(158, 158, 158);\n"
"font: italic 24pt \"Kokila\";")
        self.Rank3.setText("")
        self.Rank3.setObjectName("Rank3")
        self.verticalLayout_3.addWidget(self.Rank3)
        self.Rank1.raise_()
        self.Rank2.raise_()
        self.Rank3.raise_()
        self.Result.raise_()
        self.widget.raise_()
        self.GO.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.line_7.raise_()
        self.line_8.raise_()
        self.Rank1.raise_()
        self.line_6.raise_()
        Predictor.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Predictor)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1920, 26))
        self.menubar.setObjectName("menubar")
        Predictor.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Predictor)
        self.statusbar.setObjectName("statusbar")
        Predictor.setStatusBar(self.statusbar)

        self.retranslateUi(Predictor)
        QtCore.QMetaObject.connectSlotsByName(Predictor)
        Predictor.setTabOrder(self.EC_SL, self.EC_SB)
        Predictor.setTabOrder(self.EC_SB, self.FA_SL)
        Predictor.setTabOrder(self.FA_SL, self.FA_SB)
        Predictor.setTabOrder(self.FA_SB, self.HE_SL)
        Predictor.setTabOrder(self.HE_SL, self.HA_SB)
        Predictor.setTabOrder(self.HA_SB, self.FR_SL)
        Predictor.setTabOrder(self.FR_SL, self.FR_SB)
        Predictor.setTabOrder(self.FR_SB, self.TR_SL)
        Predictor.setTabOrder(self.TR_SL, self.TR_SB)
        Predictor.setTabOrder(self.TR_SB, self.GN_SL)
        Predictor.setTabOrder(self.GN_SL, self.GN_SB)
####
        self.EC_SL.valueChanged['int'].connect(self.EC_SB.setValue)
        self.FA_SL.valueChanged['int'].connect(self.FA_SB.setValue)
        self.HE_SL.valueChanged['int'].connect(self.HA_SB.setValue)
        self.FR_SL.valueChanged['int'].connect(self.FR_SB.setValue)
        self.TR_SL.valueChanged['int'].connect(self.TR_SB.setValue)
        self.GN_SL.valueChanged['int'].connect(self.GN_SB.setValue)

        self.GO.clicked.connect(self.Predict_fn)

####
    def retranslateUi(self, Predictor):
        _translate = QtCore.QCoreApplication.translate
        Predictor.setWindowTitle(_translate("Predictor", "Machine Learning"))
        self.label_10.setText(_translate("Predictor", "<html><head/><body><p align=\"center\">Health</p></body></html>"))
        self.label_13.setText(_translate("Predictor", "<html><head/><body><p align=\"center\">Family</p></body></html>"))
        self.label_9.setText(_translate("Predictor", "Freedom"))
        self.label_12.setText(_translate("Predictor", "<html><head/><body><p align=\"center\">Trust</p></body></html>"))
        self.label_11.setText(_translate("Predictor", "Generosity"))
        self.label.setText(_translate("Predictor", "Economy"))
        self.GO.setText(_translate("Predictor", "GO!"))
        self.label_3.setText(_translate("Predictor", "<html><head/><body><p align=\"center\">Happiness Score Predictor</p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Predictor = QtWidgets.QMainWindow()
    ui = Ui_Predictor()
    ui.setupUi(Predictor)
    Predictor.show()
    sys.exit(app.exec_())

