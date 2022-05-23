from __future__ import division

from loguru import logger
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow

from func import MathDocument
from gui import QtWidgets, Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        sys.excepthook = self.except_hook
        self.setupUi(self)
        self.mathdoc = MathDocument()
        self.heading_func()
        self.expression.setFocus()

    operations = ["inte", "diff", "lim", "fact", "sol",
                  "simp", "eval", "plot", "generate_pdf", "generate_latex"]

    for func in operations:
        exec(f"""
            \n@pyqtSlot()
            \ndef on_{func}_bt_clicked(self):
            \n    self.mathdoc.{func}(self.expression.toPlainText().\
                replace(" ", ""))
        """)

    def except_hook(self, exc_type, exc_value, exc_traceback):
        """Exceptions hook to be shown

        :exc_type: TODO
        :exc_value: TODO
        :exc_traceback: TODO
        :returns: TODO

        """
        from traceback import format_tb

        logger.error(f"Exception Type: {exc_type}")
        logger.error(f"Exception Value: {exc_value}")
        logger.error(f"Exception Traceback: {format_tb(exc_traceback)}")

        errorbox = QtWidgets.QMessageBox()
        errorbox.setText(f"""Error:
                \n{exc_type}
                \n{exc_value}
                \n{format_tb(exc_traceback)}
                """)
        errorbox.exec_()

    def heading_func(self):
        self.mathdoc.doc_heading(
            self.title.toPlainText(),
            self.author.toPlainText(),
        )

    @pyqtSlot()
    def on_generate_pdf_bt_clicked(self):
        self.heading_func()
        self.mathdoc.generate_pdf(
            self.filename.text(),
            clean_tex=True
        )

    @pyqtSlot()
    def on_generate_latex_bt_clicked(self):
        self.heading_func()
        self.mathdoc.generate_tex(self.filename.text())


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
