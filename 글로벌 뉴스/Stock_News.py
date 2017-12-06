import Bloomberg

f_stock = []
f_stock.append(Bloomberg.bloomberg_news("7974:JP"))
f_stock.append(Bloomberg.bloomberg_news("AMZN:US"))
f_stock.append(Bloomberg.bloomberg_news("TSLA:US"))
f_stock.append(Bloomberg.bloomberg_news('700:HK'))

# for k in range(len(f_stock)):
#     for v in range(5):
#         print(f_stock[k][v])

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setGeometry(800, 200, 800, 300)

        self.tableWidget = QTableWidget(self)
        self.tableWidget.resize(800, 290)
        self.tableWidget.setRowCount(len(f_stock))
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.setTableWidgetData()

    def setTableWidgetData(self):
        column_headers = ['종목코드', '종목명', '뉴스', '시간']
        self.tableWidget.setHorizontalHeaderLabels(column_headers)

        for row in range(len(f_stock)):
            for col in range(4):
                self.tableWidget.setItem(row, col, QTableWidgetItem(f_stock[row][col]))

        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()