from UI.bar import Ui_Dialog
from PyQt5.QtWidgets import QDialog,QMessageBox,QColorDialog
from PyQt5.QtCore import pyqtSignal
class Dia3(QDialog,Ui_Dialog):
    window =pyqtSignal(type(list()))
    def __init__(self,df):
        super().__init__()
        self.setupUi(self)
        self.df=df
        self.color='#000000'
        self.pushButton_3.pressed.connect(self.get_color)
        self.setupcomboBox()
        self.setWindowTitle('绘制柱状图')
    def setupcomboBox(self):
        self.comboBox_2.addItems(self.df.columns)
        self.comboBox.addItems(['None','数值分类','非数值分类'])
        self.pushButton.pressed.connect(self.getMessage)
        self.pushButton_2.pressed.connect(self.close)
        self.pushButton_3.setStyleSheet("background-color: {}".format('#000000'))
    def get_color(self):
        self.color = QColorDialog.getColor().name()
        self.pushButton_3.setStyleSheet("background-color: {}".format(self.color))
    def getMessage(self):
        self.name=self.lineEdit.text()
        self.xlabel=self.lineEdit_3.text()
        self.ylabel=self.lineEdit_4.text()
        self.dataname=self.comboBox_2.currentText()
        self.handle=self.comboBox.currentText()
        self.text=self.lineEdit_2.text()
        self.checkMessage()
    def checkMessage(self):
        if self.name=='' or self.dataname=='None' or self.xlabel=='' or self.ylabel=='':
            QMessageBox.information(self,'提示','参数接收不完整，请仔细检查！',QMessageBox.Yes,QMessageBox.Yes)
        elif self.dataname in self.df.describe().columns and self.handle=='非数值分类':
            QMessageBox.information(self,'提示','参数类型不支持，请仔细检查！',QMessageBox.Yes,QMessageBox.Yes)
        elif self.dataname not in self.df.describe().columns  and self.handle=='数值分类':
            QMessageBox.information(self, '提示', '参数类型不支持，请仔细检查！', QMessageBox.Yes, QMessageBox.Yes)
        elif self.handle !='None' and self.text=='':
            QMessageBox.information(self, '提示', '参数类型不完整，请仔细检查！', QMessageBox.Yes, QMessageBox.Yes)
        else:
            self.window.emit([self.name,self.dataname,self.handle,self.text,self.color,self.xlabel,self.ylabel])

