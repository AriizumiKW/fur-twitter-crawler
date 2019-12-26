# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import QPoint
from PyQt5.QtWidgets import QAbstractItemView, QMessageBox, QTableView
from src import FollowListModel as flist

class FollowingTableViewmodel:

    def __init__(self, the_tableview_fo, the_button_update, the_button_manAdd):
        self.fo_model = flist.FollowingListModel()
        self.tableview_fo = the_tableview_fo
        self.tableview_fo.setEditTriggers(QAbstractItemView.NoEditTriggers) # forbid edit
        self.writeToTable()
        self.button_update = the_button_update
        self.button_update.clicked.connect(self.on_clickUpdate)
        self.button_manAdd = the_button_manAdd
        self.button_manAdd.clicked.connect(self.on_clickManAdd)
        pass

    def writeToTable(self):
        row = QtGui.QStandardItemModel()
        row.setHorizontalHeaderItem(0, QtGui.QStandardItem("id"))
        row.setHorizontalHeaderItem(1, QtGui.QStandardItem("name"))
        i = 0
        for key in self.fo_model.following_list.keys():
            i = i + 1
            row.setItem(i, 0, QtGui.QStandardItem(key))
            row.setItem(i, 1, QtGui.QStandardItem(self.fo_model.following_list[key]))
        row.sort(0, QtCore.Qt.DescendingOrder)
        self.tableview_fo.setModel(row)

    def on_clickUpdate(self):
        self.fo_model.readList()
        self.fo_model.writeList()
        self.writeToTable()
        print("yyy")

    def on_clickManAdd(self):
        myQPoint = QPoint()
        myQPoint.setX(2)
        myQPoint.setY(1)
        myIndex = self.tableView_fo.indexAt(myQPoint)
        self.tableView_fo.setCurrentIndex(QTableView.model(2, 2))


