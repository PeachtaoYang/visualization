import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
choices=[
                '  ●  (圆点)',
                '  ▲  (上三角点)',
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
                'None'





            ]
means=['o','^','v','<','>','2','1','3','4','s','p','*','H','h','+','x','D','d','.',None]
Choices_means={}
for key,value in zip(choices,means):
    Choices_means[key]=value
choices1=['----------------（实线）',
 '————————（虚线）',

 '................（点线）',
 '-.-.-.-.-.-.-.-.(虚点线)',
          'None']
means1=['-','--',':','-.',None]
Choices_means1={}
for key,value in zip(choices1,means1):
    Choices_means1[key]=value
class InFo_Handle:
    def __init__(self,message,info,df):
        self.message=message
        self.info=info
        self.df=df
        self.unpackgeInfo()
        self.Paint_info()
    def unpackgeInfo(self):
        self.title=self.message['title']
        self.x_lable=self.message['x_label']
        self.x_label_frontsize=self.message['x_label_frontsize']
        self.x_label_linespace=self.message['x_label_linespace']
        self.y_lable=self.message['y_label']
        self.y_label_frontsize=self.message['y_label_frontsize']
        self.y_label_linespace=self.message['y_label_linespace']
        self.lineInfo=self.info.values.tolist()
    def Paint_info(self):
        fig=plt.figure(figsize=(10,8))
        plt.title(self.title)
        ax = plt.gca()
        if self.x_label_frontsize =='None' and self.x_label_linespace=='None':
            plt.xlabel(self.x_lable)
        elif self.x_label_frontsize == 'None' and self.x_label_linespace != 'None':
            x_major_locator = MultipleLocator(int(self.x_label_linespace))
            plt.xlabel(self.x_lable)
            ax.xaxis.set_major_locator(x_major_locator)
        elif self.x_label_frontsize != 'None' and self.x_label_linespace == 'None':
            plt.xlabel(self.x_lable,fontsize=int(self.x_label_frontsize))
        elif self.x_label_frontsize != 'None' and self.x_label_linespace != 'None':
            x_major_locator = MultipleLocator(int(self.x_label_linespace))
            plt.xlabel(self.x_lable, fontsize=int(self.x_label_frontsize))
            ax.xaxis.set_major_locator(x_major_locator)




        if self.y_label_frontsize =='None' and self.y_label_linespace=='None':
            plt.ylabel(self.y_lable)
        elif self.y_label_frontsize == 'None' and self.y_label_linespace != 'None':
            y_major_locator = MultipleLocator(int(self.y_label_linespace))
            plt.ylabel(self.y_lable)
            ax.yaxis.set_major_locator(y_major_locator)
        elif self.y_label_frontsize != 'None' and self.y_label_linespace == 'None':
            plt.ylabel(self.y_lable,fontsize=int(self.y_label_frontsize))
        elif self.y_label_frontsize != 'None' and self.y_label_linespace != 'None':
            y_major_locator = MultipleLocator(int(self.y_label_linespace))
            plt.ylabel(self.y_lable, fontsize=int(self.y_label_frontsize))
            ax.yaxis.set_major_locator(y_major_locator)
        for i in self.lineInfo:
            if i[4]=='None':
                i[4]=None
            else:
                i[4]=int(i[4])
            if i[6]=='None':
                i[6]=None
            else:
                i[6]=int(i[6])


            plt.plot(self.df[i[0]],self.df[i[1]],
                     linestyle=Choices_means1[i[2]],color=i[3],
                     linewidth=i[4],marker=Choices_means[i[5]],
                     markersize=i[6])
        plt.show()





