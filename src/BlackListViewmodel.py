# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import QPoint
from PyQt5.QtWidgets import QAbstractItemView, QMessageBox, QTableView

class BlackListViewmodel:

    def __init__(self, the_ban_list, the_tableview_ban, the_input_vm, the_input_form, the_button_refresh, the_button_manAdd,
                 the_button_manDel, the_button_clearAll, the_MainWindow):
        self.ban_list_model = the_ban_list
        self.tableview_ban = the_tableview_ban
        self.input_vm = the_input_vm
        self.input_form = the_input_form
        self.button_refresh = the_button_refresh
        self.button_refresh.clicked.connect(self.on_clickUpdate)
        self.button_manAdd = the_button_manAdd
        self.button_manAdd.clicked.connect(self.on_clickManAdd)
        self.button_manDel = the_button_manDel
        self.button_manDel.clicked.connect(self.on_clickManDel)
        self.button_clearAll = the_button_clearAll
        self.button_clearAll.clicked.connect(self.on_clickClearAll)
        self.mainWindow = the_MainWindow
        self.writeToTable()
        pass

    def writeToTable(self):
        row = QtGui.QStandardItemModel()
        row.setHorizontalHeaderItem(0, QtGui.QStandardItem("id"))
        i = 0
        for key in self.ban_list_model.black_list.keys():
            i = i + 1
            row.setItem(i, 0, QtGui.QStandardItem(key))
        row.sort(0, QtCore.Qt.AscendingOrder)
        self.tableview_ban.setModel(row)

    def on_clickUpdate(self):
        self.writeToTable()
        self.ban_list_model.writeBlackList()

    def on_clickManAdd(self):
        self.input_vm.tag = 2 # tag=2, add a follower into ban list. tag=3, delete a follower from ban list.
        self.input_form.show()

    def on_clickManDel(self):
        self.input_vm.tag = 3
        self.input_form.show()

    def on_clickClearAll(self):
        reply = QMessageBox.question(self.mainWindow, '警告', '确定清空？',
                                     QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel, QMessageBox.Cancel)
        if reply == QMessageBox.Yes:
            self.ban_list_model.clearBlackList()
            self.on_clickUpdate()