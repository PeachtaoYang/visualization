from PyQt5.QtCore import Qt
import matplotlib as mpl
import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QMessageBox
from matplotlib.backends.backend_qt5agg import (FigureCanvas,NavigationToolbar2QT
                                                as NavigationToolbar)
class QmyMainWindow3(QMainWindow):
    def __init__(self,data,df):
        super().__init__()
        self.setWindowTitle('柱状图绘制')
        mpl.rcParams['font.sans-serif'] = ['KaiTi', 'SimHei']
        mpl.rcParams['font.size'] = 12
        mpl.rcParams['axes.unicode_minus'] = False
        self.data=data
        self.df=df
        self.__iniFigure()
        self.__drawFigure()
    def __iniFigure(self):
        self.__fig = mpl.figure.Figure(figsize=(10, 12))
        self.__fig.suptitle(self.data[0])
        figCanvas = FigureCanvas(self.__fig)
        naviToolbar = NavigationToolbar(figCanvas, self)
        self.addToolBar(naviToolbar)
        self.setCentralWidget(figCanvas)

    def __drawFigure(self):
        plt = self.__fig.add_subplot(111)
        plt.set_xlabel(self.data[5])
        plt.set_ylabel(self.data[6])
        if self.data[2]=='None':
            x=self.df[self.data[1]].value_counts().index
            y=self.df[self.data[1]].value_counts().values
            plt.bar(x,y,color=self.data[4])

            for tick in plt.get_xticklabels():
                tick.set_rotation(90)
            for a ,b in zip(x,y):
                plt.text(a,b,'%.f'%b,ha='center',fontsize=10)
        elif self.data[2]=='数值分类':
            try:
                datas = []
                legends = []
                if '，' in self.data[3]:
                    tex = list(map(float, self.data[3].split('，')))
                else:
                    tex = list(map(float, self.data[3].split(',')))

                for each in range(len(tex) - 1):
                    datas.append(
                        len(self.df[(self.df[self.data[1]] >= tex[each]) & (self.df[self.data[1]] < tex[each + 1])]))
                    legends.append(str(tex[each]) + '~' + str(tex[each + 1]))
                plt.bar(legends.copy(), datas.copy(), color=self.data[4])
                for tick in plt.get_xticklabels():
                    tick.set_rotation(90)
                for a, b in zip(legends, datas):
                    plt.text(a, b, '%.f' % b, ha='center', fontsize=10)
                legends.clear()
                datas.clear()
            except Exception as e:
                QMessageBox.information(self,'提示',str(e.args),QMessageBox.Yes,QMessageBox.Yes)
        elif self.data[2]=='非数值分类':
            try:
                datas = []
                legends = []
                if '，' in self.data[3]:
                    tex = self.data[3].split('，')
                else:
                    tex = self.data[3].split(',')
                # print(text)
                for each in tex:
                    datas.append(len(self.df[(self.df[self.data[1]]) == each]))
                    legends.append(each)
                plt.bar(legends.copy(), datas.copy(), color=self.data[4])
                for tick in plt.get_xticklabels():
                    tick.set_rotation(90)
                for a, b in zip(legends, datas):
                    plt.text(a, b, '%.f' % b, ha='center', fontsize=10)
                legends.clear()
                datas.clear()
            except Exception as e:
                QMessageBox.information(self,'提示',str(e.args),QMessageBox.Yes,QMessageBox.Yes)






