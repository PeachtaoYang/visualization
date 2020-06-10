from PyQt5.QtCore import QThread
class File_Save_as_csv(QThread):
    def __init__(self,df,fileName):
        '''

        :param df: 数据
        :param fileName: 保存的文件名称
        '''
        super().__init__()
        self.df=df
        self.FileName=fileName
    def __del__(self):
        self.wait()
    def run(self):
        '''

        保存为csv文件
        '''
        self.df.to_csv(self.FileName,encoding='utf8')
class File_Save_as_excel(QThread):
    def __init__(self, df, fileName):
        '''

        :param df: 数据
        :param fileName: 保存文件的名称
        '''
        super().__init__()
        self.df = df
        self.FileName = fileName

    def __del__(self):
        self.wait()

    def run(self):
        '''
        保存为excel文件
        :return:
        '''
        self.df.to_excel(self.FileName,encoding='utf8')
