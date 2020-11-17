import sys
import win32gui,win32con,win32api

from AutoThread import *

from TableService import *

from HuoyingHelper  import *
from PointWindow import Ui_MainWindow as Point_Ui_MainWindow

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import *


class PointWindow(QMainWindow,Point_Ui_MainWindow):

    def resize_btn_click(self):

        point_text=self.point_edit.text()
        point_text=point_text.split(",")
        self.resize(int(point_text[0]), int(point_text[1]))

    def __init__(self, parent=None):
        super(PointWindow, self).__init__(parent)
        self.setupUi(self)

        self.resize_btn.clicked.connect(self.resize_btn_click)

    def resizeEvent(self, evt: QtGui.QResizeEvent) -> None:
        w=str(evt.oldSize().width())
        h=str(evt.oldSize().height())
        self.point_edit.setText(w+","+h)

class WebWindow(QMainWindow,Ui_MainWindow):

    #打开获取点位窗口
    def point_win_btn_click(self):
        self.pointWin = PointWindow()
        self.pointWin.show()

    def thread_stop_btn_click(self):
        if isinstance(self.thread,AutoThread) :
            self.thread.terminate()
            self.thread.wait()

    #快捷—下拉列表：刷新事件
    def quick_combo_refresh_click(self):
        self.quick_combo.clear()
        for t in self.tableServie.list_quick():
            self.quick_combo.addItem(t)

    # 快捷—下拉列表：读取
    def quick_combo_load_click(self):
        quick_name=self.quick_combo.currentText()
        quick_actions=self.tableServie.list_action(quick_name)
        self.tableServie.show_data(self.quick_table,quick_actions)

    #快捷按钮:开始线程
    def quick_btn_click(self):
        #切换  标签页
        '''
        self.tabWidget.setCurrentIndex(0)
        '''

        quick_name=self.sender().text()
        quick_actions = self.tableServie.list_action(quick_name)

        # 创建线程
        self.thread = AutoThread(quick_name,quick_actions)
        # # 注册信号处理函数
        self.thread._signal.connect(self.call_back)
        # # 启动线程
        self.thread.start()


    def __init__(self, parent=None):
        super(WebWindow, self).__init__(parent)
        self.setupUi(self)

        self.resize(1500,850)

        #初始化按钮
        self.test_btn.clicked.connect(self.test_btn_click)
        self.point_win_btn.clicked.connect(self.point_win_btn_click)



        #初始化“游戏”标签页
        '''
        self.browser = QWebEngineView()
        self.web_layout.addWidget(self.browser)
        self.browser.settings().setAttribute(QWebEngineSettings.PluginsEnabled,True)
        self.browser.load(QUrl('http://huoying.qq.com/server/website/'))# 加载外部的web界面
        '''

        #初始化“设置”标签页
        self.quick_combo_refresh.clicked.connect(self.quick_combo_refresh_click)
        self.quick_combo_load.clicked.connect(self.quick_combo_load_click)
        self.thread_stop_btn.clicked.connect(self.thread_stop_btn_click)

        self.tableServie=TableService(self.quick_table)

        #初始化“快捷”标签页
        for quick_name in self.tableServie.list_quick():
            btn= QPushButton(quick_name)
            btn.clicked.connect(self.quick_btn_click)
            self.quick_box_main.addWidget(btn)




    def simulate_left_button(self,point):
        print("模拟按钮：",point)
        #获取Flash主键
        flash_o=self.hwnd
        #设置位置
        clickPos = win32api.MAKELONG(int(point[0]),int(point[1]))
        #模拟鼠标
        win32gui.SendMessage(flash_o,win32con.WM_LBUTTONDOWN,win32con.MK_LBUTTON,clickPos)
        time.sleep(0.1)
        win32gui.SendMessage(flash_o, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, clickPos)

    def simulate_left_button_in_my_browser(self,point):
        #print("模拟按钮：",point)
        #获取Flash主键
        flash_o=self.browser.children()[2]
        #设置位置
        clickPos = QPoint(int(point[0]),int(point[1]))
        #模拟鼠标
        press = QMouseEvent(QEvent.MouseButtonPress, clickPos, Qt.LeftButton, Qt.MouseButton.NoButton, Qt.NoModifier)
        QCoreApplication.postEvent(flash_o, press)
        time.sleep(0.1)
        release =QMouseEvent(QEvent.MouseButtonRelease,clickPos,Qt.LeftButton,Qt.MouseButton.NoButton,Qt.NoModifier)
        QCoreApplication.postEvent(flash_o, release)

    def call_back(self,msg_type,msg,msg_info):
        print(msg_type,":",msg,":",msg_info)

        if msg_type!="sleep":
            self.statusbar.showMessage(msg_info,3000)

        if msg_type=="mouse_left":
            self.simulate_left_button(msg.split(","))


    def test_btn_click(self):
        hwnd = win32gui.FindWindow(None,"火影")
        #激活该窗口
        #win32gui.SetForegroundWindow(hwnd)
        hwnd = win32gui.FindWindowEx(hwnd,None,"TabContentWnd","")
        hwnd = win32gui.FindWindowEx(hwnd, None, "iebrowser", None)
        hwnd = win32gui.FindWindowEx(hwnd, None, "Shell Embedding", None)
        hwnd = win32gui.FindWindowEx(hwnd, None, "Shell DocObject View", None)
        hwnd = win32gui.FindWindowEx(hwnd, None, "Internet Explorer_Server", None)
        hwnd = win32gui.FindWindowEx(hwnd, None, "MacromediaFlashPlayerActiveX", None)

        rect=win32gui.GetWindowRect(hwnd)
        self.hwnd=hwnd

        print(rect)
        print("测试按钮")




if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = WebWindow()
    myWin.show()



    sys.exit(app.exec_())

