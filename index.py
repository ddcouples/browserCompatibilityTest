import sys
import time
import os
from log import *
from operation import *
def init ():
    if len(sys.argv) < 2:
        warn('请输入测试url')
    else:
        openBrowser("C:\Program Files\Internet Explorer\iexplore.exe", sys.argv[1], True)
    pass
def closeIE():
    os.system("taskkill /F /IM iexplore.exe")
if __name__ == "__main__":  
    init ()