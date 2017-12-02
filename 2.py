import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import *
import pyfinance

form_class = uic.loadUiType("main_window.ui")[0]


class MainWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("관심종목")
        self.setWindowIcon(QIcon("icon16.png"))
        self.setupUi(self)

        code_list = pyfinance.get_code_list()
        self.tableWidget.setRowCount(len(code_list))



        row = 0
        for k, v in code_list.items():
            self.tableWidget.setItem(row, 0, QTableWidgetItem(k))
            self.tableWidget.setItem(row, 1, QTableWidgetItem(v))
            row = row+1

        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = MainWindow()
    mywindow.show()
    app.exec_()
