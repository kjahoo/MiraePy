# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

import PyQt5
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
import sys
import csv
from pandas import Series, DataFrame
import pandas as pd

f_code = []
f_stock = []

class MyDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.setGeometry(500, 100, 800, 300)
        self.setWindowTitle("해외주식 실시간 뉴스 보기 v0.1 - 결과")
        self.tableWidget = QTableWidget(self)
        self.tableWidget.resize(800, 290)
        self.tableWidget.setRowCount(len(f_stock))
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.setTableWidgetData()
        self.tableWidget.cellClicked.connect(self.tableWidget_clicked)

    def setTableWidgetData(self):
        column_headers = ['종목코드', '종목명', '뉴스', '시간']
        self.tableWidget.setHorizontalHeaderLabels(column_headers)

        print(f_stock)
        for row in range(len(f_stock)):
            for col in range(4):
                self.tableWidget.setItem(row, col, QTableWidgetItem(f_stock[row][col]))

        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()

    def tableWidget_clicked(self):
        import os
        aa = self.tableWidget.selectedIndexes()
        cell = set((idx.row()) for idx in aa)
        news_row = list(cell)
        print(f_stock[news_row[0]][4])
        # os.system(str(f_stock[news_row[0]][4]))
        import webbrowser
        url = f_stock[news_row[0]][4]
        webbrowser.open(url)
        webbrowser.open('https://translate.google.com/translate?sl=en&tl=ko&js=y&prev=_t&hl=ko&ie=UTF-8&u='+url)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(800, 600)
        MainWindow.setWindowOpacity(1.0)
        self.centralwidget = PyQt5.QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.addBtn = PyQt5.QtWidgets.QPushButton(self.centralwidget)
        self.addBtn.setGeometry(PyQt5.QtCore.QRect(355, 260, 91, 31))
        self.addBtn.setObjectName("addBtn")
        self.horizontalLayoutWidget_2 = PyQt5.QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(PyQt5.QtCore.QRect(10, 0, 781, 51))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout = PyQt5.QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = PyQt5.QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = PyQt5.QtGui.QFont()
        font.setFamily("돋움")
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setTextFormat(PyQt5.QtCore.Qt.RichText)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.stockEdit = PyQt5.QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.stockEdit.setWhatsThis("")
        self.stockEdit.setText("")
        self.stockEdit.setObjectName("stockEdit")
        self.horizontalLayout.addWidget(self.stockEdit)
        self.searchBtn = PyQt5.QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.searchBtn.setObjectName("searchBtn")
        self.horizontalLayout.addWidget(self.searchBtn)
        self.saveBtn = PyQt5.QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.saveBtn.setObjectName("saveBtn")
        self.horizontalLayout.addWidget(self.saveBtn)
        self.loadBtn = PyQt5.QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.loadBtn.setObjectName("loadBtn")
        self.horizontalLayout.addWidget(self.loadBtn)
        self.exeBtn = PyQt5.QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.exeBtn.setObjectName("exeBtn")
        self.horizontalLayout.addWidget(self.exeBtn)
        self.verticalLayoutWidget = PyQt5.QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(PyQt5.QtCore.QRect(10, 50, 331, 511))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = PyQt5.QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = PyQt5.QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.resultWidget = PyQt5.QtWidgets.QTableWidget(self.verticalLayoutWidget)
        self.resultWidget.setAcceptDrops(False)
        self.resultWidget.setObjectName("resultWidget")
        self.resultWidget.setColumnCount(3)
        self.resultWidget.setRowCount(0)
        item = PyQt5.QtWidgets.QTableWidgetItem()
        self.resultWidget.setHorizontalHeaderItem(0, item)
        item = PyQt5.QtWidgets.QTableWidgetItem()
        self.resultWidget.setHorizontalHeaderItem(1, item)
        item = PyQt5.QtWidgets.QTableWidgetItem()
        self.resultWidget.setHorizontalHeaderItem(2, item)
        self.verticalLayout.addWidget(self.resultWidget)
        self.verticalLayoutWidget_2 = PyQt5.QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(PyQt5.QtCore.QRect(460, 50, 331, 511))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = PyQt5.QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = PyQt5.QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.resultWidget_2 = PyQt5.QtWidgets.QTableWidget(self.verticalLayoutWidget_2)
        self.resultWidget_2.setObjectName("resultWidget_2")
        self.resultWidget_2.setColumnCount(3)
        self.resultWidget_2.setRowCount(1)
        # item = QtWidgets.QTableWidgetItem()
        # self.resultWidget_2.setVerticalHeaderItem(0, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.resultWidget_2.setVerticalHeaderItem(1, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.resultWidget_2.setVerticalHeaderItem(2, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.resultWidget_2.setVerticalHeaderItem(3, item)
        item = PyQt5.QtWidgets.QTableWidgetItem()
        self.resultWidget_2.setHorizontalHeaderItem(0, item)
        item = PyQt5.QtWidgets.QTableWidgetItem()
        self.resultWidget_2.setHorizontalHeaderItem(1, item)
        item = PyQt5.QtWidgets.QTableWidgetItem()
        self.resultWidget_2.setHorizontalHeaderItem(2, item)
        self.verticalLayout_2.addWidget(self.resultWidget_2)
        self.addBtn.raise_()
        self.horizontalLayoutWidget_2.raise_()
        self.verticalLayoutWidget.raise_()
        self.verticalLayoutWidget_2.raise_()
        self.resultWidget.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = PyQt5.QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.exeBtn.clicked['bool'].connect(self.exeButtonClicked)
        self.searchBtn.clicked.connect(self.resultWidgetItem)
        # self.stockEdit.textEdited['QString'].connect(self.resultWidgetItem)
        self.addBtn.clicked.connect(self.addBtnClicked)
        PyQt5.QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.resultWidget.cellClicked.connect(self.resultWidget_clicked)

    def retranslateUi(self, MainWindow):
        _translate = PyQt5.QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "해외주식 실시간 뉴스 보기 v0.1"))
        self.addBtn.setText(_translate("MainWindow", "관심종목 추가"))
        self.label.setText(_translate("MainWindow", "종목명 or 코드 입력"))
        self.searchBtn.setText(_translate("MainWindow", "검색"))
        self.saveBtn.setText(_translate("MainWindow", "관심종목 저장"))
        self.loadBtn.setText(_translate("MainWindow", "관심종목 불러오기"))
        self.exeBtn.setText(_translate("MainWindow", "관심종목 뉴스보기"))
        self.label_2.setText(_translate("MainWindow", "검색결과"))
        item = self.resultWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "국가"))
        item = self.resultWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "종목코드"))
        item = self.resultWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "종목명"))
        self.label_3.setText(_translate("MainWindow", "관심종목"))
        # item = self.resultWidget_2.verticalHeaderItem(0)
        # item.setText(_translate("MainWindow", "1"))
        # item = self.resultWidget_2.verticalHeaderItem(1)
        # item.setText(_translate("MainWindow", "2"))
        # item = self.resultWidget_2.verticalHeaderItem(2)
        # item.setText(_translate("MainWindow", "3"))
        # item = self.resultWidget_2.verticalHeaderItem(3)
        # item.setText(_translate("MainWindow", "4"))
        item = self.resultWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "국가"))
        item = self.resultWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "종목코드"))
        item = self.resultWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "종목명"))

    def resultWidgetItem(self):
        self.resultWidget.setRowCount(0)
        user_input = self.stockEdit.text()
        search_result = stock_search(user_input)
        # print(len(search_result.index))
        for row in range(len(search_result.index)):
            self.resultWidget.insertRow(row)
            for col in range(3):
                self.resultWidget.setItem(row, col, QTableWidgetItem(search_result.iat[row, col]))

        self.resultWidget.resizeColumnsToContents()
        self.resultWidget.resizeRowsToContents()
        self.resultWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        del user_input
        del search_result

    def addBtnClicked(self):
        aa = self.resultWidget.selectedIndexes()
        cell = set((idx.row()) for idx in aa)
        # print(list(cell)[0])
        f = []
        for i in range(3):
            f.append(self.resultWidget.item(list(cell)[0], i).text())
        # print(f)
        self.resultWidget_2.insertRow(1)
        for col in range(3):
            self.resultWidget_2.setItem(1, col, QTableWidgetItem(f[col]))
        self.resultWidget_2.resizeColumnsToContents()
        self.resultWidget_2.resizeRowsToContents()
        self.resultWidget_2.setEditTriggers(QAbstractItemView.NoEditTriggers)

        return

    def resultWidget_clicked(self):
        return

    def exeButtonClicked(self):
        f_code = []
        # print(self.resultWidget_2.rowCount())
        # print(self.resultWidget_2.item(1, 1).text())
        for i in range(self.resultWidget_2.rowCount()):
            try:
                f_code.append((self.resultWidget_2.item(i, 1).text())+':'+self.resultWidget_2.item(i, 0).text())
            except AttributeError:
                pass
        # print(f_code)
        # print(bloomberg_news(f_code[0]))

        for i in f_code:
            try:
                f_stock.append(bloomberg_news(i))
            except IndexError:
                pass
        dialog = MyDialog()
        dialog.exec_()
        # print(f_stock)
        # self.window = PyQt5.QtWidgets
        # self.ui = ShowWindow()
        # self.ui.setupUi(self.window)
        # MainWindow.hide()
        # self.window.show()
        # self.dlg = ShowWindow(self)
        # self.dlg.show()


