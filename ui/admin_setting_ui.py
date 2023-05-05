# -*- coding: utf-8 -*-
import sys
import qtawesome
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette


class AdminSettingUi(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(500, 380)

        self.close_button = QtWidgets.QPushButton(Dialog)
        self.close_button.setGeometry(QtCore.QRect(20, 20, 31, 21))
        self.close_button.setObjectName("close_button")

        self.other_button = QtWidgets.QPushButton(Dialog)
        self.other_button.setGeometry(QtCore.QRect(60, 20, 31, 21))
        self.other_button.setObjectName("modify_more_button")

        self.minimize_button = QtWidgets.QPushButton(Dialog)
        self.minimize_button.setGeometry(QtCore.QRect(100, 20, 31, 21))
        self.minimize_button.setObjectName("search_title")

        self.gridLayoutWidget_5 = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget_5.setGeometry(QtCore.QRect(0, 50, 480, 200))
        self.gridLayoutWidget_5.setObjectName("gridLayoutWidget_5")

        self.gridLayout_6 = QtWidgets.QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName("gridLayout_6")

        self.recognition_threshold_lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget_5)
        self.recognition_threshold_lineEdit.setObjectName("recognition_threshold_lineEdit")
        self.gridLayout_6.addWidget(self.recognition_threshold_lineEdit, 2, 1, 1, 1)

        self.img_size_lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget_5)
        self.img_size_lineEdit.setObjectName("img_size_lineEdit")
        self.gridLayout_6.addWidget(self.img_size_lineEdit, 3, 1, 1, 1)

        self.camera_address_lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget_5)
        self.camera_address_lineEdit.setObjectName("name_lineEdit")
        self.gridLayout_6.addWidget(self.camera_address_lineEdit, 1, 1, 1, 1)

        self.recognition_threshold_text = QtWidgets.QPushButton(self.gridLayoutWidget_5)
        self.recognition_threshold_text.setObjectName("pushButton")
        self.gridLayout_6.addWidget(self.recognition_threshold_text, 2, 0, 1, 1)

        self.camera_address_text = QtWidgets.QPushButton(self.gridLayoutWidget_5)
        self.camera_address_text.setMinimumSize(QtCore.QSize(30, 0))
        self.camera_address_text.setObjectName("pushButton")
        self.gridLayout_6.addWidget(self.camera_address_text, 1, 0, 1, 1)

        self.img_size_text = QtWidgets.QPushButton(self.gridLayoutWidget_5)
        self.img_size_text.setObjectName("pushButton")
        self.gridLayout_6.addWidget(self.img_size_text, 3, 0, 1, 1)

        self.setting_title_text = QtWidgets.QPushButton(self.gridLayoutWidget_5)
        self.setting_title_text.setObjectName("setting_title_text")
        self.gridLayout_6.addWidget(self.setting_title_text, 0, 0, 1, 2)

        self.verticalLayoutWidget_4 = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(10, 250, 480, 200))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")

        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")

        self.gridLayout_8 = QtWidgets.QGridLayout()
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.verticalLayout_5.addLayout(self.gridLayout_8)

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.confirm_button = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.confirm_button.setMinimumSize(QtCore.QSize(20, 0))
        self.confirm_button.setObjectName("confirm_button")
        self.horizontalLayout_2.addWidget(self.confirm_button)

        self.cancel_button = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.cancel_button.setMinimumSize(QtCore.QSize(20, 0))
        self.cancel_button.setObjectName("cancel_button")
        self.horizontalLayout_2.addWidget(self.cancel_button)

        self.verticalLayout_5.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))

        self.close_button.setText(_translate("Dialog", ""))
        self.other_button.setText(_translate("Dialog", ""))
        self.minimize_button.setText(_translate("Dialog", ""))

        self.setting_title_text.setText(_translate("Dialog", "图像相关设置"))
        self.camera_address_text.setText(_translate("Dialog", "摄像头地址"))
        self.recognition_threshold_text.setText(_translate("Dialog", "人脸识别阈值"))
        self.img_size_text.setText(_translate("Dialog", "处理图像大小"))

        self.confirm_button.setText(_translate("Dialog", "应用"))
        self.cancel_button.setText(_translate("Dialog", "退出"))

        # ------------------------------------ #
        # 控制按钮样式
        self.close_button.setFixedSize(30, 30)  # 设置关闭按钮的大小
        self.other_button.setFixedSize(30, 30)  # 设置按钮大小
        self.minimize_button.setFixedSize(30, 30)  # 设置最小化按钮大小

        # 设置按钮部件的QSS样式
        self.close_button.setStyleSheet(
            '''QPushButton{background:#F76677;border-radius:12px;}QPushButton:hover{background:red;}''')
        self.other_button.setStyleSheet(
            '''QPushButton{background:#F7D674;border-radius:12px;}QPushButton:hover{background:yellow;}''')
        self.minimize_button.setStyleSheet(
            '''QPushButton{background:#6DDF6D;border-radius:12px;}QPushButton:hover{background:green;}''')


        # ------------------------------------ #
        # 整体样式
        Dialog.setWindowOpacity(0.9)
        Dialog.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        pe = QPalette()
        Dialog.setAutoFillBackground(True)
        pe.setColor(QPalette.Window, Qt.lightGray)
        Dialog.setPalette(pe)

        # ------------------------------------ #
        # 图标样式
        spin_icon = qtawesome.icon('fa5s.sliders-h', color='black')
        Dialog.setWindowIcon(spin_icon)

        # ------------------------------------ #
        self.gridLayoutWidget_5.setStyleSheet('''
            QPushButton{
                border:none;
                color:white;
                padding-left:5px;
                height:50px;
                font-size:20px;
                font-weight:500;
                padding-right:10px;
                font-family: "Helvetica Neue"
                }
            QPushButton:hover{
                border-right:4px solid black;
                font-weight:500;
                }''')

        self.verticalLayoutWidget_4.setStyleSheet('''
            QPushButton{
                border:none;color:white;
                padding-left:5px;
                height:50px;
                font-size:20px;
                font-weight:500;
                padding-right:10px;
                font-family: "Helvetica Neue";
                }
            QLabel{ 
                font-size:20px;
                font-weight:600;color:white;
                font-family: "Helvetica Neue";
                }
            QPushButton:hover{
                color:white;
                border:2px solid #F3F3F5;
                border-radius:10px;
                background:LightGray;
                } ''')

        line_edit = [self.camera_address_lineEdit, self.img_size_lineEdit, self.recognition_threshold_lineEdit]
        for line in line_edit:
            line.setStyleSheet('''
            QLineEdit{
                border:2px solid gray;
                font-size:13px;
                font-weight:700;
                font-family: "Helvetica Neue";
                border-radius:15px;
                height:30px;
                }''')
            line.setAlignment(Qt.AlignCenter)

        list_below_button = [self.confirm_button, self.cancel_button]
        for below_button in list_below_button:
            below_button.setStyleSheet(''' 
            QPushButton{
                color:black;
                border:none;
                border-bottom:2px solid white;
                font-size:30px;
                font-weight:700;
                font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
            } 
            QPushButton:hover{color:black;} ''')

        self.camera_address_lineEdit.setPlaceholderText("默认 0")  # 摄像头地址 ip摄像头查询rtsp地址放入
        self.img_size_lineEdit.setPlaceholderText("默认 0.33")  # 处理图像大小 太高处理慢，太低识别效果不好
        self.recognition_threshold_lineEdit.setPlaceholderText("默认 0.42")  # 人脸识别阈值 太低无法识别，太高容易混淆


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    widgets = QtWidgets.QMainWindow()
    ui = AdminSettingUi()
    ui.setupUi(widgets)
    widgets.show()
    sys.exit(app.exec_())
