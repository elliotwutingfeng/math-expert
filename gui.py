# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pyuic5/main.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(569, 636)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 9, 1, 1, 1)
        self.titleTxt = QtWidgets.QPlainTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.titleTxt.setFont(font)
        self.titleTxt.setObjectName("titleTxt")
        self.gridLayout.addWidget(self.titleTxt, 4, 0, 1, 2)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 20, 0, 1, 1)
        self.diffBt = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.diffBt.setFont(font)
        self.diffBt.setStyleSheet("")
        self.diffBt.setObjectName("diffBt")
        self.gridLayout.addWidget(self.diffBt, 10, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setItalic(True)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 2)
        self.simpBt = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.simpBt.setFont(font)
        self.simpBt.setObjectName("simpBt")
        self.gridLayout.addWidget(self.simpBt, 10, 1, 1, 1)
        self.authorTxt = QtWidgets.QPlainTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.authorTxt.setFont(font)
        self.authorTxt.setObjectName("authorTxt")
        self.gridLayout.addWidget(self.authorTxt, 5, 0, 1, 2)
        self.expTxt = QtWidgets.QPlainTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.expTxt.setFont(font)
        self.expTxt.setObjectName("expTxt")
        self.gridLayout.addWidget(self.expTxt, 6, 0, 1, 2)
        self.fileTxt = QtWidgets.QPlainTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.fileTxt.setFont(font)
        self.fileTxt.setObjectName("fileTxt")
        self.gridLayout.addWidget(self.fileTxt, 3, 0, 1, 2)
        self.inteBt = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.inteBt.setFont(font)
        self.inteBt.setObjectName("inteBt")
        self.gridLayout.addWidget(self.inteBt, 13, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 13, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setUnderline(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.genLatexBt = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.genLatexBt.setFont(font)
        self.genLatexBt.setObjectName("genLatexBt")
        self.gridLayout.addWidget(self.genLatexBt, 21, 1, 1, 1)
        self.genPdfBt = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.genPdfBt.setFont(font)
        self.genPdfBt.setObjectName("genPdfBt")
        self.gridLayout.addWidget(self.genPdfBt, 21, 0, 1, 1)
        self.limBt = QtWidgets.QPushButton(self.centralwidget)
        self.limBt.setObjectName("limBt")
        self.gridLayout.addWidget(self.limBt, 15, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 9, 0, 1, 1)
        self.plotBt = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.plotBt.setFont(font)
        self.plotBt.setObjectName("plotBt")
        self.gridLayout.addWidget(self.plotBt, 15, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Math Expert"))
        self.label_5.setText(_translate("MainWindow", "Algebra"))
        self.titleTxt.setPlainText(_translate("MainWindow", "Title"))
        self.label_3.setText(_translate("MainWindow", "Output"))
        self.diffBt.setText(_translate("MainWindow", "Differentiate"))
        self.label_4.setText(_translate("MainWindow", "Let me do your work"))
        self.simpBt.setText(_translate("MainWindow", "Simplify"))
        self.authorTxt.setPlainText(_translate("MainWindow", "Author"))
        self.expTxt.setPlainText(_translate("MainWindow", "Expression"))
        self.fileTxt.setPlainText(_translate("MainWindow", "File"))
        self.inteBt.setText(_translate("MainWindow", "Integrate"))
        self.label_6.setText(_translate("MainWindow", "Graphics"))
        self.label.setText(_translate("MainWindow", "Math Expert"))
        self.genLatexBt.setText(_translate("MainWindow", "Generate LaTeX"))
        self.genPdfBt.setText(_translate("MainWindow", "Generate PDF"))
        self.limBt.setText(_translate("MainWindow", "Limit"))
        self.label_2.setText(_translate("MainWindow", "Calculus"))
        self.plotBt.setText(_translate("MainWindow", "Plot"))
        self.actionNew.setText(_translate("MainWindow", "New"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
