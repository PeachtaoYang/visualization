from UI.hist import Ui_Dialog
from PyQt5.QtWidgets import QDialog,QMessageBox,QColorDialog
from PyQt5.QtCore import pyqtSignal
def isNumbertic(data):
    try:
        data=float(data)
        return True
    except:
        return False
class Dia5(QDialog,Ui_Dialog):
    window =pyqtSignal(type(list()))
    def __init__(self,df):
        super().__init__()
        self.setupUi(self)
        self.df=df
        self.color='#000000'
        self.pushButton.pressed.connect(self.get_color)
        self.setupcomboBox()
        self.setWindowTitle('绘制频率分布直方图')
    def setupcomboBox(self):

        self.comboBox.addItems(self.df.describe().columns)
        self.pushButton_2.pressed.connect(self.getMessage)
        self.pushButton_3.pressed.connect(self.close)
        self.pushButton.setStyleSheet("background-color: {}".format('#000000'))
    def get_color(self):
        self.color = QColorDialog.getColor().name()
        self.pushButton.setStyleSheet("background-color: {}".format(self.color))
    def getMessage(self):
        self.name=self.lineEdit.text()
        self.xlabel=self.lineEdit_2.text()
        self.ylabel=self.lineEdit_3.text()
        self.dataname=self.comboBox.currentText()
        self.start=self.lineEdit_4.text()
        self.end = self.lineEdit_5.text()
        self.step = self.lineEdit_6.text()

        self.checkMessage()
    def checkMessage(self):
        if self.name=='' or self.dataname=='None' or self.xlabel=='' or self.ylabel=='':
            QMessageBox.information(self,'提示','参数接收不完整，请仔细检查！',QMessageBox.Yes,QMessageBox.Yes)
        elif self.start =='' or self.end=='' or self.step=='':
            QMessageBox.information(self, '提示', '参数接收不完整，请仔细检查！', QMessageBox.Yes, QMessageBox.Yes)
        elif not isNumbertic(self.start) and not isNumbertic(self.end) and not isNumbertic(self.step):
            QMessageBox.information(self, '提示', '请在起始数值、终止数值、步长处填数值参数，请仔细检查！', QMessageBox.Yes, QMessageBox.Yes)
        else:
            self.window.emit([self.name,self.xlabel,self.ylabel,self.dataname,self.start,self.end,self.step,self.color])

