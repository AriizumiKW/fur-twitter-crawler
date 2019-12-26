# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QTableView, QMessageBox
import re as regex

class InputFormViewmodel:

    def __init__(self, the_fo_list, the_input_form, the_input_window, the_main_viewmodel, the_main_window):
        self.fo_model = the_fo_list
        self.input_form = the_input_form
        self.input_form.pushButton_i_can.clicked.connect(self.on_clicked_i_can)
        self.input_form.pushButton_i_cant.clicked.connect(self.on_clicked_i_cant)
        self.input_window = the_input_window
        self.main_viewmodel = the_main_viewmodel
        self.main_window = the_main_window
        pass

    def on_clicked_i_can(self):
        id = self.input_form.lineEdit_edit_id.text()
        name = self.input_form.lineEdit_edit_name.text()
        check_error = regex.findall("[^a-zA-Z0-9_]",id) # check error: some chars not a-z A-Z 0-9
        if (not len(check_error) == 0) or (len(id) == 0):
            QMessageBox.warning(self.input_window,'错误','id格式有误',QMessageBox.Yes)
        else:
            if self.main_viewmodel.tag == 0:
                self.fo_model.appendfollower(id, name)
                self.input_form.lineEdit_edit_id.setText("")
                self.input_form.lineEdit_edit_name.setText("")
                self.main_window.pushButton_fo_updateList.click()
                self.input_window.close()
                QMessageBox.information(self.input_window, '成功', '添加关注者(id:'+id+')', QMessageBox.Yes)
            else:
                if id in self.fo_model.following_list.keys():
                    QMessageBox.information(self.input_window, '成功', '删除关注者(id:'+id+')', QMessageBox.Yes)
                else:
                    QMessageBox.information(self.input_window, '失败', '未找到关注者(id:'+id+')', QMessageBox.Yes)
                self.fo_model.deletefollower(id)
                self.input_form.lineEdit_edit_id.setText("")
                self.input_form.lineEdit_edit_name.setText("")
                self.main_window.pushButton_fo_updateList.click()
                self.input_window.close()

    def on_clicked_i_cant(self):
        self.input_window.close()
        print("kjhk")