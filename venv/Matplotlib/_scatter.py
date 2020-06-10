from UI.scatter import Ui_Dialog
from PyQt5.QtWidgets import QApplication, QDialog, QColorDialog, QHeaderView, QAbstractItemView, QMessageBox
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QColor
import sys
import pandas as pd
from PyQt5.QtCore import pyqtSignal
def DataHandle(df):
    df = pd.Series(df)
    df = pd.DataFrame(df).T
    return df
class Dia1(QDialog, Ui_Dialog):
    window = pyqtSignal(type(list()))

    def __init__(self, df):
        super().__init__()
        self.setupUi(self)
        self.df = df
        self.Datas = []
        self.title = None
        self.x_label = None
        self.y_label = None
        self.setWindowTitle('绘制散点图')
        self.tablewidgetDatasseted = False
        self.setupcomboBox()
        self.pushButton_2.pressed.connect(self.getMessage)
        self.pushButton.pressed.connect(self.getLineColor)
        self.pushButton_5.pressed.connect(self.getRowIndex_and_Delete)
        self.pushButton_6.pressed.connect(self.Clear)
        self.pushButton_6.setEnabled(False)
        self.pushButton_3.pressed.connect(self.checkMessage)
        self.pushButton_4.pressed.connect(self.close)
    def setupcomboBox(self):
        # 默认颜色设置
        self.pushButton.setStyleSheet("background-color: {}".format('#000000'))
        self.color = '#000000'
        # 自变量xcombobox设置
        self.comboBox.addItems(self.df.columns)
        #self.comboBox.addItem('其它序列')
        # 因变量设置
        self.comboBox_2.addItems(self.df.columns)
        #self.comboBox_2.addItem('其它序列')
        # x标签字体大小设置
        self.comboBox_8.addItem('None')
        self.comboBox_8.addItems(map(str, range(1, 51)))


        # y标签字体大小设置
        self.comboBox_9.addItem('None')
        self.comboBox_9.addItems(map(str, range(1, 51)))
        # 标记风格设置
        self.comboBox_3.addItem('None')
        self.comboBox_3.addItems(
            [   '  ●  (圆点)',
                    '  ,  (像素点)',
                    'o    (圈）',
                    '  ▼  (下三角点)',
                    '  ◀  (左三角点)',
                    '  ▶  (右三角点)',
                    '  ┴  (上三叉点)',
                    '  ┬  (下三叉点)',
                    '  ┤  (左三叉点）',
                    '  ├  (右三叉点）',
                    '  ■  (正方形）',
                    '  ⑤  (五角形)',
                    '  ❃  (星形点）',
                    '  ✡  (六边形点1）',
                    '  ✡  (六边形点2）',
                    '  +  (加点号）',
                    '  X  (乘点号）',
                    '  ♦  (实心菱形点）',
                    '  ◊  (瘦菱形点）',
                    '  -  (横线点）']
        )
        # 点渐变
        self.comboBox_4.addItem('None')
        self.comboBox_4.addItems(map(str, range(1, 11)))
        # 标记大小
        self.comboBox_5.addItem('None')
        self.comboBox_5.addItems(map(str, range(1, 11)))
        # 透明度
        self.comboBox_7.addItem('None')
        self.comboBox_7.addItems(map(str, range(0, 101)))
    def getLineColor(self):
        self.color = QColorDialog.getColor().name()
        self.pushButton.setStyleSheet("background-color: {}".format(self.color))

    def getMessage(self):
        # 标题
        self.title = self.lineEdit_3.text()
        # x标签
        self.x_label = self.lineEdit.text()
        # x标签字体大小
        self.x_label_frontsize = self.comboBox_8.currentText()
        # x标签刻度

        # self.x_label_linespace = self.comboBox_10.currentText()

        # y标签
        self.y_label = self.lineEdit_2.text()
        # y标签字体大小
        self.y_label_frontsize = self.comboBox_9.currentText()
        # y标签刻度
        # 命名
        self.name=self.lineEdit_4.text()
        # 自变量
        self.x = self.comboBox.currentText()
        # 因变量
        self.y = self.comboBox_2.currentText()
        # 标记风格
        self.markstyle = self.comboBox_3.currentText()
        # 点渐变
        self.pointschange= self.comboBox_4.currentText()
        # 标记大小
        self.markersize = self.comboBox_5.currentText()
        # 透明度
        self.alpha= self.comboBox_7.currentText()
        #整合数据
        keys0 = ['title', 'x_label', 'x_label_frontsize', 'y_label', 'y_label_frontsize'
                 ]
        values0 = [self.title, self.x_label, self.x_label_frontsize,
                   self.y_label, self.y_label_frontsize]
        self.message0 = {}
        for key, value in zip(keys0, values0):
            self.message0[key] = value
        keys=['name','x','y','linecolor','markstyle','pointschange','markersize','alpha']
        values=[self.name,self.x,self.y,self.color,self.markstyle,self.pointschange,self.markersize,self.alpha]
        self.message = {}
        for key, value in zip(keys, values):
            self.message[key] = value
        self.Datahandle()
        self.tableViewshow()
        self.comboBox_renew()
    def comboBox_renew(self):
        self.lineEdit_4.clear()
        self.comboBox.setCurrentIndex(0)
        self.comboBox_2.setCurrentIndex(0)
        self.comboBox_3.setCurrentIndex(0)
        self.comboBox_4.setCurrentIndex(0)
        self.comboBox_5.setCurrentIndex(0)
        self.comboBox_7.setCurrentIndex(0)
        self.pushButton.setStyleSheet("background-color: {}".format('#000000'))
        self.color = '#000000'
    def Datahandle(self):

        keys = ['name','x','y','linecolor','markstyle','pointschange','markersize','alpha']
        self.Datas.append(self.message)
        Datas = list(map(DataHandle, self.Datas))
        Datas = pd.concat(Datas)
        Datas = Datas.reset_index(range(0, len(Datas))).drop(['index'], axis=1)[keys]
        self.tablewidgetDatas = Datas
    def tableViewshow(self):
        if self.tablewidgetDatas.empty:
            pass
        elif not self.tablewidgetDatas.empty:
            self.pushButton_6.setEnabled(True)
            self.tablewidgetDatasseted = True
            col, row = self.tablewidgetDatas.shape
            self.tableView.model = QStandardItemModel(col, row)
            self.tableView.verticalHeader().setDefaultSectionSize(20)
            self.tableView.setEditTriggers(QAbstractItemView.NoEditTriggers)
            self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)
            self.tableView.model.setHorizontalHeaderLabels(list(self.tablewidgetDatas.columns))
            self.tableView.model.setVerticalHeaderLabels(list(map(str, self.tablewidgetDatas.index)))
            self.tableView.setModel(self.tableView.model)
            # self.tableView.horizontalHeader().setStretchLastSection(True)
            # self.tableView.verticalHeader().setStretchLastSection(True)
            index_x = 0
            for row in self.tablewidgetDatas.iteritems():
                index_x += 1
                index_y = 0
                for s in list(row[1]):
                    index_y += 1
                    newItem = QStandardItem(str(s))
                    self.tableView.model.setItem(index_y - 1, index_x - 1, newItem)
                    if index_x - 1 == 3:
                        newItem.setBackground(QColor(str(s)))

    def getRowIndex_and_Delete(self):

        index = self.tableView.currentIndex()
        print(index.row())
        if index.row() == -1:
            pass

        elif (self.tablewidgetDatas is not None) or (not self.tablewidgetDatas.empty):

            self.tablewidgetDatas.drop([index.row()], inplace=True)
            del self.Datas[index.row()]
            print(self.tablewidgetDatas)
            if self.tablewidgetDatas.empty:
                self.tableView.model.clear()


            else:
                self.tablewidgetDatas.index = list(range(0, len(self.tablewidgetDatas)))
                print(self.tablewidgetDatas)
                self.tableViewshow()

    def Clear(self):
        self.Datas.clear()
        self.tablewidgetDatas.drop(self.tablewidgetDatas.index, inplace=True)
        self.tableView.model.clear()
    def checkMessage(self):
        if None in [self.title, self.x_label, self.y_label]:
            QMessageBox.information(self, '提示', '有未填信息，请仔细核对', QMessageBox.Yes, QMessageBox.Yes)
        elif self.tablewidgetDatasseted == False:
            QMessageBox.information(self, '提示', '有未填信息，请仔细核对', QMessageBox.Yes, QMessageBox.Yes)
        elif self.tablewidgetDatas.empty:
            QMessageBox.information(self, '提示', '有未填信息，请仔细核对', QMessageBox.Yes, QMessageBox.Yes)
        else:

            self.window.emit([self.message0,self.tablewidgetDatas,self.df])
            print(self.message0)
            print(self.tablewidgetDatas)
            self.close()
if __name__ == '__main__':
    df=pd.read_excel(r'C:\Users\Dante\Desktop\111.xlsx',index_col=0)
    app = QApplication(sys.argv)
    win = Dia(df.describe())
    win.show()
    exit(app.exec_())



