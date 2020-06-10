
from PyQt5.QtCore import Qt
import matplotlib as mpl
import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QMessageBox
from matplotlib.backends.backend_qt5agg import (FigureCanvas,NavigationToolbar2QT
                                                as NavigationToolbar)
class QmyMainWindow2(QMainWindow):
    def __init__(self,name=None,dataname=None,handle=None,text=None,hollow=None,df=None):
        super().__init__()
        self.setWindowTitle('饼状图绘制')
        mpl.rcParams['font.sans-serif']=['KaiTi','SimHei']
        mpl.rcParams['font.size']=12
        mpl.rcParams['axes.unicode_minus']=False
        self.name=name
        self.dataname=dataname
        self.handle=handle
        self.text=text
        self.hollow=hollow
        self.df=df
        #self.Messagehandle()
        self.__iniFigure()
        self.__drawFigure()

    def __iniFigure(self):
        self.__fig = mpl.figure.Figure(figsize=(8, 8))
        self.__fig.suptitle(self.name)
        figCanvas = FigureCanvas(self.__fig)
        naviToolbar = NavigationToolbar(figCanvas, self)
        self.addToolBar(naviToolbar)
        self.setCentralWidget(figCanvas)
    def __drawFigure(self):

        plt = self.__fig.add_subplot(111)
        if self.handle=='None':

            plt.pie(self.df[self.dataname].value_counts(),autopct='%1.1f%%',radius=1)
            plt.legend(self.df[self.dataname].value_counts().index,loc=1)
            if self.hollow == True:
                x = [1, 0, 0, 0]
                plt.pie(x, colors='w', radius=0.6)
        elif self.handle=='数值分类':
            try :
                datas = []
                legends = []
                if '，' in self.text:
                    text = list(map(float, self.text.split('，')))
                else:
                    text = list(map(float, self.text.split(',')))
                #print(text)
                for each in range(len(text) - 1):
                    datas.append(len(
                        self.df[(self.df[self.dataname] >= text[each]) & (self.df[self.dataname] < text[each + 1])]))
                    legends.append(str(text[each]) + '~' + str(text[each + 1]))
                print(datas)

                plt.pie(datas.copy(), autopct='%1.1f%%',radius=1)
                plt.legend(legends.copy(), loc=1)
                if self.hollow == True:
                    x = [1, 0, 0, 0]
                    plt.pie(x, colors='w', radius=0.6)
                datas.clear()
                legends.clear()
            except Exception as e:
                QMessageBox.information(self,'错误',str(e.args),QMessageBox.Yes,QMessageBox.Yes)
                self.close()
        elif self.handle=='非数值分类':
            try :
                datas = []
                legends = []
                if '，' in self.text:
                    text = self.text.split('，')
                else:
                    text = self.text.split(',')
                #print(text)
                for each in text:
                    datas.append(len(self.df[(self.df[self.dataname]) == each]))
                    legends.append(each)

                plt.pie(datas.copy(), autopct='%1.1f%%',radius=1)
                plt.legend(legends.copy(), loc=1)
                if self.hollow == True:
                    x = [1, 0, 0, 0]
                    plt.pie(x, colors='w', radius=0.6)
                datas.clear()
                legends.clear()
            except Exception as e:
                QMessageBox.information(self, '错误', str(e.args), QMessageBox.Yes, QMessageBox.Yes)
                self.close()








