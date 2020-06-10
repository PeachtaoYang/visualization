from UI.Selection import Ui_Dialog
from PyQt5.QtWidgets import QDialog,QApplication,QComboBox,QTableWidgetItem,QMessageBox,QItemDelegate
from PyQt5.QtCore import pyqtSignal

import sys
import pandas as pd
class EmptyDelegate(QItemDelegate):
    def __init__(self, parent):
        super(EmptyDelegate, self).__init__(parent)

    def createEditor(self, QWidget, QStyleOptionViewItem, QModelIndex):
        return None
class mySelection(QDialog,Ui_Dialog):
    SelectionSignal=pyqtSignal(type(list()))
    closeButtonPressed=pyqtSignal()
    def __init__(self,df):
        super().__init__()
        self.setupUi(self)
        self.df=df
        self.Data=[]
        self.settableWidget()
        self.pushButton.pressed.connect(self.get_Message)
        self.pushButton_2.pressed.connect(self.close_and_emit)
        self.setWindowTitle('筛选')
        self.setWhatsThis('你可以对数据进行筛选操作，read only 这一操作表示只读，'
                          '对数据筛选只是形成一份数据视图，inplace操作表示对原数据'
                          '进行修改，你可以对各列数据进行筛选，每一行条件判断都是取'
                          '并集，read only 在筛选之后点击cancal按钮，数据视图将会'
                          '还原，而inplace 将直接修改原数据，以方便进行可视化操作。'
                          )

    def close_and_emit(self):
        self.closeButtonPressed.emit()
        self.close()
    def closeEvent(self, QCloseEvent):
        self.closeButtonPressed.emit()
        self.close()
    def settableWidget(self):
        if self.df is not None and not self.df.empty:
            col,row=(6,len(self.df.columns))
            self.tableWidget.setRowCount(row)
            self.tableWidget.setColumnCount(col)
            self.tableWidget.setHorizontalHeaderLabels(['列名','操作符','参数','附加','操作','参数'])
            #self.tableView.model.setVerticalHeaderLabels(list(map(str,range(len(self.df.columns)))))
            self.tableWidget.horizontalHeader().setStretchLastSection(True)
            #self.tableWidget.setInputMethodHints(Qt.ImhHiddenText)


            x=0
            for s in self.df.columns:
                x+=1
                newItem=QTableWidgetItem(str(s))
                NoneItem=QTableWidgetItem('Null')
                NoneItem1=QTableWidgetItem('Null')
                self.tableWidget.setItem(x-1,0, newItem)
                self.tableWidget.setItem(x - 1, 2, NoneItem)
                self.tableWidget.setItem(x - 1, 5, NoneItem1)

            comboxlist = ['Null', '>', '<', '≠','=']
            comboxlist1 = ['Null', 'or', 'and']
            for i in range(len(self.df.columns)):
                NewcomboBox=QComboBox()
                NewcomboBox.addItems(comboxlist)
                NewcomboBox1=QComboBox()
                NewcomboBox1.addItems(comboxlist1)
                NewcomboBox2=QComboBox()
                NewcomboBox2.addItems(comboxlist)
                self.tableWidget.setCellWidget(i,1,NewcomboBox)
                self.tableWidget.setCellWidget(i, 3, NewcomboBox1)
                self.tableWidget.setCellWidget(i, 4, NewcomboBox2)
        self.tableWidget.setItemDelegateForColumn(0, EmptyDelegate(self))

    def get_Message(self):


        data=[]
        row=self.tableWidget.rowCount()
        col=self.tableWidget.columnCount()
        #print(self.tableWidget.item(0, 0).text())
        #print(self.tableWidget.cellWidget(0,1).currentText())

        for i in range(row):
            for j in range(col):
                if j==1 or j==3 or j==4:
                    data.append(self.tableWidget.cellWidget(i,j).currentText())
                else:
                    data.append(self.tableWidget.item(i,j).text())
            if 'Null' == data[1]  or  'Null'==data[2]:
                data.clear()
            else:
                self.Data.append(data.copy())

            data.clear()
        if  self.Data:
            #print(self.Data)
            #print(list(self.df.describe().columns))
            '''
            类型检查
            '''
            wrong=False
            for i in self.Data:
                if i[0] not in list(self.df.describe().columns)and i[1]!='≠'and i[1]!='=' :
                    QMessageBox.information(self,'waring','“{}”参数类型不支持该逻辑操作,\n请检查参数类型或者进行类型转换。'.format(i[0]),QMessageBox.Yes,QMessageBox.Yes)
                    self.Data.clear()
                    self.settableWidget()
                    wrong=True
                    break
            if not wrong:
                self.SelectionSignal.emit(self.Data.copy())
                self.Data.clear()



        else:
            QMessageBox.warning(self,'waring','参数接收不完整,\n请检查输入参数',QMessageBox.Yes,QMessageBox.Yes)
            self.settableWidget()
            self.Data.clear()

