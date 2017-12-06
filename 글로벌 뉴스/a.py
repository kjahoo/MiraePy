import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("main_window.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUI(self):
        self.setGeometry(800, 400, 300, 150)

        # Label
        label = QLabel("종목코드", self)
        label.move(10, 10)

        # LineEdit
        self.StockEdit = QLineEdit("", self)
        self.StockEdit.move(80, 20)
        self.StockEdit.textChanged.connect(self.lineEditChanged)

        # Search Button
        self.searchBtn.clicked.connect(QCoreApplication.instance().quit)

        # StatusBar
        self.statusBar = QStatusBar(self)
        self.setStatusBar(self.statusBar)

    def lineEditChanged(self):
        self.statusBar.showMessage(self.StockEdit.text())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()