# class ShowWindow(object):
#     def __init__(self):
#         super(ShowWindow, self).__init__()
#         self.setupUi()
#
#     def setupUi(self):
#         self.setGeometry(800, 200, 800, 300)
#         self.setWindowsTitle("Global News")
#         self.tableWidget = QTableWidget(self)
#         self.tableWidget.resize(800, 290)
#         self.tableWidget.setRowCount(len(f_stock))
#         self.tableWidget.setColumnCount(4)
#         self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
#
#         self.setTableWidgetData()
#
#     def setTableWidgetData(self):
#         column_headers = ['종목코드', '종목명', '뉴스', '시간']
#         self.tableWidget.setHorizontalHeaderLabels(column_headers)
#         print(f_stock)
#         for row in range(len(f_stock)):
#             for col in range(4):
#                 self.tableWidget.setItem(row, col, QTableWidgetItem(f_stock[row][col]))
#
#         self.tableWidget.resizeColumnsToContents()
#         self.tableWidget.resizeRowsToContents()

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


def bloomberg_news(code):

    import requests
    from bs4 import BeautifulSoup

    url = "https://www.bloomberg.com/quote/" + code
    response = requests.get(url).text
    #soup = BeautifulSoup(html, "html.parser")
    soup = BeautifulSoup(response, "html5lib")
    stock_name = soup.select(
        "section.company__c1979f17 > h1")
    news_article = soup.select("div.headline__eb73356e")
    news_time = soup.select("div.updatedAt__3fe411c9")
    link_news = soup.select('article:nth-of-type(1) > a')
    url_news = link_news[0].get('href')
    # print(stock_name)

    return [code, stock_name[0].text, news_article[0].text, news_time[0].text, url_news]


if __name__ == "__main__":
    import sys
    app = PyQt5.QtWidgets.QApplication(sys.argv)
    MainWindow = PyQt5.QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    app.exec_()
    # sys.exit(app.exec_())

