# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette
import qtawesome


class AdminLoginUi(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(350, 340)

        # 关闭 按钮
        self.close_button = QtWidgets.QPushButton(Dialog)
        self.close_button.setGeometry(QtCore.QRect(20, 20, 31, 21))
        self.close_button.setObjectName("minimize_button")
        # 其他 按钮
        self.other_button = QtWidgets.QPushButton(Dialog)
        self.other_button.setGeometry(QtCore.QRect(60, 20, 31, 21))
        self.other_button.setObjectName("other_button")
        # 最小化 按钮
        self.minimize_button = QtWidgets.QPushButton(Dialog)
        self.minimize_button.setGeometry(QtCore.QRect(100, 20, 31, 21))
        self.minimize_button.setObjectName("close_button")


        self.gridLayoutWidget_1 = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget_1.setGeometry(QtCore.QRect(0, 60, 341, 191))
        self.gridLayoutWidget_1.setObjectName("gridLayoutWidget_1")

        self.gridLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(0, 280, 341, 191))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")

        self.gridLayout_1 = QtWidgets.QGridLayout(self.gridLayoutWidget_1)
        self.gridLayout_1.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_1.setSpacing(0)
        self.gridLayout_1.setObjectName("gridLayout_1")

        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")

        self.layoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.layoutWidget_2.setGeometry(QtCore.QRect(0, 300, 341, 40))
        self.layoutWidget_2.setObjectName("layoutWidget_1")

        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_1")


        # 登录 标题
        self.register_title = QtWidgets.QPushButton(self.gridLayoutWidget_1)
        self.register_title.setObjectName("register_title")
        self.gridLayout_1.addWidget(self.register_title, 0, 0, 1, 2)
        # 姓名 输入框
        self.name_lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget_1)
        self.name_lineEdit.setMaximumSize(QtCore.QSize(167777, 16777215))
        self.name_lineEdit.setObjectName("name_lineEdit")
        self.gridLayout_1.addWidget(self.name_lineEdit, 1, 1, 1, 1)
        # 密码 输入框
        self.password_lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget_1)
        self.password_lineEdit.setObjectName("password_lineEdit")
        self.gridLayout_1.addWidget(self.password_lineEdit, 2, 1, 1, 1)

        # 姓名 标题
        self.register_msg_1 = QtWidgets.QPushButton(self.gridLayoutWidget_1)
        self.register_msg_1.setMinimumSize(QtCore.QSize(50, 0))
        self.register_msg_1.setObjectName("register_msg_1")
        self.gridLayout_1.addWidget(self.register_msg_1, 1, 0, 1, 1)
        # 密码 标题
        self.register_msg_2 = QtWidgets.QPushButton(self.gridLayoutWidget_1)
        self.register_msg_2.setObjectName("register_msg_3")
        self.gridLayout_1.addWidget(self.register_msg_2, 2, 0, 1, 1)

        # 确定 按钮
        self.confirm_button = QtWidgets.QPushButton(self.layoutWidget_2)
        self.confirm_button.setMinimumSize(QtCore.QSize(20, 0))
        self.confirm_button.setObjectName("confirm_button")
        self.horizontalLayout_3.addWidget(self.confirm_button)
        # 取消 按钮
        self.cancel_button = QtWidgets.QPushButton(self.layoutWidget_2)
        self.cancel_button.setMinimumSize(QtCore.QSize(20, 0))
        self.cancel_button.setObjectName("cancel_button")
        self.horizontalLayout_3.addWidget(self.cancel_button)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))

        self.close_button.setText(_translate("Dialog", ""))
        self.other_button.setText(_translate("Dialog", ""))
        self.minimize_button.setText(_translate("Dialog", ""))

        self.register_title.setText(_translate("Dialog", "  登录  "))
        self.register_msg_1.setText(_translate("Dialog", "  账号  "))
        self.register_msg_2.setText(_translate("Dialog", "  密码  "))

        self.confirm_button.setText(_translate("Dialog", "登录"))
        self.cancel_button.setText(_translate("Dialog", "取消"))

        # ------------------------------------ #
        # 控制按钮样式
        self.close_button.setFixedSize(30, 30)  # 设置关闭按钮大小
        self.other_button.setFixedSize(30, 30)  # 设置其他按钮大小
        self.minimize_button.setFixedSize(30, 30)  # 设置最小化按钮的大小

        # 设置按钮部件的QSS样式
        # 默认为淡色，鼠标悬浮时为深色
        self.close_button.setStyleSheet(
            '''QPushButton{background:#F76677;border-radius:7px;}QPushButton:hover{background:red;}''')
        self.other_button.setStyleSheet(
            '''QPushButton{background:#F7D674;border-radius:7px;}QPushButton:hover{background:yellow;}''')
        self.minimize_button.setStyleSheet(
            '''QPushButton{background:#6DDF6D;border-radius:7px;}QPushButton:hover{background:green;}''')

        # ------------------------------------ #
        # 整体样式
        Dialog.setWindowOpacity(0.9)  # 设置窗口透明度
        Dialog.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框
        pe = QPalette()
        Dialog.setAutoFillBackground(True)
        pe.setColor(QPalette.Window, Qt.lightGray)  # 设置背景色
        Dialog.setPalette(pe)

        # ------------------------------------ #
        # 图标样式
        spin_icon = qtawesome.icon('fa5s.folder-open', color='black')
        Dialog.setWindowIcon(spin_icon)

        # ------------------------------------ #
        self.gridLayoutWidget_1.setStyleSheet('''
                QPushButton{
                    border:none;
                    color:white;
                    padding-left:5px;
                    height:50px;
                    font-size:20px;
                    font-weight:500;
                    padding-right:10px;
                    font-family: "Helvetica Neue"
                }''')
        self.gridLayoutWidget_2.setStyleSheet('''
                QPushButton{
                    border:none;
                    color:white;
                    padding-left:5px;
                    height:50px;
                    font-size:20px;
                    font-weight:500;
                    padding-right:10px;
                    font-family: "Helvetica Neue";
                }
                QLabel{
                    font-size:20px;
                    font-weight:600;
                    color:white;
                    ont-family: "Helvetica Neue";
                }''')

        self.register_title.setStyleSheet('''
                QPushButton{
                    border:none;
                    border-bottom:2px solid white;
                    font-size:28px;
                    font-weight:700;
                    font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
                } ''')



        # ------------------------------------ #
        # 输入栏样式
        lineText = [self.name_lineEdit,self.password_lineEdit]
        line = 0
        for lineEdit in lineText:
            lineEdit.setStyleSheet('''
                QLineEdit{
                    border:2px solid gray;
                    font-size:13px;
                    font-weight:700;
                    font-family: "Helvetica Neue";
                    border-radius:12px;
                    height:25px;
                }''')
            lineEdit.setPlaceholderText(str(line))
            lineEdit.setAlignment(Qt.AlignCenter)
        self.name_lineEdit.setPlaceholderText("请输入姓名")
        self.password_lineEdit.setPlaceholderText("请输入密码")


        # ------------------------------------ #
        # 确定 退出按钮样式
        controlButton = [self.confirm_button, self.cancel_button]
        for button in controlButton:
            button.setStyleSheet(''' 
                QPushButton{
                    color:black;
                    border:none;
                    border-bottom:2px solid white;
                    font-size:28px;
                    font-weight:700;
                    font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
                } 
                QPushButton:hover{
                    color:white;
                    border:0px solid #F3F3F5;
                    border-radius:0px;
                    background:LightGray;
                 } ''')

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    widgets = QtWidgets.QMainWindow()
    ui = AdminLoginUi()
    ui.setupUi(widgets)
    widgets.show()
    sys.exit(app.exec_())
