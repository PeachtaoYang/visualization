from UI.Forced_type_conversion import Ui_Dialog
from PyQt5.QtWidgets import QDialog,QApplication,QComboBox,QTableWidgetItem,QMessageBox,QItemDelegate
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QIcon
import numpy as np
from ForcedTypeConversion.timeRadioButton import mytimeRadio

class EmptyDelegate(QItemDelegate):
    def __init__(self, parent):
        super(EmptyDelegate, self).__init__(parent)

    def createEditor(self, QWidget, QStyleOptionViewItem, QModelIndex):
        return None

class myTypeConversion(QDialog,Ui_Dialog):
    okButtonPressed=pyqtSignal(type(list()))
    applyButtonPressed=pyqtSignal()
    cancalButtonPressed=pyqtSignal()
    def __init__(self,df):
        super().__init__()
        self.setupUi(self)
        self.df=df
        self.Data = []
        self.formatStr=[]
        self.pushButton.pressed.connect(self.get_Message)
        self.pushButton_3.pressed.connect(self.close)
        self.setWindowTitle('强制类型转换')
        self.setWindowIcon(QIcon(r'Z:\Data_Visualization\venv\qrc\icons\icon.png'))
        self.setWhatsThis('你可以对数据类型进行强制转换，当然这是建立在类型转换支持的基础上，你可以在参数一栏选择需要转换的类型，如果转换不支持，将不会有任何对原数据的修改。')
        self.settableWidget()

    def settableWidget(self):
        col, row = (3, len(self.df.columns))
        self.tableWidget.setRowCount(row)
        self.tableWidget.setColumnCount(col)
        self.tableWidget.setHorizontalHeaderLabels(['列名','类型' ,'参数'])
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        comboxlist=['Null','int (整数)','float  (小数)','string  (字符串)']
        x = 0
        for s in self.df.columns:
            x += 1
            newItem = QTableWidgetItem(str(s))
            oneItem = QTableWidgetItem(str(self.df[s].dtype))
            NewcomboBox = QComboBox()
            NewcomboBox.addItems(comboxlist)
            self.tableWidget.setItem(x - 1, 0, newItem)
            self.tableWidget.setItem(x - 1, 1, oneItem)
            self.tableWidget.setCellWidget(x-1, 2, NewcomboBox)
        self.tableWidget.setItemDelegateForColumn(0, EmptyDelegate(self))
        self.tableWidget.setItemDelegateForColumn(1, EmptyDelegate(self))


    def get_Message(self):

        row=self.tableWidget.rowCount()


        for i in range(row):
            temp = self.tableWidget.cellWidget(i,2).currentText()
            if temp !='Null':

                self.Data.append([self.tableWidget.item(i,0).text(),temp])
        if  self.Data:



            self.okButtonPressed.emit(self.Data.copy())
            self.Data.clear()
        else:
            self.Data.clear()
            QMessageBox.information(self,'waring','参数输入不完整，请检查！',QMessageBox.Yes,QMessageBox.Yes)





