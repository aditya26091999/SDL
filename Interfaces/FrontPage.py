# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\FrontPage.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from Interfaces.DashBoard import Ui_DashBoard


class Ui_FrontPg(object):
    def jump_DashBoard(self):
        self.DashBoard = QtWidgets.QDialog()
        self.ui = Ui_DashBoard()
        self.ui.setupUi(self.DashBoard)
        self.DashBoard.show()

    def setupUi(self, FrontPg):
        FrontPg.setObjectName("FrontPg")
        FrontPg.resize(1094, 730)
        FrontPg.setStyleSheet("")
        self.FrontPage = QtWidgets.QLabel(FrontPg)
        self.FrontPage.setGeometry(QtCore.QRect(-210, 0, 1420, 946))
        self.FrontPage.setText("")
        self.FrontPage.setPixmap(QtGui.QPixmap("../Images/wp2411972.jpg"))
        self.FrontPage.setObjectName("FrontPage")
        self.label = QtWidgets.QLabel(FrontPg)
        self.label.setGeometry(QtCore.QRect(-70, 70, 851, 131))
        self.label.setObjectName("label")
        self.Explore = QtWidgets.QPushButton(FrontPg)
        self.Explore.setGeometry(QtCore.QRect(220, 520, 299, 80))
        self.Explore.setStyleSheet("background-color: rgb(136, 191, 232);\n"
"font: 36pt \"Kokila\";")
        self.Explore.setObjectName("Explore")
        self.label_2 = QtWidgets.QLabel(FrontPg)
        self.label_2.setGeometry(QtCore.QRect(90, 300, 511, 111))
        self.label_2.setObjectName("label_2")

###
        self.Explore.clicked.connect(self.jump_DashBoard)
###
        self.retranslateUi(FrontPg)
        QtCore.QMetaObject.connectSlotsByName(FrontPg)

    def retranslateUi(self, FrontPg):
        _translate = QtCore.QCoreApplication.translate
        FrontPg.setWindowTitle(_translate("FrontPg", "FrontPage"))
        self.label.setText(_translate("FrontPg", "<html><head/><body><p align=\"center\"><span style=\" font-size:36pt; font-weight:600;\">How Happy are YOU?</span></p></body></html>"))
        self.Explore.setToolTip(_translate("FrontPg", "<html><head/><body><p>Check worldwide trends</p></body></html>"))
        self.Explore.setText(_translate("FrontPg", "Explore!"))
        self.label_2.setText(_translate("FrontPg", "<html><head/><body><p><span style=\" font-size:16pt;\">&quot; If you want to be happy, BE &quot;</span></p><p align=\"right\"><span style=\" font-size:16pt;\">- Leo Tolstoy</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FrontPg = QtWidgets.QDialog()
    ui = Ui_FrontPg()
    ui.setupUi(FrontPg)
    FrontPg.show()
    sys.exit(app.exec_())

