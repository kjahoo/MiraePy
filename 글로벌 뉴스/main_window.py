# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import sys
import csv
from pandas import Series, DataFrame
import pandas as pd

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(800, 600)
        MainWindow.setWindowOpacity(1.0)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.addBtn = QtWidgets.QPushButton(self.centralwidget)
        self.addBtn.setGeometry(QtCore.QRect(355, 260, 91, 31))
        self.addBtn.setObjectName("addBtn")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 0, 781, 51))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("돋움")
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.stockEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.stockEdit.setWhatsThis("")
        self.stockEdit.setText("")
        self.stockEdit.setObjectName("stockEdit")
        self.horizontalLayout.addWidget(self.stockEdit)
        self.searchBtn = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.searchBtn.setObjectName("searchBtn")
        self.horizontalLayout.addWidget(self.searchBtn)
        self.exeBtn = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.exeBtn.setObjectName("exeBtn")
        self.horizontalLayout.addWidget(self.exeBtn)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 50, 331, 511))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.resultWidget = QtWidgets.QTableWidget(self.verticalLayoutWidget)
        self.resultWidget.setAcceptDrops(False)
        self.resultWidget.setObjectName("resultWidget")
        self.resultWidget.setColumnCount(3)
        self.resultWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.resultWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.resultWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.resultWidget.setHorizontalHeaderItem(2, item)
        self.verticalLayout.addWidget(self.resultWidget)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(460, 50, 331, 511))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.resultWidget_2 = QtWidgets.QTableWidget(self.verticalLayoutWidget_2)
        self.resultWidget_2.setObjectName("resultWidget_2")
        self.resultWidget_2.setColumnCount(3)
        self.resultWidget_2.setRowCount(20)
        item = QtWidgets.QTableWidgetItem()
        self.resultWidget_2.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.resultWidget_2.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.resultWidget_2.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.resultWidget_2.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.resultWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.resultWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.resultWidget_2.setHorizontalHeaderItem(2, item)
        self.verticalLayout_2.addWidget(self.resultWidget_2)
        self.addBtn.raise_()
        self.horizontalLayoutWidget_2.raise_()
        self.verticalLayoutWidget.raise_()
        self.verticalLayoutWidget_2.raise_()
        self.resultWidget.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.exeBtn.clicked['bool'].connect(MainWindow.setDockNestingEnabled)
        self.searchBtn.clicked.connect(self.resultWidgetItem)
        # self.stockEdit.textEdited['QString'].connect(self.resultWidgetItem)
        self.addBtn.clicked.connect(self.addBtnClicked)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.resultWidget.cellClicked.connect(self.resultWidgetClicked)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "글로벌 주식 최신 뉴스 검색"))
        self.addBtn.setText(_translate("MainWindow", "관심종목 추가"))
        self.label.setText(_translate("MainWindow", "종목명 or 코드 입력"))
        self.searchBtn.setText(_translate("MainWindow", "검색"))
        self.exeBtn.setText(_translate("MainWindow", "관심종목 뉴스보기"))
        self.label_2.setText(_translate("MainWindow", "검색결과"))
        item = self.resultWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "국가"))
        item = self.resultWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "종목코드"))
        item = self.resultWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "종목명"))
        self.label_3.setText(_translate("MainWindow", "관심종목"))
        item = self.resultWidget_2.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.resultWidget_2.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.resultWidget_2.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "3"))
        item = self.resultWidget_2.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "4"))
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
        cell = self.resultWidget.item()
        print(cell)

    def resultWidgetClicked(self, row, col):
        cell = self.self.resultWidget.Item(row, col)



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
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

