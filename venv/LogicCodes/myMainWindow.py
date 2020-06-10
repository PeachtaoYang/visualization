from PyQt5.QtCore import pyqtSignal
from UI.myMainWindow import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow,QApplication
from FileOperator.FileReadingThread import File_read_thread
from FileOperator.FileSavingThread import File_Save_as_csv,File_Save_as_excel
from PyQt5.QtWidgets import QFileDialog,QMessageBox,QInputDialog,QTableView,QScrollArea,QAbstractItemView,QProgressDialog
from qtpandas.models.DataFrameModel import DataFrameModel
from PyQt5.QtGui import QStandardItemModel,QStandardItem,QIcon
from Matplotlib._plot import *
from Selection._Selection import *
from pandas import DataFrame
import sys
from Selection.Selection_infoHandle import *
from pandas import merge
from FillnaWith._FillNaWith import myFillnaWith
from ScientificComputation.Scientific_add import myAdd
from ScientificComputation.Scientific_radd import myrAdd
from ScientificComputation.Scientific_sub import mySub
from ScientificComputation.Scientific_rsub import myrSub
from ScientificComputation.Scientific_div import myDiv
from ScientificComputation.Scientific_rdiv import myrDiv
from ScientificComputation.Scientific_floordiv import myFloordiv
from ScientificComputation.Scientific_rfloordiv import myrFloordiv
from ScientificComputation.Scientific_pow import myPow
from ScientificComputation.Scientific_rpow import myrPow
from ScientificComputation.Scientific_corr import myCorr
from ScientificComputation.CorrShow import Corr_show
from ScientificComputation.CovShow import Cov_show
from PyQt5.QtCore import QBasicTimer
from ForcedTypeConversion.TypeConversion import myTypeConversion
from PyQt5.QtCore import Qt
import numpy as np
from pandas import to_datetime
from Matplotlib.PlotWidget import *
from Matplotlib.ScatterWidget import *
from Matplotlib._scatter import *
from Matplotlib._pie import *
from Matplotlib.PieWidget import *
from Matplotlib._bar import *
from Matplotlib.BarWidget import *
from Matplotlib._barh import *
from Matplotlib.BarhWidget import *
from Matplotlib._hist import *
from Matplotlib.HistWidget import *
from PyQt5.QtWidgets import QApplication,QLabel,QWidget,QMainWindow
from PyQt5.QtCore import Qt,QTimer,pyqtSignal
from PyQt5.QtGui import QMovie
from UI.myMainWindow import Ui_MainWindow
info={
    'int (整数)':np.int,
    'float  (小数)':np.float,
    'string  (字符串)':np.str
}

def Numbertic(data):
    try:
        data=float(data)
    finally:
        return data
