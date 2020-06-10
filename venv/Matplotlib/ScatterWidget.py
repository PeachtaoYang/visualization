from PyQt5.QtCore import Qt
import matplotlib as mpl
import sys
import numpy as np
from PyQt5.QtWidgets import QApplication,QMainWindow
from matplotlib.backends.backend_qt5agg import (FigureCanvas,NavigationToolbar2QT
                                                as NavigationToolbar)
import pandas as pd
choices=[   '  ●  (圆点)',
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
                    '  -  (横线点）',
                     'None']
means=['.',',','o','^','v','<','>','2','1','3','4','s','p','*','H','h','+','x','D','d','.',None]
Choices_means={}
for key,value in zip(choices,means):
    Choices_means[key]=value
class QmyMainWindow1(QMainWindow):
    def __init__(self,message=None,info=None,df=None):
        super().__init__()
        self.setWindowTitle('散点图绘制')
        mpl.rcParams['font.sans-serif']=['KaiTi','SimHei']
        mpl.rcParams['font.size']=12
        mpl.rcParams['axes.unicode_minus']=False

        self.message=message
        self.info=info
        self.df=df
        self.unpackgeInfo()
        self.__iniFigure()
        self.__drawFigure()

    def unpackgeInfo(self):
        self.title=self.message['title']
        self.x_lable=self.message['x_label']
        self.x_label_frontsize=self.message['x_label_frontsize']

        self.y_lable=self.message['y_label']
        self.y_label_frontsize=self.message['y_label_frontsize']

        self.lineInfo=self.info.values.tolist()

    def __iniFigure(self):
        self.__fig = mpl.figure.Figure(figsize=(16, 10))
        self.__fig.suptitle(self.title)
        figCanvas = FigureCanvas(self.__fig)
        naviToolbar = NavigationToolbar(figCanvas, self)
        self.addToolBar(naviToolbar)
        self.setCentralWidget(figCanvas)

    def __drawFigure(self):
        legends=[]
        plt = self.__fig.add_subplot(111)
        if self.x_label_frontsize =='None' :
            plt.set_xlabel(self.x_lable)
        elif self.x_label_frontsize != 'None' :
            plt.set_xlabel(self.x_lable,fontsize=int(self.x_label_frontsize))
        if self.y_label_frontsize =='None' :
            plt.set_ylabel(self.y_lable)
        elif self.y_label_frontsize != 'None':
            plt.set_ylabel(self.y_lable,fontsize=int(self.y_label_frontsize))
        for i in self.lineInfo:
            if i[4]=='None':
                i[4]=None
            if i[5]=='None':
                i[5]=None
            else:
                i[5]=[int(i[5])*(n/30) for n in range(len(self.df[i[1]]))]
            if i[6]=='None':
                i[6]=2
            else:
                i[6]=int(i[6])
            if i[7]=='None':
                i[7]=1
            else:
                i[7]=(int(i[7])/100)
            plt.scatter(self.df[i[1]],self.df[i[2]]
                        ,color=i[3],marker=Choices_means[i[4]],s=i[5],linewidths=i[6],alpha=i[7])
            legends.append(i[0])
        plt.legend(legends.copy(),loc=1)

