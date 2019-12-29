# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QTableView, QMessageBox
import re as regex

class InputFormViewmodel:

    def __init__(self, the_fo_list, the_ban_list, the_input_form, the_input_window, the_main_window):
        self.fo_model = the_fo_list
        self.ban_model = the_ban_list
        self.input_form = the_input_form
        self.input_form.pushButton_i_can.clicked.connect(self.on_clicked_i_can)
        self.input_form.pushButton_i_cant.clicked.connect(self.on_clicked_i_cant)
        self.input_window = the_input_window
        self.main_window = the_main_window
        self.tag = 0
        pass

    def on_clicked_i_can(self):
        id = self.input_form.lineEdit_edit_id.text()
        name = self.input_form.lineEdit_edit_name.text()
        check_error = regex.findall("[^a-zA-Z0-9_]",id) # check error: some chars not a-z A-Z 0-9
        if (not len(check_error) == 0) or (len(id) == 0):
            QMessageBox.warning(self.input_window,'错误','id格式有误', QMessageBox.Yes)
        else:
            if self.tag == 0: # tag=0, add a follower. tag=1, delete a follower.
                self.fo_model.appendfollower(id, name)
                self.main_window.pushButton_fo_updateList.click()
                self.input_window.close()
                self.input_form.lineEdit_edit_id.setText("")
                self.input_form.lineEdit_edit_name.setText("")
                QMessageBox.information(self.input_window, '成功', '成功添加关注者(id:'+id+')', QMessageBox.Yes)
            elif self.tag == 1:
                if id in self.fo_model.following_list.keys():
                    QMessageBox.information(self.input_window, '成功', '删除关注者(id:'+id+')', QMessageBox.Yes)
                    self.input_window.close()
                    self.input_form.lineEdit_edit_id.setText("")
                    self.input_form.lineEdit_edit_name.setText("")
                else:
                    QMessageBox.information(self.input_window, '失败', '未找到关注者(id:'+id+')', QMessageBox.Yes)
                self.fo_model.deletefollower(id)
                self.main_window.pushButton_fo_updateList.click()
            elif self.tag == 2: # tag=2, add a follower into ban list. tag=3, delete a follower from ban list.
                self.ban_model.banUser(id)
                self.main_window.pushButton_black_refresh.click()
                self.input_window.close()
                self.input_form.lineEdit_edit_id.setText("")
                self.input_form.lineEdit_edit_name.setText("")
                QMessageBox.information(self.input_window, '成功', '成功添加忽略规则(id:' + id + ')', QMessageBox.Yes)
            elif self.tag == 3:
                success = self.ban_model.unbanUser(id)
                self.main_window.pushButton_black_refresh.click()
                if success:
                    QMessageBox.information(self.input_window, '成功', '删除忽略规则(id:' + id + ')', QMessageBox.Yes)
                    self.input_window.close()
                    self.input_form.lineEdit_edit_id.setText("")
                    self.input_form.lineEdit_edit_name.setText("")
                else:
                    QMessageBox.information(self.input_window, '失败', '未找到(id:' + id + ')', QMessageBox.Yes)

    def on_clicked_i_cant(self):
        self.input_window.close()
        print("kjhk")