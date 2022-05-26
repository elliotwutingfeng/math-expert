# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt5/main.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(611, 623)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/media/logo2.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.filename = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.filename.setFont(font)
        self.filename.setObjectName("filename")
        self.gridLayout.addWidget(self.filename, 3, 0, 1, 2)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setUnderline(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 9, 0, 1, 1)
        self.expression = QtWidgets.QPlainTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.expression.setFont(font)
        self.expression.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.expression.setTabChangesFocus(True)
        self.expression.setObjectName("expression")
        self.gridLayout.addWidget(self.expression, 6, 0, 1, 2)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 20, 0, 1, 1)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("border:0;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(80, 0, 81, 71))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap(":/newPrefix/media/logo1.jpeg"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.frame, 1, 1, 1, 1)
        self.author = QtWidgets.QPlainTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.author.setFont(font)
        self.author.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.author.setTabChangesFocus(True)
        self.author.setObjectName("author")
        self.gridLayout.addWidget(self.author, 5, 0, 1, 2)
        self.simp_bt = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.simp_bt.setFont(font)
        self.simp_bt.setObjectName("simp_bt")
        self.gridLayout.addWidget(self.simp_bt, 10, 1, 1, 1)
        self.plot_bt = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.plot_bt.setFont(font)
        self.plot_bt.setObjectName("plot_bt")
        self.gridLayout.addWidget(self.plot_bt, 15, 1, 1, 1)
        self.inte_bt = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.inte_bt.setFont(font)
        self.inte_bt.setObjectName("inte_bt")
        self.gridLayout.addWidget(self.inte_bt, 11, 0, 1, 1)
        self.eval_bt = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.eval_bt.setFont(font)
        self.eval_bt.setObjectName("eval_bt")
        self.gridLayout.addWidget(self.eval_bt, 15, 0, 1, 1)
        self.diff_bt = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.diff_bt.setFont(font)
        self.diff_bt.setStyleSheet("")
        self.diff_bt.setObjectName("diff_bt")
        self.gridLayout.addWidget(self.diff_bt, 10, 0, 1, 1)
        self.title = QtWidgets.QPlainTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.title.setFont(font)
        self.title.setTabChangesFocus(True)
        self.title.setObjectName("title")
        self.gridLayout.addWidget(self.title, 4, 0, 1, 2)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 13, 1, 1, 1)
        self.generate_latex_bt = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.generate_latex_bt.setFont(font)
        self.generate_latex_bt.setObjectName("generate_latex_bt")
        self.gridLayout.addWidget(self.generate_latex_bt, 21, 1, 1, 1)
        self.generate_pdf_bt = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.generate_pdf_bt.setFont(font)
        self.generate_pdf_bt.setObjectName("generate_pdf_bt")
        self.gridLayout.addWidget(self.generate_pdf_bt, 21, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setItalic(True)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.lim_bt = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lim_bt.setFont(font)
        self.lim_bt.setObjectName("lim_bt")
        self.gridLayout.addWidget(self.lim_bt, 12, 0, 1, 1)
        self.fact_bt = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.fact_bt.setFont(font)
        self.fact_bt.setObjectName("fact_bt")
        self.gridLayout.addWidget(self.fact_bt, 11, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 13, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 9, 1, 1, 1)
        self.sol_bt = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.sol_bt.setFont(font)
        self.sol_bt.setObjectName("sol_bt")
        self.gridLayout.addWidget(self.sol_bt, 12, 1, 1, 1)
        self.label_8.raise_()
        self.plot_bt.raise_()
        self.inte_bt.raise_()
        self.label_4.raise_()
        self.simp_bt.raise_()
        self.sol_bt.raise_()
        self.eval_bt.raise_()
        self.fact_bt.raise_()
        self.label_5.raise_()
        self.diff_bt.raise_()
        self.author.raise_()
        self.label_6.raise_()
        self.label_2.raise_()
        self.label.raise_()
        self.label_3.raise_()
        self.expression.raise_()
        self.title.raise_()
        self.frame.raise_()
        self.generate_pdf_bt.raise_()
        self.generate_latex_bt.raise_()
        self.filename.raise_()
        self.lim_bt.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.filename, self.title)
        MainWindow.setTabOrder(self.title, self.author)
        MainWindow.setTabOrder(self.author, self.expression)
        MainWindow.setTabOrder(self.expression, self.diff_bt)
        MainWindow.setTabOrder(self.diff_bt, self.fact_bt)
        MainWindow.setTabOrder(self.fact_bt, self.eval_bt)
        MainWindow.setTabOrder(self.eval_bt, self.lim_bt)
        MainWindow.setTabOrder(self.lim_bt, self.generate_latex_bt)
        MainWindow.setTabOrder(self.generate_latex_bt, self.generate_pdf_bt)
        MainWindow.setTabOrder(self.generate_pdf_bt, self.sol_bt)
        MainWindow.setTabOrder(self.sol_bt, self.simp_bt)
        MainWindow.setTabOrder(self.simp_bt, self.inte_bt)
        MainWindow.setTabOrder(self.inte_bt, self.plot_bt)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Math Expert"))
        self.filename.setText(_translate("MainWindow", "MathDocument"))
        self.label.setText(_translate("MainWindow", "Math Expert"))
        self.label_2.setText(_translate("MainWindow", "Calculus"))
        self.expression.setPlainText(_translate("MainWindow", "(sin(x)^2-cos(x)^2)/(cos(x)^2*sin(x)^2)"))
        self.label_3.setText(_translate("MainWindow", "Output"))
        self.author.setPlainText(_translate("MainWindow", "Marawan, SalahDin, Younis"))
        self.simp_bt.setText(_translate("MainWindow", "Simplify"))
        self.simp_bt.setShortcut(_translate("MainWindow", "Alt+S"))
        self.plot_bt.setText(_translate("MainWindow", "Plot"))
        self.plot_bt.setShortcut(_translate("MainWindow", "Ctrl+P"))
        self.inte_bt.setText(_translate("MainWindow", "Integrate"))
        self.inte_bt.setShortcut(_translate("MainWindow", "Ctrl+I"))
        self.eval_bt.setText(_translate("MainWindow", "Evaluate"))
        self.eval_bt.setShortcut(_translate("MainWindow", "Ctrl+E"))
        self.diff_bt.setText(_translate("MainWindow", "Differentiate"))
        self.diff_bt.setShortcut(_translate("MainWindow", "Ctrl+D"))
        self.title.setPlainText(_translate("MainWindow", "STEM Luxor Grade 12 Math Project"))
        self.label_6.setText(_translate("MainWindow", "Graphics"))
        self.generate_latex_bt.setText(_translate("MainWindow", "Generate LaTeX"))
        self.generate_latex_bt.setShortcut(_translate("MainWindow", "Alt+Return"))
        self.generate_pdf_bt.setText(_translate("MainWindow", "Generate PDF"))
        self.generate_pdf_bt.setShortcut(_translate("MainWindow", "Ctrl+Return"))
        self.label_4.setText(_translate("MainWindow", "Let me do your work"))
        self.lim_bt.setText(_translate("MainWindow", "Limit"))
        self.lim_bt.setShortcut(_translate("MainWindow", "Ctrl+L"))
        self.fact_bt.setText(_translate("MainWindow", "Factorize"))
        self.fact_bt.setShortcut(_translate("MainWindow", "Ctrl+F"))
        self.label_8.setText(_translate("MainWindow", "General"))
        self.label_5.setText(_translate("MainWindow", "Algebra"))
        self.sol_bt.setText(_translate("MainWindow", "Solve for X"))
        self.sol_bt.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionNew.setText(_translate("MainWindow", "New"))
import media_rc