from UI.scientific_compution import *
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QDialog,QApplication,QComboBox,QTableWidgetItem,QMessageBox,QItemDelegate
from PyQt5.QtCore import pyqtSignal
def isNumbertic(data):
    try:
        data=float(data)
        result=True

    except:
        result=False
    finally:
        return result
class EmptyDelegate(QItemDelegate):
    def __init__(self, parent):
        super(EmptyDelegate, self).__init__(parent)

    def createEditor(self, QWidget, QStyleOptionViewItem, QModelIndex):
        return None
class myrSub(QDialog,Ui_Dialog):
    okButtonPressed=pyqtSignal(type(list()))
    applyButtonPressed=pyqtSignal()
    cancalButtonPressed=pyqtSignal()
    def __init__(self,df):
        super().__init__()
        self.setupUi(self)
        self.df=df
        self.Data=[]
        self.settableWidget()
        self.pushButton.pressed.connect(self.get_Message)
        self.pushButton_2.pressed.connect(self.Apply_and_emit)
        self.pushButton_3.pressed.connect(self.Cancal_and_emit)
        self.setWindowTitle('（左）减法')
        self.setWhatsThis('左减法，即你输入的参数在÷的左边\n'
                          '如： 你输入的参数÷原有数据')
    def settableWidget(self):
        col,row=(2,len(self.df.describe().columns))
        self.tableWidget.setRowCount(row)
        self.tableWidget.setColumnCount(col)
        self.tableWidget.setHorizontalHeaderLabels(['列名',  '参数'])
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        x = 0
        for s in self.df.describe().columns:
            x += 1
            newItem = QTableWidgetItem(str(s))
            NoneItem = QTableWidgetItem('Null')

            self.tableWidget.setItem(x - 1, 0, newItem)
            self.tableWidget.setItem(x - 1, 1, NoneItem)
        self.tableWidget.setItemDelegateForColumn(0, EmptyDelegate(self))
    def Apply_and_emit(self):
        self.applyButtonPressed.emit()
        self.close()
    def Cancal_and_emit(self):
        self.cancalButtonPressed.emit()
        self.close()
    def closeEvent(self, QCloseEvent):
        self.cancalButtonPressed.emit()
        self.close()
    def get_Message(self):
        data=[]
        row=self.tableWidget.rowCount()
        col=self.tableWidget.columnCount()
        for i in range(row):
            for j in range(col):
                data.append(self.tableWidget.item(i,j).text())
            if 'Null'==data[1]:
                data.clear()
            else:
                self.Data.append(data.copy())
            data.clear()

       # print(self.Data)
        if self.Data:
            wrong=False
            for i in self.Data:
                if not isNumbertic(i[1]):
                    QMessageBox.information(self,'waring','数值类型不能与非数值类型相加！\n请仔细检查输入参数。',
                                                   QMessageBox.Yes,QMessageBox.Yes)
                    wrong=True
                    self.Data.clear()
                    break


            if not wrong:
                self.okButtonPressed.emit(self.Data.copy())
                self.Data.clear()

        else:
            QMessageBox.warning(self, 'waring', '参数接收不完整,\n请检查输入参数', QMessageBox.Yes, QMessageBox.Yes)
            self.settableWidget()
            self.Data.clear()


