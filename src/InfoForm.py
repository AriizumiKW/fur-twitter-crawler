# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'info.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form_instruction(object):
    def setupUi(self, Form_instruction):
        Form_instruction.setObjectName("Form_instruction")
        Form_instruction.resize(337, 225)
        self.textBrowser_instruction = QtWidgets.QTextBrowser(Form_instruction)
        self.textBrowser_instruction.setGeometry(QtCore.QRect(30, 20, 271, 191))
        self.textBrowser_instruction.setObjectName("textBrowser_instruction")

        self.retranslateUi(Form_instruction)
        QtCore.QMetaObject.connectSlotsByName(Form_instruction)

    def retranslateUi(self, Form_instruction):
        _translate = QtCore.QCoreApplication.translate
        Form_instruction.setWindowTitle(_translate("Form_instruction", "Form"))
        self.textBrowser_instruction.setHtml(_translate("Form_instruction", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\';\">使用说明在Github上，自取：</span></p></body></html>"))
