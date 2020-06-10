from UI.pie import Ui_Dialog
from PyQt5.QtWidgets import QDialog,QMessageBox
from PyQt5.QtCore import pyqtSignal
class Dia2(QDialog,Ui_Dialog):
    window=pyqtSignal(type(list()))

    def __init__(self,df):
        super().__init__()
        self.df=df
        self.setupUi(self)
        self.setupcomboBox()
        self.name=None
        self.text=None
        self.setWindowTitle('绘制饼状图')
        self.pushButton.pressed.connect(self.getMessage)
        self.pushButton_2.pressed.connect(self.close)

    def setupcomboBox(self):
        self.comboBox_2.addItems(self.df.columns)
        self.comboBox.addItems(['None','数值分类','非数值分类'])
        self.checkBox.setChecked(True)
    def getMessage(self):
        self.name=self.lineEdit.text()
        self.dataname=self.comboBox_2.currentText()
        self.handle=self.comboBox.currentText()
        self.text=self.lineEdit_2.text()
        self.hollow=self.checkBox.isChecked()
        self.checkMessage()
    def checkMessage(self):
        if self.name ==''  :
            QMessageBox.information(self,'提示','参数不完整，请检查参数！',QMessageBox.Yes,QMessageBox.Yes)
        elif self.dataname in self.df.describe().columns and self.handle=='非数值分类':
            QMessageBox.information(self,'提示','数值类型不能进行非数值类型的分类！',QMessageBox.Yes,QMessageBox.Yes)
        elif self.dataname not in self.df.describe().columns and self.handle=='数值分类':
            QMessageBox.information(self, '提示', '非数值类型不能进行数值类型的分类！', QMessageBox.Yes, QMessageBox.Yes)
        elif self.handle !='None' and self.text =='':
            QMessageBox.information(self, '提示', '参数不完整，请检查参数！', QMessageBox.Yes, QMessageBox.Yes)

        else:
            self.window.emit([self.name,self.dataname,self.handle,self.text,self.hollow])

            self.close()

