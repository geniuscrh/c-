# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\pycharm_workspace\HuoyingHelper\HuoyingHelper.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(473, 361)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.web_tab = QtWidgets.QWidget()
        self.web_tab.setObjectName("web_tab")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.web_tab)
        self.verticalLayout.setObjectName("verticalLayout")
        self.web_layout = QtWidgets.QVBoxLayout()
        self.web_layout.setObjectName("web_layout")
        self.verticalLayout.addLayout(self.web_layout)
        self.tabWidget.addTab(self.web_tab, "")
        self.quick_tab = QtWidgets.QWidget()
        self.quick_tab.setObjectName("quick_tab")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.quick_tab)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.thread_stop_btn = QtWidgets.QPushButton(self.quick_tab)
        self.thread_stop_btn.setObjectName("thread_stop_btn")
        self.horizontalLayout.addWidget(self.thread_stop_btn)
        self.point_win_btn = QtWidgets.QPushButton(self.quick_tab)
        self.point_win_btn.setObjectName("point_win_btn")
        self.horizontalLayout.addWidget(self.point_win_btn)
        self.test_btn = QtWidgets.QPushButton(self.quick_tab)
        self.test_btn.setObjectName("test_btn")
        self.horizontalLayout.addWidget(self.test_btn)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        self.quick_box = QtWidgets.QGroupBox(self.quick_tab)
        self.quick_box.setObjectName("quick_box")
        self.formLayout = QtWidgets.QFormLayout(self.quick_box)
        self.formLayout.setObjectName("formLayout")
        self.quick_box_main = QtWidgets.QFormLayout()
        self.quick_box_main.setObjectName("quick_box_main")
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.LabelRole, self.quick_box_main)
        self.verticalLayout_5.addWidget(self.quick_box)
        self.tabWidget.addTab(self.quick_tab, "")
        self.setting_tab = QtWidgets.QWidget()
        self.setting_tab.setObjectName("setting_tab")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.setting_tab)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox = QtWidgets.QGroupBox(self.setting_tab)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.quick_combo = QtWidgets.QComboBox(self.groupBox)
        self.quick_combo.setObjectName("quick_combo")
        self.horizontalLayout_3.addWidget(self.quick_combo)
        self.quick_combo_load = QtWidgets.QPushButton(self.groupBox)
        self.quick_combo_load.setObjectName("quick_combo_load")
        self.horizontalLayout_3.addWidget(self.quick_combo_load)
        self.quick_combo_add = QtWidgets.QPushButton(self.groupBox)
        self.quick_combo_add.setObjectName("quick_combo_add")
        self.horizontalLayout_3.addWidget(self.quick_combo_add)
        self.quick_combo_refresh = QtWidgets.QPushButton(self.groupBox)
        self.quick_combo_refresh.setObjectName("quick_combo_refresh")
        self.horizontalLayout_3.addWidget(self.quick_combo_refresh)
        self.verticalLayout_3.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.setting_tab)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.quick_table = QtWidgets.QTableView(self.groupBox_2)
        self.quick_table.setObjectName("quick_table")
        self.verticalLayout_4.addWidget(self.quick_table)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.table_row_save = QtWidgets.QPushButton(self.groupBox_2)
        self.table_row_save.setObjectName("table_row_save")
        self.horizontalLayout_2.addWidget(self.table_row_save)
        self.table_row_add = QtWidgets.QPushButton(self.groupBox_2)
        self.table_row_add.setObjectName("table_row_add")
        self.horizontalLayout_2.addWidget(self.table_row_add)
        self.table_row_del = QtWidgets.QPushButton(self.groupBox_2)
        self.table_row_del.setObjectName("table_row_del")
        self.horizontalLayout_2.addWidget(self.table_row_del)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.verticalLayout_3.addWidget(self.groupBox_2)
        self.tabWidget.addTab(self.setting_tab, "")
        self.verticalLayout_2.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 473, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.web_tab), _translate("MainWindow", "游戏"))
        self.thread_stop_btn.setText(_translate("MainWindow", "停止线程"))
        self.point_win_btn.setText(_translate("MainWindow", "点位获取"))
        self.test_btn.setText(_translate("MainWindow", "开发测试按钮"))
        self.quick_box.setTitle(_translate("MainWindow", "快捷"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.quick_tab), _translate("MainWindow", "快捷"))
        self.groupBox.setTitle(_translate("MainWindow", "GroupBox"))
        self.quick_combo_load.setText(_translate("MainWindow", "读取"))
        self.quick_combo_add.setText(_translate("MainWindow", "增加"))
        self.quick_combo_refresh.setText(_translate("MainWindow", "刷新"))
        self.groupBox_2.setTitle(_translate("MainWindow", "GroupBox"))
        self.table_row_save.setText(_translate("MainWindow", "保存"))
        self.table_row_add.setText(_translate("MainWindow", "增加"))
        self.table_row_del.setText(_translate("MainWindow", "删除"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.setting_tab), _translate("MainWindow", "设置"))