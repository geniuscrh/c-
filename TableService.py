import pandas as pd
from PyQt5.QtGui import QStandardItemModel,QStandardItem

class TableService():
    def __init__(self,quick_table):
        super(TableService, self).__init__()

        self.excel_path="D:/火影.xlsx"

        model = QStandardItemModel()
        model.setHorizontalHeaderLabels(['排序','动作',"内容","提示"])

        quick_table.setModel(model)

        quick_table.setColumnWidth(1,300)
        quick_table.setColumnWidth(2, 300)
        quick_table.horizontalHeader().setStretchLastSection(True)  # 最后一列自动拉长


    def load(self):
        self.data = pd.read_excel(self.excel_path)

        # self.model.setItem(0, 0, QStandardItem("基于网优工参的经纬度纠错"))
        # self.model.setItem(1, 0, QStandardItem("基于资产系统的RRU数量纠错"))
        # self.model.setItem(2, 0, QStandardItem("基于网管数据的RRU型号纠错"))
        pass

    def show_data(self,quick_table,quick_actions):
        model = quick_table.model()
        for index,action  in quick_actions.iterrows():

            model.setItem(index, 0, QStandardItem(str(action["排序"])))
            model.setItem(index, 1, QStandardItem(str(action["动作"])))
            model.setItem(index, 2, QStandardItem(str(action["内容"])))
            model.setItem(index, 3, QStandardItem(str(action["提示"])))


    def list_quick(self):
        self.load()
        return self.data["快捷"].unique()

    def list_action(self,quick_name):
        return self.data[self.data["快捷"]==quick_name]
