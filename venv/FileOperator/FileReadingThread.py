from PyQt5.QtCore import QThread,pyqtSignal
import pandas as pd
import chardet
class File_read_thread(QThread):
    '''
    新建一个线程出来进行文件读取

    '''
    '''
    文件读取成功信号
    '''
    fileReadDone = pyqtSignal(type(pd.DataFrame()))

    def __init__(self,filename):
        '''

        :param filename: 传入文件名
        '''

        super().__init__()
        self.FileName=filename
        self.setPriority(7)


    def get_encoding(self):
        with open(self.FileName,'rb') as f:
            return chardet.detect(f.read())['encoding']
    def __del__(self):
        self.wait()
    def run(self):
        '''
        判断文件后缀名来调用对应api读取
        并发射信号

        '''

        '''
        csv文件读取逻辑代码
        '''
        if self.FileName[-4:]=='.csv':
            with open(self.FileName,'rb') as f:
                encoding=self.get_encoding()

                if encoding=='GB2312' or encoding=='gb2312':
                    encoding='gbk'
                if encoding=='ISO-8859-9':
                    encoding='gbk'

                self.df = pd.read_csv(f, index_col=0,encoding=encoding)






        #excel文件读取逻辑代码
        else:


            with open(self.FileName,'rb') as f:
                encoding=self.get_encoding()

                if encoding=='GB2312' or encoding=='gb2312':
                    encoding='gbk'
                if encoding=='ISO-8859-9':
                    encoding='gbk'
                self.df = pd.read_excel(f, index_col=0,encoding=encoding)

        #if self.fileReadDone is not None and self.finished is not 0:

        self.fileReadDone.emit(self.df)


