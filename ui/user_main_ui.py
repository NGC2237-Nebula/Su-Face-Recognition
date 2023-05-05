# -*- coding: utf-8 -*-
import sys
import qtawesome
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtWidgets

class UserMainUi(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("UserMainWindow")
        MainWindow.resize(1200, 800)

        # ------------ 整体界面设计，使用网格布局 ------------ #
        self.main_widget = QtWidgets.QWidget(MainWindow)  # 创建窗口主部件
        self.main_layout = QtWidgets.QGridLayout()  # 创建主部件的网格布局
        self.main_widget.setLayout(self.main_layout)  # 设置窗口主部件布局为网格布局

        self.left_widget = QtWidgets.QWidget(MainWindow)  # 创建左侧部件
        self.left_widget.setObjectName('left_widget')
        self.left_layout = QtWidgets.QGridLayout()
        self.left_widget.setLayout(self.left_layout)  # 设置左侧部件布局为网格

        self.right_widget = QtWidgets.QWidget(MainWindow)  # 创建右侧部件
        self.right_widget.setObjectName('right_widget')
        self.right_layout = QtWidgets.QGridLayout()
        self.right_widget.setLayout(self.right_layout)  # 设置右侧部件布局为网格

        self.main_layout.addWidget(self.left_widget, 0, 0, 15, 2)  # 左侧部件在第0行第0列，占15行2列
        self.main_layout.addWidget(self.right_widget, 0, 2, 15, 10)  # 右侧部件在第0行第2列，占15行10列
        MainWindow.setCentralWidget(self.main_widget)  # 设置窗口主部件

        # ------------ 左侧菜单模块，使用网格布局 ------------ #
        # 关闭按钮
        self.close_button = QtWidgets.QPushButton("")
        # 空白按钮
        self.other_button = QtWidgets.QPushButton("")
        # 最小化按钮
        self.minimize_button = QtWidgets.QPushButton("")

        # JUNIOR 标志
        self.left_label_1 = QtWidgets.QPushButton("JUNIOR")
        self.left_label_1.setObjectName('left_label')
        # SENIOR 标志
        self.left_label_2 = QtWidgets.QPushButton("SENIOR")
        self.left_label_2.setObjectName('left_label')

        # 打开摄像头 按钮
        self.camera_button = QtWidgets.QPushButton(qtawesome.icon('fa5s.video', color='white'), "打开相机")
        self.camera_button.setObjectName('left_button')
        # 用户登录 按钮
        self.login_button = QtWidgets.QPushButton(qtawesome.icon('fa5s.user-alt', color='white'), "用户登录")
        self.login_button.setObjectName('left_button')

        # 用户登出 按钮
        self.logout_button = QtWidgets.QPushButton(qtawesome.icon('fa5s.sign-out-alt', color='white'), "用户登出")
        self.logout_button.setObjectName('left_button')
        # 用户注册 按钮
        self.register_button = QtWidgets.QPushButton(qtawesome.icon('fa5s.user-plus', color='white'), "用户注册")
        self.register_button.setObjectName('left_button')
        # 查询用户 按钮
        self.query_user_button = QtWidgets.QPushButton(qtawesome.icon('fa5s.search', color='white'), "修改信息")
        self.query_user_button.setObjectName('left_button')

        # 人脸识别 按钮
        self.recognition_button = QtWidgets.QPushButton(qtawesome.icon('fa5s.eye', color='white'), "人脸识别")
        self.recognition_button.setObjectName('left_button')
        # 人脸对比 按钮
        self.face_compare_button = QtWidgets.QPushButton(qtawesome.icon('fa5s.people-arrows', color='white'),
                                                         "人脸对比")
        self.face_compare_button.setObjectName('left_button')
        # 活体检测 按钮
        self.biopsy_testing_button = QtWidgets.QPushButton(qtawesome.icon('fa5s.atom', color='white'), "活体检测")
        self.biopsy_testing_button.setObjectName('left_button')
        # 精细分割 按钮
        self.fine_segmentation_button = QtWidgets.QPushButton(qtawesome.icon('fa5s.cut', color='white'), "背景模糊")
        self.fine_segmentation_button.setObjectName('left_button')
        # 关键点检测 按钮
        self.attitude_detection_button = QtWidgets.QPushButton(qtawesome.icon('fa5s.draw-polygon', color='white'),
                                                               "姿态检测")
        self.attitude_detection_button.setObjectName('left_button')

        # 添加左侧按钮
        self.left_layout.addWidget(self.close_button, 0, 0, 1, 1)
        self.left_layout.addWidget(self.other_button, 0, 1, 1, 1)
        self.left_layout.addWidget(self.minimize_button, 0, 2, 1, 1)

        self.left_layout.addWidget(self.left_label_1, 1, 0, 1, 3)
        self.left_layout.addWidget(self.camera_button, 2, 0, 1, 3)
        self.left_layout.addWidget(self.login_button, 3, 0, 1, 3)
        self.left_layout.addWidget(self.logout_button, 4, 0, 1, 3)
        self.left_layout.addWidget(self.register_button, 5, 0, 1, 3)
        self.left_layout.addWidget(self.query_user_button, 6, 0, 1, 3)

        self.left_layout.addWidget(self.left_label_2, 7, 0, 1, 3)
        self.left_layout.addWidget(self.recognition_button, 8, 0, 1, 3)
        self.left_layout.addWidget(self.biopsy_testing_button, 9, 0, 1, 3)
        self.left_layout.addWidget(self.face_compare_button, 10, 0, 1, 3)
        self.left_layout.addWidget(self.fine_segmentation_button, 11, 0, 1, 3)
        self.left_layout.addWidget(self.attitude_detection_button, 12, 0, 1, 3)

        # ------------ 右侧模块，使用网格布局 ------------ #
        # 摄像头展示部分
        self.camera_label = QtWidgets.QLabel('\n人脸识别\n\n系统')
        self.camera_label.setAlignment(Qt.AlignCenter)

        # 信息展示界面
        self.msg_label_a = QtWidgets.QLabel('')
        self.msg_label_b = QtWidgets.QLabel('')
        self.msg_label_c = QtWidgets.QLabel('')
        self.remind_label = QtWidgets.QLabel('')

        self.right_layout.addWidget(self.camera_label, 1, 0, 3, 10)
        self.right_layout.addWidget(self.msg_label_a, 5, 2, )
        self.right_layout.addWidget(self.msg_label_b, 5, 4, )
        self.right_layout.addWidget(self.msg_label_c, 5, 6, )
        self.right_layout.addWidget(self.remind_label, 5, 3, )

        self.camera_label.setMinimumSize(QtCore.QSize(900, 560))
        self.camera_label.setMaximumSize(QtCore.QSize(900, 560))

        labels = [self.msg_label_a, self.msg_label_b, self.msg_label_c]
        for label in labels:
            label.setMinimumSize(QtCore.QSize(150, 200))
            label.setMaximumSize(QtCore.QSize(150, 200))

        self.remind_label.setMinimumSize(QtCore.QSize(170, 200))
        self.remind_label.setMaximumSize(QtCore.QSize(170, 200))

        # ----------------------美化------------------ #
        # 美化控制按钮
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

        # 美化左侧布局
        self.left_widget.setStyleSheet('''
            QPushButton{
                border:none;
                color:white;
                height:35px;
                padding-left:5px;
                padding-right:10px;
                font-size:15px;}
                
            QWidget#left_widget{
                background:#96989B;
                border-top-left-radius:5px;
                border-bottom-left-radius:5px;}
                
            QPushButton#left_label{
                border:none;
                font-size:20px;
                font-weight:700;
                font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;}
                
            QPushButton#left_button:hover{
                color:white;
                border-radius:10px;
                background:#646669;}''')

        # 美化右侧布局
        self.right_widget.setStyleSheet('''
            QWidget#right_widget{
                background:#AAACAF;
                border-top-right-radius:5px;
                border-bottom-right-radius:5px;}''')

        # 去除组件间间隙
        self.right_layout.setContentsMargins(0, 0, 2, 1)
        self.main_layout.setSpacing(0)
        self.right_layout.setSpacing(0)
        self.left_layout.setSpacing(0)

        # 设置整体样式
        MainWindow.setWindowOpacity(0.9)  # 设置窗口透明度
        MainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 隐藏外围边框
        MainWindow.setWindowFlag(QtCore.Qt.FramelessWindowHint) # 产生一个无边框的窗口，用户不能移动和改变大小
        MainWindow.setWindowTitle("人脸识别")  # 设置标题
        MainWindow.setWindowIcon(QIcon('Logo.jpg'))  # 设置logo

        # 其他组件美化
        self.camera_label.setStyleSheet('''
                                        color:#F8FCFF;
                                        font-size:60px;
                                        font-weight:bold;
                                        font-family:Roman times;''')
        self.remind_label.setStyleSheet('''
                                        color:#F0F7F4;
                                        font-size:30px;
                                        font-family:Microsoft YaHei;''')
        self.remind_label.setWordWrap(True)
        self.remind_label.setAlignment(Qt.AlignRight)




if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    widgets = QtWidgets.QMainWindow()
    ui = UserMainUi()
    ui.setupUi(widgets)
    widgets.show()
    sys.exit(app.exec_())
