from PyQt5.QtCore import Qt
import matplotlib as mpl
import sys
import numpy as np
from PyQt5.QtWidgets import QApplication,QMainWindow,QMessageBox
from matplotlib.backends.backend_qt5agg import (FigureCanvas,NavigationToolbar2QT
                                                as NavigationToolbar)
def Numtic(data):
    return float(data)
class QmyMainWindow5(QMainWindow):
    def __init__(self,data,df):
        super().__init__()
        self.setWindowTitle('频率分布直方图绘制')
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
        plt.set_xlabel(self.data[1])
        plt.set_ylabel(self.data[2])
        bins=np.arange(Numtic(self.data[4]),Numtic(self.data[5]),Numtic(self.data[6]))
        plt.hist(self.df[self.data[3]],bins=bins,color=self.data[7])