class myMainWindow(QMainWindow,Ui_MainWindow,QScrollArea):

    def __init__(self):
        super().__init__()
        self.setAcceptDrops(True)
        self.setupUi(self)

        '''
        以下是各按键与各函数的绑定
        '''
        #数据初始化
        self.orignal_df=None
        self.tempDF= None
        #异常模块窗口初始化信息
        self.modelseted=False
        #数据摘要窗口初始化信息
        self.tableViewSeted=False
        self.setFixedSize(1068, 737)
        self.setWindowTitle('Data Visualization')
        self.setWindowIcon(QIcon(r'Z:\Data_Visualization\venv\qrc\icons\icon.png'))

        #self.progressBar.hide()
        #openfile键与获取文件信息并展示函数的绑定
        self.actionOpen_file.triggered.connect(self.getFile_toShow)
        #save as csv file键与函数save as csv 文件的绑定
        self.actionas_a_Csv_File.triggered.connect(self.File_save_as_csv)
        #save as excel file 与 函数save as execl文件的绑定
        self.actionas_a_Excel_file.triggered.connect(self.File_save_as_excel)
        #退出键
        self.actionExit.triggered.connect(self.close)
        #删除所有问题行操作键与相关函数的绑定
        self.actionDelete_problematic_rows.triggered.connect(self.Quick_Operation_delete_rows)
        #删除所有问题列操作键与相关函数的绑定
        self.actionDelete_problematic_columns.triggered.connect(self.Quick_Operation_delete_cols)
        #删除重复值操作键与相关函数的绑定
        self.actionDelete_duplicate_values.triggered.connect(self.Quick_Operation_delete_duplicate_values)
        #刷新所有窗口数据操作键与其相关函数的绑定
        self.actionUpdating_all_the_Windows.triggered.connect(self.Updating_all_windows)
        #填充空缺值操作
        self.actionFill_problematic_columns_with.triggered.connect(self.FillnaWith)
        #强制类型转换与相关ui界面的绑定
        self.actionForced_type_Conversion.triggered.connect(self.Forced_type_conversion)
        #筛选操作的绑定
        self.actionread_only.triggered.connect(self.Selection_read_only)
        #筛选操作并替换原来的数据
        self.actioninplace.triggered.connect(self.Selection_inplace)
        #科学计算add与相关ui界面的绑定
        self.actionadd.triggered.connect(self.Scientific_add)
        #科学计算radd与相关ui界面的绑定
        self.actionradd.triggered.connect(self.Scientific_radd)
        #科学计算sub与相关ui界面的绑定
        self.actionsub.triggered.connect(self.Scientific_sub)
        #科学计算rsub与相关ui界面的绑定
        self.actionrsub.triggered.connect(self.Scientific_rsub)
        #科学计算div与相关ui界面的绑定
        self.actiondiv.triggered.connect(self.Scientific_div)
        #科学计算rdiv与相关ui界面的绑定
        self.actionrdiv.triggered.connect(self.Scientific_rdiv)
        #科学计算floordiv与相关ui界面的绑定
        self.actionfloordiv.triggered.connect(self.Scientific_floordiv)
        #科学计算rfloordiv与相关ui界面的绑定
        self.actionrfloordiv.triggered.connect(self.Scientific_rfloordiv)
        #科学计算pow与相关ui界面的绑定
        self.actionpow.triggered.connect(self.Scientific_pow)
        #科学计算rpow与相关ui界面的绑定
        self.actionrpow.triggered.connect(self.Scientific_rpow)
        #相关系数计算
        self.actioncorr.triggered.connect(self.Scientific_corr)
        #cov
        self.actioncov.triggered.connect(self.Scientific_cov)
        #绘画函数plot与相关函数绑定
        self.actionplot.triggered.connect(self.Matplotlib_plot)
        #散点图
        self.actionscatter.triggered.connect(self.Matplotlib_scatter)
        #饼图
        self.actionpie.triggered.connect(self.Matplotlib_pie)
        #柱状图
        self.actionbar.triggered.connect(self.Matplotlib_bar)
        #水平柱状图
        self.actionbarh.triggered.connect(self.Matplotlib_barh)
        #直方图
        self.actionhist.triggered.connect(self.Matplotlib_hist)

        #self.orignal_df[i[0]] = to_datetime(self.orignal_df[i[0]], errors='ignore', format=self.formatStr)

    def Forced_type_conversion(self):
        if self.orignal_df is not None:
            self.ui=myTypeConversion(self.orignal_df)
            self.ui.show()
            self.ui.okButtonPressed.connect(self.Forced_type_conversion_recive)


    def Forced_type_conversion_recive(self,data):

        #print(data)
        try:
            for i in data:
                self.orignal_df[i[0]] = self.orignal_df[i[0]].astype(info[i[1]], errors='ignore')
            self.Updating_all_windows()

        except :
            QMessageBox.information(self,'提示','类型转换不支持',QMessageBox.Yes)
        #print('end')
        #print(self.orignal_df.dtypes)



    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()
    def closeEvent(self, *args, **kwargs):
        try:
            self.ui.close()
        except :
            pass
        finally:
            self.close()
    def dropEvent(self, event):
        filename=event.mimeData().urls()[0].path()[1:]
        #print(filename)
        if filename[-4:]=='.csv' or filename[-4:]=='xlsx' or filename[-4:]=='.xls':
            self.thread0 = File_read_thread(filename)
        # 线程0文件读取完毕发送信号与receive以及viewFile函数绑定
            self.thread0.fileReadDone[type(DataFrame())].connect(self.receive)
            self.thread0.fileReadDone[type(DataFrame())].connect(self.viewFile)
            self.thread0.start()
            self.timer = QBasicTimer()
            self.step = 0
            self.progressBar=QProgressDialog(self)
            self.progressBar.setCancelButton(None)
            #self.progressBar.setWindowFlags(Qt.WindowCloseButtonHint)
            self.progressBar.setWindowModality(Qt.WindowModal)
            self.progressBar.setWindowTitle('文件读取中...')
            self.progressBar.setLabelText('解析进行中，请稍候...')
            self.progressBar.setRange(0,100 )
            self.progressBar.show()
            if self.timer.isActive():
                self.timer.stop()
                self.step = 0
            else:
                self.step = 0
                self.timer.start(100, self)

        else:
            QMessageBox.warning(self,'warning!','文件格式不支持',QMessageBox.Yes,QMessageBox.Yes)
    def receive(self,df):
        '''
        接收线程发送的文件信息
        :return:
        '''
        #self.orignal_df = self.thread0.df
        self.orignal_df = df
        self.progressBar.setValue(300)
        self.timer.stop()
        self.progressBar.close()


    def Temp_data_init(self):
        self.tempDF=None
    def data_recovery(self):
        if self.tempDF is not None:
            self.orignal_df=self.tempDF
            self.tempDF=None
            self.Updating_all_windows()
    def Fillna_data_recive(self,data):
        if self.tempDF is None:
            self.tempDF=self.orignal_df.copy()
        for i in data:
            if i[1]=='Null':
                self.orignal_df[i[0]].fillna(Numbertic(i[2]),inplace=True)
                self.Updating_all_windows()
            else:
                if i[1]=='mean':
                    self.orignal_df[i[0]].fillna(self.orignal_df[i[0]].mean(), inplace=True)
                    self.Updating_all_windows()
                elif i[1]=='median':
                    self.orignal_df[i[0]].fillna(self.orignal_df[i[0]].median(), inplace=True)
                    self.Updating_all_windows()
                elif i[1]=='max':
                    self.orignal_df[i[0]].fillna(self.orignal_df[i[0]].max(), inplace=True)
                    self.Updating_all_windows()
                elif i[1]=='min':
                    self.orignal_df[i[0]].fillna(self.orignal_df[i[0]].min(), inplace=True)
                    self.Updating_all_windows()

    def Scientific_add(self):
        if self.orignal_df is not None:
            self.ui=myAdd(self.orignal_df)
            self.ui.show()
            self.ui.okButtonPressed.connect(self.Scientific_data_add_recive)
            self.ui.applyButtonPressed.connect(self.Temp_data_init)
            self.ui.cancalButtonPressed.connect(self.data_recovery)
    def Scientific_data_add_recive(self,data):
        #print(data)
        if self.tempDF is None:
            self.tempDF=self.orignal_df.copy()
        for i in data:
            self.orignal_df[i[0]]=self.orignal_df[i[0]].add(Numbertic(i[1]))
        self.Updating_all_windows()
    def Scientific_radd(self):
        if self.orignal_df is not None:
            self.ui = myrAdd(self.orignal_df)
            self.ui.show()
            self.ui.okButtonPressed.connect(self.Scientific_data_radd_recive)
            self.ui.applyButtonPressed.connect(self.Temp_data_init)
            self.ui.cancalButtonPressed.connect(self.data_recovery)
    def Scientific_data_radd_recive(self,data):
        #print(data)
        if self.tempDF is None:
            self.tempDF=self.orignal_df.copy()
        for i in data:
            self.orignal_df[i[0]]=self.orignal_df[i[0]].radd(Numbertic(i[1]))
        self.Updating_all_windows()
    def Scientific_sub(self):
        if self.orignal_df is not None:
            self.ui = mySub(self.orignal_df)
            self.ui.show()
            self.ui.okButtonPressed.connect(self.Scientific_data_sub_recive)
            self.ui.applyButtonPressed.connect(self.Temp_data_init)
            self.ui.cancalButtonPressed.connect(self.data_recovery)
    def Scientific_data_sub_recive(self,data):
        #print(data)
        if self.tempDF is None:
            self.tempDF=self.orignal_df.copy()
        for i in data:
            self.orignal_df[i[0]]=self.orignal_df[i[0]].sub(Numbertic(i[1]))
        self.Updating_all_windows()
    def Scientific_rsub(self):
        if self.orignal_df is not None:
            self.ui = myrSub(self.orignal_df)
            self.ui.show()
            self.ui.okButtonPressed.connect(self.Scientific_data_rsub_recive)
            self.ui.applyButtonPressed.connect(self.Temp_data_init)
            self.ui.cancalButtonPressed.connect(self.data_recovery)
    def Scientific_data_rsub_recive(self,data):
        #print(data)
        if self.tempDF is None:
            self.tempDF=self.orignal_df.copy()
        for i in data:
            self.orignal_df[i[0]]=self.orignal_df[i[0]].rsub(Numbertic(i[1]))
        self.Updating_all_windows()
    def Scientific_div(self):
        if self.orignal_df is not None:
            self.ui = myDiv(self.orignal_df)
            self.ui.show()
            self.ui.okButtonPressed.connect(self.Scientific_data_div_recive)
            self.ui.applyButtonPressed.connect(self.Temp_data_init)
            self.ui.cancalButtonPressed.connect(self.data_recovery)

    def Scientific_data_div_recive(self,data):
        #print(data)
        if self.tempDF is None:
            self.tempDF=self.orignal_df.copy()
        for i in data:
            self.orignal_df[i[0]]=self.orignal_df[i[0]].div(Numbertic(i[1]))
        self.Updating_all_windows()
    def Scientific_rdiv(self):
        if self.orignal_df is not None:
            self.ui = myrDiv(self.orignal_df)
            self.ui.show()
            self.ui.okButtonPressed.connect(self.Scientific_data_rdiv_recive)
            self.ui.applyButtonPressed.connect(self.Temp_data_init)
            self.ui.cancalButtonPressed.connect(self.data_recovery)

    def Scientific_data_rdiv_recive(self,data):
        #print(data)
        if self.tempDF is None:
            self.tempDF=self.orignal_df.copy()
        for i in data:
            self.orignal_df[i[0]]=self.orignal_df[i[0]].rdiv(Numbertic(i[1]))
        self.Updating_all_windows()
    def Scientific_floordiv(self):
        if self.orignal_df is not None:
            self.ui = myFloordiv(self.orignal_df)
            self.ui.show()
            self.ui.okButtonPressed.connect(self.Scientific_data_floordiv_recive)
            self.ui.applyButtonPressed.connect(self.Temp_data_init)
            self.ui.cancalButtonPressed.connect(self.data_recovery)

    def Scientific_data_floordiv_recive(self,data):
        #print(data)
        if self.tempDF is None:
            self.tempDF=self.orignal_df.copy()
        for i in data:
            self.orignal_df[i[0]]=self.orignal_df[i[0]].floordiv(Numbertic(i[1]))
        self.Updating_all_windows()
    def Scientific_rfloordiv(self):
        if self.orignal_df is not None:
            self.ui = myrFloordiv(self.orignal_df)
            self.ui.show()
            self.ui.okButtonPressed.connect(self.Scientific_data_rfloordiv_recive)
            self.ui.applyButtonPressed.connect(self.Temp_data_init)
            self.ui.cancalButtonPressed.connect(self.data_recovery)

    def Scientific_data_rfloordiv_recive(self,data):
        #print(data)
        if self.tempDF is None:
            self.tempDF=self.orignal_df.copy()
        for i in data:
            self.orignal_df[i[0]]=self.orignal_df[i[0]].rfloordiv(Numbertic(i[1]))
        self.Updating_all_windows()
    def Scientific_pow(self):
        if self.orignal_df is not None:
            self.ui = myPow(self.orignal_df)
            self.ui.show()
            self.ui.okButtonPressed.connect(self.Scientific_data_pow_recive)
            self.ui.applyButtonPressed.connect(self.Temp_data_init)
            self.ui.cancalButtonPressed.connect(self.data_recovery)

    def Scientific_data_pow_recive(self,data):
        #print(data)
        if self.tempDF is None:
            self.tempDF=self.orignal_df.copy()
        for i in data:
            self.orignal_df[i[0]]=self.orignal_df[i[0]].pow(Numbertic(i[1]))
        self.Updating_all_windows()
    def Scientific_rpow(self):
        if self.orignal_df is not None:
            self.ui = myrPow(self.orignal_df)
            self.ui.show()
            self.ui.okButtonPressed.connect(self.Scientific_data_rpow_recive)
            self.ui.applyButtonPressed.connect(self.Temp_data_init)
            self.ui.cancalButtonPressed.connect(self.data_recovery)

    def Scientific_data_rpow_recive(self,data):
        #print(data)
        if self.tempDF is None:
            self.tempDF=self.orignal_df.copy()
        for i in data:
            self.orignal_df[i[0]]=self.orignal_df[i[0]].rpow(Numbertic(i[1]))
        self.Updating_all_windows()
    def Scientific_data_corr_recive(self,data):
        #print(data)
        result=self.orignal_df.corr(data[0])
        self.ui=Corr_show(result)
        self.ui.show()
    def Scientific_corr(self):
        if self.orignal_df is not None:
            self.ui=myCorr()
            self.ui.show()
            self.ui.window.connect(self.Scientific_data_corr_recive)
    def Scientific_cov(self):
        if self.orignal_df is not None:
            result=self.orignal_df.cov()
            self.ui=Cov_show(result)
            self.ui.show()
    def Selection_data_recive(self,data):
        '''

        :param data: 返回操作信息
        :return: None
        '''
        #判空操作，若非空则执行
        #print(data)

        tempData=[]#各逻辑操作返回的数据集
        for i in data:
            tempData.append(sih(self.orignal_df,i))
        #对数据集进行取交集操作
        #print(tempData)
        try:
            if type(str()) in list(map(type,tempData)):
                ok=QMessageBox.warning(self.ui,'waring','参数错误,\n请检查输入的参数。',QMessageBox.Yes|QMessageBox.Yes,QMessageBox.No)
                if ok:
                    self.ui.settableWidget()
            else:
                if len(tempData) == 1 and tempData[0].empty:
                    QMessageBox.information(self, '提示', '数据集为空', QMessageBox.Yes, QMessageBox.Yes)

                elif len(tempData) == 1 and not tempData[0].empty:
                    if type(self.tempDF)is  type(None):
                        self.tempDF=self.orignal_df
                        self.orignal_df = tempData[0]
                        self.Updating_all_windows()
                    else:
                        self.orignal_df = tempData[0]
                        self.Updating_all_windows()

                else:
                    if type(self.tempDF) is type(None):
                        self.tempDF = self.orignal_df
                    if True in list(map(lambda x:x.empty,tempData)):
                        #print(list(map(lambda x:x.empty,tempData)))
                        QMessageBox.information(self, '提示', '数据集为空', QMessageBox.Yes, QMessageBox.Yes)
                    else:
                        for i in range(len(tempData) - 1):
                            self.orignal_df = merge(tempData[i], tempData[i + 1], how='inner')
                        if self.orignal_df.empty:
                            QMessageBox.information(self, '提示', '数据集为空', QMessageBox.Yes, QMessageBox.Yes)
                        else:
                            self.Updating_all_windows()


        except Exception as e :
            QMessageBox.warning(self.ui, 'waring', str(e.args), QMessageBox.Yes, QMessageBox.Yes)
    def Selection_inplace(self):
        if self.orignal_df is not None:
            self.ui=mySelection(self.orignal_df)
            self.ui.show()
            self.ui.SelectionSignal[type(list())].connect(self.Selection_data_recive)
    def FillnaWith(self):
        if self.orignal_df is None:
            QMessageBox.information(self, '提示', '未读取数据', QMessageBox.Yes, QMessageBox.Yes)

        else:
            self.ui=myFillnaWith(self.orignal_df)
            if len(self.ui.columns)==0:
                QMessageBox.information(self,'提示','数据不存在异常值',QMessageBox.Yes,QMessageBox.Yes)
                self.ui.close()
            else:
                self.ui.show()
                self.ui.FillNaSignal.connect(self.Fillna_data_recive)
                self.ui.CancalButtonPressed.connect(self.data_recovery)
                self.ui.ExitButtonPressed.connect(self.Temp_data_init)
    def Selection_read_only(self):
        if self.orignal_df is not None:
            self.ui=mySelection(self.orignal_df)
            self.ui.show()
            self.ui.SelectionSignal[type(list())].connect(self.Selection_data_recive)
            self.ui.closeButtonPressed.connect(self.data_recovery)
    def timerEvent(self, *args, **kwargs):
        self.progressBar.setValue(self.step)
        if self.step>=100:
            self.timer.stop()
            self.step=0
            return
        elif self.step<99:
            self.step+=1



    def  getFile_toShow(self):


        '''
        获取文件信息并显示
        :return:
        '''

        FileName=QFileDialog.getOpenFileName(filter="Data file(*.csv *.xlsx *.xls)")
        #print(FileName)
        #print(FileName[0])
        if FileName[0]!='':
            self.thread0=File_read_thread(FileName[0])
            #线程0文件读取完毕发送信号与receive以及viewFile函数绑定
            self.thread0.fileReadDone[type(DataFrame())].connect(self.receive)
            self.thread0.fileReadDone[type(DataFrame())].connect(self.viewFile)
            self.thread0.start()
            self.timer = QBasicTimer()
            self.step = 0
            self.progressBar=QProgressDialog(self)
            self.progressBar.setCancelButton(None)
            #self.progressBar.setWindowFlags(Qt.WindowCloseButtonHint)
            self.progressBar.setWindowModality(Qt.WindowModal)
            self.progressBar.setWindowTitle('文件读取中...')
            self.progressBar.setLabelText('解析进行中，请稍候...')
            self.progressBar.setRange(0,100)
            self.progressBar.show()
            if self.timer.isActive():
                self.timer.stop()
                self.step = 0
            else:
                self.step = 0
                self.timer.start(100, self)

    def viewFile(self):
        '''
        展示文件的函数
        :return:
        '''
        if self.orignal_df.empty:
            QMessageBox.warning(self, '警告', '文件为空文件！', QMessageBox.Yes, QMessageBox.Yes)
        self.ErrorDataview_show()
        self.tableView_show()
        self.label_2.close()
        self.widget = self.pandastablewidget
        self.model = DataFrameModel()
        self.widget.setViewModel(self.model)
        self.model.setDataFrame(self.orignal_df)
    def File_save_as_csv(self):

        '''
        文件保存为csv文件
        :return:
        '''
        if self.orignal_df is None:
            QMessageBox.information(self,'提示','未读取文件',QMessageBox.Yes,QMessageBox.Yes)
        else:
            FileName=QFileDialog.getSaveFileUrl(filter="Data file(*.csv )")
            print(str(FileName[0].toString())[8:])
            if str(FileName[0].toString())!='':
                try :
                    self.thread2 = File_Save_as_csv(self.orignal_df, str(FileName[0].toString())[8:])
                    self.thread2.start()
                except Exception as e:
                    QMessageBox.information(self,'提示','文件保存失败！',QMessageBox.Yes,QMessageBox.Yes)
            #text, ok = QInputDialog.getText(self, 'save as csv', '请输入文件名称')
            #if ok:
                #FileName = text + '.csv'
                #self.thread2 = File_Save_as_csv(self.orignal_df, FileName)
                #self.thread2.start()
    def File_save_as_excel(self):
        '''
        文件保存为excel文件
        :return:
        '''
        if self.orignal_df is None:
            QMessageBox.information(self,'提示','未读取文件',QMessageBox.Yes,QMessageBox.Yes)
        else:
            FileName = QFileDialog.getSaveFileUrl(filter="Data file(*.xls *xlsx)")
            #print(str(FileName[0].toString())[8:])
            if str(FileName[0].toString()) != '':
                try:
                    self.thread2 = File_Save_as_excel(self.orignal_df, str(FileName[0].toString())[8:])
                    self.thread2.start()
                except Exception as e:
                    QMessageBox.information(self, '提示', '文件保存失败！', QMessageBox.Yes, QMessageBox.Yes)
    def tableView_show(self):
        '''
        数据摘要显示
        :return:
        '''
        if not self.orignal_df.empty:
            self.tableViewSeted=True
            col,row=self.orignal_df.describe().shape
            self.tableView.model=QStandardItemModel(col,row)
            self.tableView.model.setHorizontalHeaderLabels(list(self.orignal_df.describe().columns))
            self.tableView.model.setVerticalHeaderLabels(list(self.orignal_df.describe().index))
            self.tableView.setModel(self.tableView.model)
            self.tableView.setEditTriggers(QAbstractItemView.NoEditTriggers)
            self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)
            #self.tableView.horizontalHeader().setStretchLastSection(True)
            #self.tableView.verticalHeader().setStretchLastSection(True)
            index_x=0
            for row in self.orignal_df.describe().iteritems():
                index_x+=1
                index_y=0
                for s in list(row[1]):
                    index_y+=1
                    newItem=QStandardItem(str(s))
                    self.tableView.model.setItem(index_y-1,index_x-1,newItem)
        elif self.orignal_df.empty and self.tableViewSeted==True:
            self.tableView.model.clear()
    def ErrorDataview_show(self):

        if not self.orignal_df[self.orignal_df.isnull().values == True].empty and not self.orignal_df.empty:
            self.modelseted = True
            data = self.orignal_df[self.orignal_df.isnull().values == True]
            col, row = data.shape
            self.tableView_2.model = QStandardItemModel(col, row)
            self.tableView_2.model.setHorizontalHeaderLabels(list(data.columns))
            self.tableView_2.model.setVerticalHeaderLabels(list((map(str,data.index))))
            self.tableView_2.setModel(self.tableView_2.model)
            self.tableView_2.setEditTriggers(QAbstractItemView.NoEditTriggers)
            self.tableView_2.setSelectionBehavior(QAbstractItemView.SelectRows)
            #self.tableView_2.horizontalHeader().setStretchLastSection(True)
            #self.tableView_2.verticalHeader().setStretchLastSection(True)

            index_x = 0
            for row in data.iteritems():
                index_x += 1
                index_y = 0
                for s in list(row[1]):
                    index_y += 1
                    newItem = QStandardItem(str(s))
                    self.tableView_2.model.setItem(index_y - 1, index_x - 1, newItem)
        elif  self.orignal_df.empty and self.modelseted==True :
            self.tableView_2.model.clear()
        elif  self.orignal_df[self.orignal_df.isnull().values == True].empty and not self.orignal_df.empty :
            if self.modelseted==True :
                self.tableView_2.model.clear()
            else:
                pass
    def Quick_Operation_delete_rows(self):
        if self.orignal_df is None:
            QMessageBox.information(self, '提示', '未读取数据', QMessageBox.Yes, QMessageBox.Yes)
        else:
            self.orignal_df=self.orignal_df.dropna()
            self.Updating_all_windows()
    def Quick_Operation_delete_cols(self):
        if self.orignal_df is None:
            QMessageBox.information(self, '提示', '未读取数据', QMessageBox.Yes, QMessageBox.Yes)
        else:
            self.orignal_df=self.orignal_df.dropna(axis=1)
            self.Updating_all_windows()
    def Quick_Operation_delete_duplicate_values(self):
        if self.orignal_df is None:
            QMessageBox.information(self, '提示', '未读取数据', QMessageBox.Yes, QMessageBox.Yes)
        else:
            self.orignal_df=self.orignal_df.drop_duplicates()
            self.Updating_all_windows()
    def Updating_all_windows(self):
        if self.orignal_df is None:
            QMessageBox.information(self, '提示', '未读取数据', QMessageBox.Yes, QMessageBox.Yes)
        else:
            self.ErrorDataview_show()
            self.tableView_show()
            self.widget = self.pandastablewidget
            self.model = DataFrameModel()
            self.widget.setViewModel(self.model)
            self.model.setDataFrame(self.orignal_df)
    def Matplotlib_plot_show(self,data):
        self.ui=QmyMainWindow(data[0],data[1],data[2])
        self.ui.show()

    def Matplotlib_plot(self):
        if self.orignal_df is not None:
            self.ui=Dia(self.orignal_df[self.orignal_df.describe().columns])
            self.ui.show()
            self.ui.window.connect(self.Matplotlib_plot_show)
    def Matplotlib_scatter_show(self,data):
        self.ui=QmyMainWindow1(data[0],data[1],data[2])
        self.ui.show()
    def Matplotlib_scatter(self):
        if self.orignal_df is not None:
            self.ui=Dia1(self.orignal_df[self.orignal_df.describe().columns])
            self.ui.show()
            self.ui.window.connect(self.Matplotlib_scatter_show)
    def Matplotlib_pie_show(self,data):
        #print(data)
        self.ui=QmyMainWindow2(data[0],data[1],data[2],data[3],data[4],self.orignal_df)
        self.ui.show()
    def Matplotlib_pie(self):
        if self.orignal_df is not None:
            self.ui=Dia2(self.orignal_df)
            self.ui.show()
            self.ui.window.connect(self.Matplotlib_pie_show)
    def Matplotlib_bar_show(self,data):
        #print(data)
        self.ui = QmyMainWindow3(data, self.orignal_df)
        self.ui.show()
    def Matplotlib_bar(self):
        if self.orignal_df is not None:
            self.ui=Dia3(self.orignal_df)
            self.ui.show()
            self.ui.window.connect(self.Matplotlib_bar_show)
    def Matplotlib_barh_show(self,data):
        #print(data)
        if self.orignal_df is not None:
            self.ui = QmyMainWindow4(data, self.orignal_df)
            self.ui.show()
    def Matplotlib_barh(self):
        if self.orignal_df is not None:
            self.ui=Dia4(self.orignal_df)
            self.ui.show()
            self.ui.window.connect(self.Matplotlib_barh_show)
    def Matplotlib_hist_show(self,data):
        #print(data)
        if self.orignal_df is not None:
            self.ui = QmyMainWindow5(data, self.orignal_df)
            self.ui.show()
    def Matplotlib_hist(self):
        if self.orignal_df is not None:
            self.ui=Dia5(self.orignal_df)
            self.ui.show()
            self.ui.window.connect(self.Matplotlib_hist_show)
'''
启动加载gif动画

'''

#import qrc.icons_rc

class LoadingGif(QWidget):
    closed=pyqtSignal(int)
    def __init__(self):
        super().__init__()
        self.label=QLabel("",self)
        self.setFixedSize(520,320)
        self.setWindowFlags(Qt.Dialog | Qt.FramelessWindowHint)
        self.movie=QMovie('..\qrc\icons\logo_done.gif')
        self.label.setMovie(self.movie)
        self.movie.start()
        self.timer=QTimer(self)
        self.timer.timeout.connect(self.Begin)
        self.timer.start(3500)
    def Begin(self):

        self.close()
        self.closed.emit(1)






'''
测试
'''




if __name__=='__main__':
    app=QApplication(sys.argv)
    form=form=LoadingGif()
    form.show()
    win=myMainWindow()
    win.setStyleSheet("#MainWindow{background-color: #E8E8E8}")
    form.closed.connect(win.show)

    sys.exit(app.exec_())
