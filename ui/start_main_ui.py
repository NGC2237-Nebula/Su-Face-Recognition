# -*- coding: utf-8 -*-
import sys

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon


class StartMainUi(object):
    def setupUi(self, MainWindow):
        MainWindow.resize(700, 450)

        self.main_widget = QtWidgets.QWidget(MainWindow)  # 创建窗口主部件
        self.main_layout = QtWidgets.QGridLayout()  # 创建主部件的网格布局
        self.main_widget.setLayout(self.main_layout)  # 设置窗口主部件布局为网格布局
        MainWindow.setCentralWidget(self.main_widget)
        self.close_button = QtWidgets.QPushButton(MainWindow)
        self.close_button.setGeometry(QtCore.QRect(30, 30, 31, 21))
        self.other_button = QtWidgets.QPushButton(MainWindow)
        self.other_button.setGeometry(QtCore.QRect(90, 30, 31, 21))
        self.minimize_button = QtWidgets.QPushButton(MainWindow)
        self.minimize_button.setGeometry(QtCore.QRect(150, 30, 31, 21))
        self.Title_label = QtWidgets.QLabel(MainWindow)
        self.Title_label.setGeometry(QtCore.QRect(170, 100, 360, 60))
        self.user_button = QtWidgets.QPushButton(MainWindow)
        self.user_button.setGeometry(QtCore.QRect(150, 210, 400, 40))
        self.admin_button = QtWidgets.QPushButton(MainWindow)
        self.admin_button.setGeometry(QtCore.QRect(150, 270, 400, 40))
        self.cancel_button = QtWidgets.QPushButton(MainWindow)
        self.cancel_button.setGeometry(QtCore.QRect(150, 330, 400, 40))

        # ------------------------------------ #
        self.close_button.setFixedSize(30, 30)
        self.other_button.setFixedSize(30, 30)
        self.minimize_button.setFixedSize(30, 30)

        self.close_button.setStyleSheet(
            '''QPushButton{background:#F76677;border-radius:12px;}QPushButton:hover{background:red;}''')
        self.other_button.setStyleSheet(
            '''QPushButton{background:#F7D674;border-radius:12px;}QPushButton:hover{background:yellow;}''')
        self.minimize_button.setStyleSheet(
            '''QPushButton{background:#6DDF6D;border-radius:12px;}QPushButton:hover{background:green;}''')

        MainWindow.setWindowOpacity(0.85)
        MainWindow.setAttribute(Qt.WA_TranslucentBackground)
        MainWindow.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        MainWindow.setAutoFillBackground(True)
        MainWindow.setWindowTitle("人脸识别")
        MainWindow.setWindowIcon(QIcon('Logo.jpg'))

        buttons = [self.user_button,self.admin_button,self.cancel_button]
        for button in buttons:
            button.setStyleSheet('''
                QPushButton{
                    border:none;
                    color:white;
                    padding-left:5px;
                    padding-right:10px;
                    font-size:20px;
                    font-weight:700;
                    font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;}
                QPushButton:hover{ 
                    color:white;
                    border:1.5px solid #F0F7F4;
                    border-radius:10px;
                    background:#707275;}''')

        self.main_widget.setStyleSheet('''
            QWidget{
                background:#96989B;
                border-top-right-radius:15px;
                border-top-left-radius:15px;
                border-bottom-right-radius:15px;
                border-bottom-left-radius:15px;}''')


        self.Title_label.setAlignment(Qt.AlignCenter)
        self.Title_label.setStyleSheet("QLabel{color:#F8FCFF;font-size:60px;font-weight:bold;font-family:Roman times;}")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.Title_label.setText(_translate("Form", "——人脸识别系统——"))
        self.user_button.setText(_translate("Form", "用户身份登录"))
        self.admin_button.setText(_translate("Form", "管理员身份登录"))
        self.cancel_button.setText(_translate("Form", "取消"))



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    widgets = QtWidgets.QMainWindow()
    ui = StartMainUi()
    ui.setupUi(widgets)
    widgets.show()
    sys.exit(app.exec_())
