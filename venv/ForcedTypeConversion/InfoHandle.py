import numpy as np
from pandas import to_datetime
from ForcedTypeConversion.timeRadioButton import mytimeRadio
#info=['int (整数)','float  (小数)','string  (字符串)','time  (时间序列）']
info={
    'int (整数)':np.int,
    'float  (小数)':np.float,
    'string  (字符串)':np.str
}


def TypeHandle(this,data):
    '''

    :param this:
    :param data:
    :return:
    '''

    formatStr=None

    def receive(string):
        global formatStr
        formatStr=string
    for i in data:
        if i[1]=='time  (时间序列）':
            this.tempui=mytimeRadio()
            this.tempui.show()
            this.tempui.okButtonPressed.connect(receive)
            this.orignal_df[i[0]]=to_datetime(this.orignal_df[i[0]],errors='ignore',format=formatStr)
        else:
            this.orignal_df[i[0]].astype(info[i[1]],errors='ignore',copy=False)
    #return this.orignal_df

