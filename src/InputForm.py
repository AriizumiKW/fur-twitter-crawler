# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'input.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form_Input(object):
    def setupUi(self, Form_Input):
        Form_Input.setObjectName("Form_Input")
        Form_Input.resize(320, 200)
        self.lineEdit_edit_id = QtWidgets.QLineEdit(Form_Input)
        self.lineEdit_edit_id.setGeometry(QtCore.QRect(100, 40, 121, 31))
        self.lineEdit_edit_id.setText("")
        self.lineEdit_edit_id.setObjectName("lineEdit_edit_id")
        self.lineEdit_edit_name = QtWidgets.QLineEdit(Form_Input)
        self.lineEdit_edit_name.setGeometry(QtCore.QRect(100, 90, 121, 31))
        self.lineEdit_edit_name.setText("")
        self.lineEdit_edit_name.setObjectName("lineEdit_edit_name")
        self.pushButton_i_can = QtWidgets.QPushButton(Form_Input)
        self.pushButton_i_can.setGeometry(QtCore.QRect(50, 150, 93, 28))
        self.pushButton_i_can.setObjectName("pushButton_i_can")
        self.pushButton_i_cant = QtWidgets.QPushButton(Form_Input)
        self.pushButton_i_cant.setGeometry(QtCore.QRect(180, 150, 93, 28))
        self.pushButton_i_cant.setObjectName("pushButton_i_cant")
        self.label = QtWidgets.QLabel(Form_Input)
        self.label.setGeometry(QtCore.QRect(40, 50, 51, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form_Input)
        self.label_2.setGeometry(QtCore.QRect(35, 95, 61, 16))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Form_Input)
        QtCore.QMetaObject.connectSlotsByName(Form_Input)

    def retranslateUi(self, Form_Input):
        _translate = QtCore.QCoreApplication.translate
        Form_Input.setWindowTitle(_translate("Form_Input", "Form"))
        self.pushButton_i_can.setText(_translate("Form_Input", "我可以"))
        self.pushButton_i_cant.setText(_translate("Form_Input", "我不行"))
        self.label.setText(_translate("Form_Input", "用户ID"))
        self.label_2.setText(_translate("Form_Input", "用户名字"))
