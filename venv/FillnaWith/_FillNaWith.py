from UI.Fillna import Ui_Dialog
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QDialog,QApplication,QComboBox,QTableWidgetItem,QMessageBox
from PyQt5.QtCore import pyqtSignal

def isNumbertic(data):
    try:
        data=float(data)
        result=True
    except :
        result=False
    finally:
        return result
def Numbertic(data):
    try:
        data=float(data)
    finally:
        return data

def isnull_empty(df):
    columns=[]
    for i in df.columns:
        if not df[df[i].isnull()].empty:
            #print(df[i].name)
            #print(df[df[i].isnull()])
            #print('--------------------------------')
            columns.append(df[i].name)
    #print(columns)
    return columns

class myFillnaWith(QDialog,Ui_Dialog):
    FillNaSignal=pyqtSignal(type(list()))
    CancalButtonPressed=pyqtSignal()
    ExitButtonPressed = pyqtSignal()
    def __init__(self,df):
        super().__init__()
        self.setupUi(self)

        self.df=df
        self.Data=[]
        self.settableWidget()
        self.pushButton.pressed.connect(self.get_Message)
        self.pushButton_2.pressed.connect(self.cancal_and_emit)
        self.pushButton_3.pressed.connect(self.close_and_initTemp)
        self.setWindowTitle('错误填充')
        self.setWhatsThis('你可以对错误数据进行填充，你可以在填充数值选项一栏中选择mean（均值）、median（中值）、max（最大值）、min（最小值）进行填充，当然，你也可以在自定义参数一栏输入任何你想要的数值或字符串进行填充。')
    def cancal_and_emit(self):
        self.CancalButtonPressed.emit()
    def close_and_initTemp(self):
        self.ExitButtonPressed.emit()
        self.close()
    def closeEvent(self, QCloseEvent):
        self.ExitButtonPressed.emit()
        self.close()
    def settableWidget(self):
        if self.df is not None and not self.df.empty:
            self.columns=isnull_empty(self.df)
            col,row=(3,len(self.columns))
            self.tableWidget.setRowCount(row)
            self.tableWidget.setColumnCount(col)
            self.tableWidget.setHorizontalHeaderLabels(['列名','填充值选项','自定义参数'])
            self.tableWidget.horizontalHeader().setStretchLastSection(True)

            x=0
            for s in self.columns:
                x+=1
                newItem=QTableWidgetItem(str(s))
                self.tableWidget.setItem(x-1,0, newItem)
                NoneItem=QTableWidgetItem('Null')
                self.tableWidget.setItem(x - 1, 2, NoneItem)
            comboxlist=['Null','mean','median','max','min']
            for i in range(len(self.columns)):
                NewcomboBox=QComboBox()
                NewcomboBox.addItems(comboxlist)
                self.tableWidget.setCellWidget(i, 1, NewcomboBox)
    def get_Message(self):
        row=self.tableWidget.rowCount()
        col=self.tableWidget.columnCount()
        data=[]
        for i in range(row):
            for j in range(col):
                if j==1:
                    data.append(self.tableWidget.cellWidget(i, j).currentText())
                else:
                    data.append(self.tableWidget.item(i, j).text())
            if 'Null'==data[1] and 'Null'==data[2]:
                data.clear()
            elif'Null'!=data[1] and 'Null'!=data[2]:
                QMessageBox.warning(self,'waring','参数错误，\n请检查输入参数。')
                self.settableWidget()

            else:
                self.Data.append(data.copy())
            data.clear()
        #print(self.Data)
        if self.Data:
            wrong=False
            for i in self.Data:
                if i[0] not in list(self.df.describe().columns) and i[1]!='Null':
                    QMessageBox.warning(self,'waring','类型不兼容1，请检查输入参数.')
                    self.Data.clear()
                    self.settableWidget()
                    wrong=True
                    break
                elif i[0]  in list(self.df.describe().columns) and i[1]=='Null' and not  isNumbertic(i[2]):
                    QMessageBox.warning(self,'waring','类型不兼容2，请检查输入参数.')
                    self.Data.clear()
                    self.settableWidget()
                    wrong=True
                    break
            if not wrong:

                self.FillNaSignal.emit(self.Data.copy())
                self.Data.clear()
        else:
            QMessageBox.warning(self,'waring','参数接收不完整,\n请检查输入参数',QMessageBox.Yes,QMessageBox.Yes)
            self.settableWidget()
            self.Data.clear()





