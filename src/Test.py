from PyQt5.QtWidgets import QMessageBox

# 退出确定框
reply = QMessageBox.question('退出', '确定退出？', QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel, QMessageBox.Cancel)
if reply == QMessageBox.Yes:
	print('退出')
else:
	print('不退出')
