import Bloomberg

f_stock = []
f_stock.append(Bloomberg.bloomberg_news("7974:JP"))
f_stock.append(Bloomberg.bloomberg_news("AMZN:US"))
f_stock.append(Bloomberg.bloomberg_news("TSLA:US"))
f_stock.append(Bloomberg.bloomberg_news('700:HK'))

print(f_stock)

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

column_idx_lookup = {'code': 0, 'name': 1, 'cprice': 2}
#
# class MyWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setupUI()
#
#     def setupUI(self):
#         self.setGeometry(800, 200, 300, 300)
#
#         self.tableWidget = QTableWidget(self)
#         self.tableWidget.resize(290, 290)
#         self.tableWidget.setRowCount(5)
#         self.tableWidget.setColumnCount(3)
#         self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
#
#         self.setTableWidgetData()
#
#     def setTableWidgetData(self):
#         column_headers = ['종목코드', '종목명', '종가']
#         self.tableWidget.setHorizontalHeaderLabels(column_headers)
#
#         for k, v in kospi_top5.items():
#             col = column_idx_lookup[k]
#             for row, val in enumerate(v):
#                 item = QTableWidgetItem(val)
#                 if col == 2:
#                     item.setTextAlignment(Qt.AlignVCenter | Qt.AlignRight)
#
#                 self.tableWidget.setItem(row, col, item)
#
#         self.tableWidget.resizeColumnsToContents()
#         self.tableWidget.resizeRowsToContents()
#
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     mywindow = MyWindow()
#     mywindow.show()
#     app.exec_()