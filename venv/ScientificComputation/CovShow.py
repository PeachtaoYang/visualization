from PyQt5.QtWidgets import QDialog,QAbstractItemView
from UI.Corr_show import Ui_Dialog
from PyQt5.QtGui import QStandardItemModel,QStandardItem
class Cov_show(QDialog,Ui_Dialog):
    def __init__(self,df):
        super().__init__()
        self.setupUi(self)
        self.df=df
        self.setTableView()
        self.pushButton.pressed.connect(self.close)
        self.pushButton_2.pressed.connect(self.close)
        self.setWindowTitle('协方差分析')
    def setTableView(self):
        col,row =len(self.df.index),len(self.df.columns)
        self.tableView.model = QStandardItemModel(col, row)
        self.tableView.model.setHorizontalHeaderLabels(list(self.df.columns))
        self.tableView.model.setVerticalHeaderLabels(list(self.df.index))
        self.tableView.setModel(self.tableView.model)
        self.tableView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        index_x = 0
        for row in self.df.iteritems():
            index_x += 1
            index_y = 0
            for s in list(row[1]):
                index_y += 1
                newItem = QStandardItem(str(s))
                self.tableView.model.setItem(index_y - 1, index_x - 1, newItem)