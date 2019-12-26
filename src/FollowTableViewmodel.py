# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import QPoint
from PyQt5.QtWidgets import QAbstractItemView, QMessageBox, QTableView

class FollowingTableViewmodel:

    def __init__(self, the_fo_list, the_tableview_fo, the_input_form, the_button_update, the_button_manAdd, the_button_manDel, the_button_clearAll, the_MainWindow):
        self.tag = 0 # tag=1, delete a follower. tag=0, add a follower
        self.fo_model = the_fo_list
        self.tableview_fo = the_tableview_fo
        self.tableview_fo.setEditTriggers(QAbstractItemView.NoEditTriggers) # forbid edit
        self.writeToTable()
        self.input_form = the_input_form
        self.button_update = the_button_update
        self.button_update.clicked.connect(self.on_clickUpdate)
        self.button_manAdd = the_button_manAdd
        self.button_manAdd.clicked.connect(self.on_clickManAdd)
        self.button_manDel = the_button_manDel
        self.button_manDel.clicked.connect(self.on_clickManDel)
        self.button_clearAll = the_button_clearAll
        self.button_clearAll.clicked.connect(self.on_clickClearAll)
        self.mainWindow = the_MainWindow
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
        row.sort(0, QtCore.Qt.AscendingOrder)
        self.tableview_fo.setModel(row)

    def on_clickUpdate(self):
        self.fo_model.readList()
        self.fo_model.writeList()
        self.writeToTable()

    def on_clickManAdd(self):
        self.tag = 0
        self.input_form.show()

    def on_clickManDel(self):
        self.tag = 1
        self.input_form.show()

    def on_clickClearAll(self):
        reply = QMessageBox.question(self.mainWindow, '警告', '确定清空？\n重新使用则必须再次导入关注列表。', QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel, QMessageBox.Cancel)
        if reply == QMessageBox.Yes:
            self.fo_model.clearAll()
            self.on_clickUpdate()
