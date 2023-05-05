# -*- coding: utf-8 -*-
import sys
import qtawesome
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import *


class AdminMainUi(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("UserMainWindow")
        MainWindow.resize(300, 600)

        # ------------ 整体界面设计，使用网格布局 ------------ #
        self.main_widget = QtWidgets.QWidget(MainWindow)  # 创建窗口主部件
        self.main_layout = QtWidgets.QGridLayout()  # 创建主部件的网格布局
        self.main_widget.setLayout(self.main_layout)  # 设置窗口主部件布局为网格布局
        self.main_widget.setObjectName('main_widget')

        MainWindow.setCentralWidget(self.main_widget)  # 设置窗口主部件

        # ------------ 左侧菜单模块，使用网格布局 ------------ #
        # 关闭按钮
        self.close_button = QtWidgets.QPushButton("")
        # 空白按钮
        self.other_button = QtWidgets.QPushButton("")
        # 最小化按钮
        self.minimize_button = QtWidgets.QPushButton("")

        # JUNIOR 标志
        self.left_label_1 = QtWidgets.QPushButton("USER")
        self.left_label_1.setObjectName('label')
        # SENIOR 标志
        self.left_label_2 = QtWidgets.QPushButton("HISTORY")
        self.left_label_2.setObjectName('label')
        # ELSE 标志
        self.left_label_3 = QtWidgets.QPushButton("SETTING")
        self.left_label_3.setObjectName('label')


        # 管理员登录 按钮
        self.login_button = QtWidgets.QPushButton(qtawesome.icon('fa5s.user-alt', color='white'), "管理员登录")
        self.login_button.setObjectName('button')

        # 用户解锁 按钮
        self.unlock_button = QtWidgets.QPushButton(qtawesome.icon('fa5s.user-alt', color='white'), "用户解锁")
        self.unlock_button.setObjectName('button')
        # 用户注销 按钮
        self.delete_button = QtWidgets.QPushButton(qtawesome.icon('fa5s.user-alt', color='white'), "用户注销")
        self.delete_button.setObjectName('button')

        # 查询记录 按钮
        self.query_records_button = QtWidgets.QPushButton(qtawesome.icon('fa5s.history', color='white'), "历史记录")
        self.query_records_button.setObjectName('button')
        # 设置 按钮
        self.setting_button = QtWidgets.QPushButton(qtawesome.icon('fa.cog', color='white'), "系统设置")
        self.setting_button.setObjectName('button')

        # 添加左侧按钮
        self.main_layout.addWidget(self.close_button, 0, 0, 1, 1)
        self.main_layout.addWidget(self.minimize_button, 0, 2, 1, 1)
        self.main_layout.addWidget(self.other_button, 0, 1, 1, 1)

        self.main_layout.addWidget(self.left_label_1, 1, 0, 1, 3)
        self.main_layout.addWidget(self.login_button, 2, 0, 1, 3)
        self.main_layout.addWidget(self.unlock_button, 3, 0, 1, 3)
        self.main_layout.addWidget(self.delete_button, 4, 0, 1, 3)

        self.main_layout.addWidget(self.left_label_2, 5, 0, 1, 3)
        self.main_layout.addWidget(self.query_records_button, 6, 0, 1, 3)

        self.main_layout.addWidget(self.left_label_3, 7, 0, 1, 3)
        self.main_layout.addWidget(self.setting_button, 8, 0, 1, 3)


        # ----------------------美化------------------ #
        self.close_button.setFixedSize(28, 28)
        self.other_button.setFixedSize(28, 28)
        self.minimize_button.setFixedSize(28, 28)

        self.close_button.setStyleSheet('''
             QPushButton{
                 background:#F76677;
                 border-radius:7px;}
             QPushButton:hover{
                 background:red;}''')
        self.other_button.setStyleSheet('''
             QPushButton{
                 background:#F7D674;
                 border-radius:7px;}
             QPushButton:hover{
                 background:yellow;}''')
        self.minimize_button.setStyleSheet('''
             QPushButton{
                 background:#6DDF6D;
                 border-radius:7px;}
             QPushButton:hover{
                 background:green;}''')

        # 设置左侧菜单按钮
        # 左侧的部件背景是灰色的，按钮和文字颜色设置为白色，并且将按钮的边框去掉
        self.main_widget.setStyleSheet('''
            QPushButton{
                border:none;
                color:white;
                padding-left:5px;
                height:35px;
                font-size:15px;
                padding-right:10px;}
            QPushButton#label{
                border:none;
                border-bottom:1px solid white;
                font-size:20px;
                font-weight:700;
                font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;}
            QPushButton#button:hover{ 
                color:white;
                border:2px solid #F0F7F4;
                border-radius:15px;
                background:#4D5353;}
            QWidget#main_widget{
                background:#96989B;
                border-top-left-radius:7px;
                border-top-right-radius:7px;
                border-bottom-left-radius:7px;
                border-bottom-left-radius:7px;}''')


        # 设置整体样式
        MainWindow.setWindowOpacity(0.95)  # 设置窗口透明度
        MainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 隐藏边框
        MainWindow.setWindowFlag(QtCore.Qt.FramelessWindowHint)


        MainWindow.setWindowTitle("人脸识别")  # 设置标题
        MainWindow.setWindowIcon(QIcon('Amg.jpg'))  # 设置logo


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    widgets = QtWidgets.QMainWindow()
    ui = AdminMainUi()
    ui.setupUi(widgets)
    widgets.show()
    sys.exit(app.exec_())
