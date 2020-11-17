import time
from  PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import QThread

class AutoThread(QThread):
    _signal = pyqtSignal(str,str,str)


    def __init__(self, thread_name,quick_actions):
        super(AutoThread,self).__init__()
        self.thread_name=thread_name
        self.quick_actions=quick_actions


    def run(self):
        self._signal.emit("start", self.thread_name, "线程创建成功:" + self.thread_name)
        time.sleep(1)
        while True:
            for index,action in self.quick_actions.iterrows():
                self._signal.emit(str(action["动作"]), str(action["内容"]), action["提示"])
                if action["动作"]=="sleep":
                    time.sleep(int(action["内容"]))

        self._signal.emit("end",self.thread_name,"线程执行完成:"+self.thread_name)
        #while True:
        #
        #    time.sleep(3)
        #    self._signal.emit("mouse_left", "741,565","返回游戏")
        #    time.sleep(3)
