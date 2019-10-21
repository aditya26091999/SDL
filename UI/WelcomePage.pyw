# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WelcomePage.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from UI.DatasetExplore import Ui_DatasetExplore


class Ui_WelcomePage(object):
    def jump_DatasetExplore(self):
        self.DatasetExplore = QtWidgets.QMainWindow()
        self.ui = Ui_DatasetExplore()
        self.ui.setupUi(self.DatasetExplore)
        self.DatasetExplore.show()
        WelcomePage.hide()

    def setupUi(self, WelcomePage):
        WelcomePage.setObjectName("WelcomePage")
        WelcomePage.resize(1920, 1080)
        WelcomePage.setMinimumSize(QtCore.QSize(1920, 1080))
        WelcomePage.setMaximumSize(QtCore.QSize(1920, 1080))
        WelcomePage.showMaximized()
        self.centralwidget = QtWidgets.QWidget(WelcomePage)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1920, 1080))
        self.label.setMinimumSize(QtCore.QSize(1920, 1080))
        self.label.setMaximumSize(QtCore.QSize(1920, 1080))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../Images/rsz_1boy.jpg"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 450, 1141, 151))
        self.label_2.setStyleSheet("font: 90pt \"Kokila\";")
        self.label_2.setObjectName("label_2")
        self.Explore = QtWidgets.QPushButton(self.centralwidget)
        self.Explore.setGeometry(QtCore.QRect(290, 710, 421, 111))
        self.Explore.setToolTipDuration(-2)
        self.Explore.setStyleSheet("background-color: rgb(175, 141, 174);\n"
"font: 75 36pt \"Kokila\";")
        self.Explore.setObjectName("Explore")
        WelcomePage.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(WelcomePage)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1920, 26))
        self.menubar.setObjectName("menubar")
        WelcomePage.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(WelcomePage)
        self.statusbar.setObjectName("statusbar")
        WelcomePage.setStatusBar(self.statusbar)


###
        self.Explore.clicked.connect(self.jump_DatasetExplore)

###

        self.retranslateUi(WelcomePage)
        QtCore.QMetaObject.connectSlotsByName(WelcomePage)

    def retranslateUi(self, WelcomePage):
        _translate = QtCore.QCoreApplication.translate
        WelcomePage.setWindowTitle(_translate("WelcomePage", "WelcomePage"))
        self.label_2.setText(_translate("WelcomePage", "How Happy are YOU?"))
        self.Explore.setToolTip(_translate("WelcomePage", "Dive into the details"))
        self.Explore.setText(_translate("WelcomePage", "EXPLORE!"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    WelcomePage = QtWidgets.QMainWindow()
    ui = Ui_WelcomePage()
    ui.setupUi(WelcomePage)
    WelcomePage.show()
    sys.exit(app.exec_())

