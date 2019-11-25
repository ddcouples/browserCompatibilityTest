import sys
import time
import os
from log import *
from operation import *
browserPaths = [r"C:\Program Files\Internet Explorer\iexplore.exe", os.path.abspath('./chrome49/Chrome.exe')]
def init ():
    if len(sys.argv) < 2:
        warn('请输入测试url')
    else:
        for path in browserPaths:
            print((path))
            if (os.path.exists(path)):
               openBrowser(path, sys.argv[1], True if path.find('Chrome') == -1 else False)
            else:
                warn('请先安装对应浏览器' + '~~~~~~~~~~' + path)
    pass
def closeIE():
    os.system("taskkill /F /IM iexplore.exe")
if __name__ == "__main__":  
    init ()