from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
from pandas import Series, DataFrame
import pandas as pd
import requests


def __init__(self, parent=None):
    QtGui.QWidget.__init__(self, parent)
    self.ntableView = QtGui.QTableView()
    self.nlayout = QtGui.QVBoxLayout()
    self.nmodel = QtGui.QStandardItemModel()
    self.ntableView.setModel(self.nmodel)
    self.nlayout.addWidget(self.ntableView)
    self.setLayout(self.nlayout)
    self.func_mappingSignal()


def func_mappingSignal(self):
    self.ntableView.clicked.connect(self.func_test)


def func_test(self, item):
    # http://www.python-forum.org/viewtopic.php?f=11&t=16817
    cellContent = item.data()
    print(cellContent)  # test
    sf = "You clicked on {}".format(cellContent)
    print(sf)