from PyQt5.QtWidgets import QDialog,QMessageBox
from UI.corr import Ui_Dialog
from PyQt5.QtCore import pyqtSignal
class myCorr(QDialog,Ui_Dialog):
    window=pyqtSignal(type(list()))
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.radioButton_2.setCheckable(True)
        self.pushButton.pressed.connect(self.getMessage)
        self.pushButton_2.pressed.connect(self.close)
        self.setWindowTitle('相关性关系分析')

    def getMessage(self):
        self.text=[]
        if self.radioButton_2.isChecked():
            self.text.append('pearson')
        elif self.radioButton.isChecked():
            self.text.append('spearman')
        elif self.radioButton_3.isChecked():
            self.text.append('kendall')
        self.checkMessage()
    def checkMessage(self):
        if len(self.text)!=1:
            QMessageBox.information(self,'提示','请选择计算方法！',QMessageBox.Yes,QMessageBox.Yes)
        else :
            self.window.emit(self.text.copy())
            self.text.clear()
            self.close()
