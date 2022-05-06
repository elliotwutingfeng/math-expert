from doc import MathDoc
from sympy import sin, cos, exp, log, sqrt, sympify, pi  # common math functions
from sympy.abc import x  # x symbols
from gui import QtWidgets, Ui_MainWindow  # gui


if __name__ == "__main__":
    # Setup the ui.
    import sys  # for command line arguments
    app = QtWidgets.QApplication(sys.argv)  # Create the application.
    MainWindow = QtWidgets.QMainWindow()  # Create the main window.
    ui = Ui_MainWindow()  # Create the ui.
    ui.setupUi(MainWindow)  # Setup the ui.

    # Setup the document and buttons.
    math_doc = MathDoc()  # The document.
    math_doc.GenPdf(ui.fileTxt.toPlainText(), ui.titleTxt.toPlainText(),
                 ui.authorTxt.toPlainText(), clean_tex=True)
    # Initialize the document.
    ui.inteBt.clicked.connect(lambda: math_doc.Inte(
        sympify(ui.expTxt.toPlainText())))  # The integral button.
    ui.diffBt.clicked.connect(lambda: math_doc.Diff(
        sympify(ui.expTxt.toPlainText())))  # The differentiation button.
    ui.plotBt.clicked.connect(lambda: math_doc.Plot(
        (ui.expTxt.toPlainText())))  # The plot button.
    ui.genPdfBt.clicked.connect(lambda: math_doc.GenPdf(ui.fileTxt.toPlainText(
    ), ui.titleTxt.toPlainText(), ui.authorTxt.toPlainText(), clean_tex=True))
    # The generate pdf button.
    ui.genLatexBt.clicked.connect(lambda: math_doc.GenTex(ui.fileTxt.toPlainText(
        ), ui.titleTxt.toPlainText(), ui.authorTxt.toPlainText()))
    # The generate tex button.

    MainWindow.show()
    sys.exit(app.exec_())
