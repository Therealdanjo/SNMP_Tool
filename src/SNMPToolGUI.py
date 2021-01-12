import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication

from MainWindow import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
