# _*_ coding:UTF-8 _*_
import win32api
import win32con
import win32gui
from ctypes import *
import time
from vk_code import VK_CODE
from printscreen import screenshot
class POINT(Structure):
    _fields_ = [("x", c_ulong),("y", c_ulong)]
def get_mouse_point():
    po = POINT()
    windll.user32.GetCursorPos(byref(po))
    return int(po.x), int(po.y)
def mouse_click(x=None,y=None):
    if not x is None and not y is None:
        mouse_move(x,y)
        time.sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
def mouse_dclick(x=None,y=None):
    if not x is None and not y is None:
        mouse_move(x,y)
        time.sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
def mouse_move(x,y):
    windll.user32.SetCursorPos(x, y)
def key_input(str=''):
    for c in str:
        win32api.keybd_event(VK_CODE[c],0,0,0)
        win32api.keybd_event(VK_CODE[c],0,win32con.KEYEVENTF_KEYUP,0)
        time.sleep(0.01)
def maxWindow():
    win32api.keybd_event(122,0,0,0) #F11
    win32api.keybd_event(122,0,win32con.KEYEVENTF_KEYUP,0) #Realize the F11 button
def keyDownF12():
    win32api.keybd_event(VK_CODE['F12'],0,0,0) #F12
    win32api.keybd_event(VK_CODE['F12'],0,win32con.KEYEVENTF_KEYUP,0) 
def ieSwitchConsole():
    pressQuicKey(['ctrl', '2'])
    # win32api.keybd_event(VK_CODE['ctrl'],0,0,0) #F12
    # win32api.keybd_event(VK_CODE['2'],0,0,0) #F12
    # win32api.keybd_event(VK_CODE['ctrl'],0,win32con.KEYEVENTF_KEYUP,0) 
    # win32api.keybd_event(VK_CODE['2'],0,win32con.KEYEVENTF_KEYUP,0)
def pressF5():
    win32api.keybd_event(VK_CODE['F5'],0,0,0)
    win32api.keybd_event(VK_CODE['F5'],0,win32con.KEYEVENTF_KEYUP,0)
def pressQuicKey(keys=[]):
    for i in keys:
        win32api.keybd_event(VK_CODE[i],0,0,0)
    for i in keys:
        win32api.keybd_event(VK_CODE[i],0,win32con.KEYEVENTF_KEYUP,0)

def pressCtrlShiftF5():
    pressQuicKey(['ctrl', 'shift', 'F5'])
def switchTab():
    win32api.keybd_event(17,0,0,0) #Ctrl
    win32api.keybd_event(9,0,0,0) #Tab
    win32api.keybd_event(17,0,win32con.KEYEVENTF_KEYUP,0) #Realize the Ctrl button
    win32api.keybd_event(19,0,win32con.KEYEVENTF_KEYUP,0) #Realize the Tab button
def openBrowser(path, url, isIE = False):
    browser = win32api.ShellExecute(0, 'open', path, url, '', 1)
    time.sleep(1)
    # user32 =  WinDLL('user32')
    # SW_MAXIMISE = 3
    # hWnd = user32.GetForegroundWindow()
    # user32.ShowWindow(hWnd, SW_MAXIMISE)
    win32gui.ShowWindow(browser, 3)
    keyDownF12()
    if isIE:
        ieSwitchConsole()
        pressF5()
        time.sleep(1)
        pressCtrlShiftF5()
    else:
        pressQuicKey('esc')
        pressF5()
    firsthWn =  win32gui.GetForegroundWindow()
    time.sleep(3)
    now = int(round(time.time()*1000))
    # now2 = time.strftime('%Y-%m-%d~%H:%M:%S',time.localtime(now/1000))
    text = 'ie' if isIE else 'chrome49'
    screenshot(f'./{text}-{now}.png')
    time.sleep(1)
    win32gui.PostMessage(firsthWn, win32con.WM_CLOSE, 0, 0)
if __name__ == "__main__":    
    mouse_click(500,280)
    str1 = 'python'
    key_input(str1)
    mouse_click(1000,280)