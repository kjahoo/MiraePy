import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import csv
from pandas import Series, DataFrame
import pandas as pd

form_class = uic.loadUiType("main_window.ui")[0]


class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.searchBtn.clicked.connect(self.btn_clicked)
        self.resultWidget(self)

    # def setupUi(self):
    #     self.resultWidget = QTableWidget(self)
        #
        # self.result.setRowCount(3)
        # self.result.setColumnCount(3)
        # self.result.setTableWidgetData()

    def btn_clicked(self):
        user_input = self.stockEdit.text()
        search_result = stock_search(user_input)
        # self.resultWidget.setItem(0,0,"1")
        self.resultWidget.setRowCount(len(search_result))
        for row in range(len(search_result)):
            for col in range(3):
                self.resultWidget.setItem(row, col, QTableWidgetItem(search_result[row][col]))


def stock_search(code):
    nyse = pd.read_csv('NYSE_20171204.txt')
    nyse = nyse.drop(['<date>', '<open>', '<high>', '<low>', '<close>', '<vol>'], axis=1)
    nyse['<market>'] = 'US'
    nyse = DataFrame(nyse, columns=['<market>', '<ticker>', '<name>'])

    nasdaq = pd.read_csv('NASDAQ_20171204.txt')
    nasdaq = nasdaq.drop(['<date>', '<open>', '<high>', '<low>', '<close>', '<vol>'], axis=1)
    nasdaq['<market>'] = 'US'
    nasdaq = DataFrame(nasdaq, columns=['<market>', '<ticker>', '<name>'])

    us = pd.concat([nyse, nasdaq])

    result = pd.concat(
        [DataFrame(us[us['<ticker>'].str.contains(code)]), DataFrame(us[us['<name>'].str.contains(code)])])
    result = result.drop_duplicates(['<ticker>', '<name>'], keep='first')
    return result



if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
