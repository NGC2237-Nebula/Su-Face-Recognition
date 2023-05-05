# -*- coding: utf-8 -*-
import sys
from time import time

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QApplication, QMainWindow

from ui.start_main_ui import StartMainUi

from logic.admin_main import AdminMainWindow, AdminSettingWindow, LoginWindow, DeleteWindow, UnloadWindow
from logic.user_main import UserMainWindow, RegisterWindow, FaceCompareWindow, ModifyWindow


class StartMainWindow(QMainWindow, StartMainUi):
    signal_user = pyqtSignal()
    signal_admin = pyqtSignal()

    def __init__(self, parent=None):
        super(StartMainWindow, self).__init__(parent)
        self.setupUi(self)

        self.close_button.clicked.connect(self.close)
        self.minimize_button.clicked.connect(self.showMinimized)

        self.user_button.clicked.connect(self.send_signal_user)
        self.admin_button.clicked.connect(self.send_signal_admin)
        self.cancel_button.clicked.connect(self.close)
        self.show()

    def send_signal_user(self):
        self.signal_user.emit()
        self.close()

    def send_signal_admin(self):
        self.signal_admin.emit()
        self.close()


if __name__ == "__main__":
    ui_start_time = time()
    app = QApplication(sys.argv)

    # 主界面
    main_win = StartMainWindow()
    user_main = UserMainWindow()
    admin_main = AdminMainWindow()
    # 用户次界面
    modify = ModifyWindow()
    register = RegisterWindow()
    faceCompare = FaceCompareWindow()
    # 管理员次界面
    login = LoginWindow()
    delete = DeleteWindow()
    unlock = UnloadWindow()
    setting = AdminSettingWindow()

    # 主界面信号槽
    main_win.signal_user.connect(user_main.show)
    main_win.signal_admin.connect(admin_main.show)
    # 用户界面信号槽
    user_main.signal_register.connect(register.show)
    user_main.signal_compare.connect(faceCompare.show)
    user_main.signal_modify.connect(modify.show)
    # 管理员界面信号槽
    admin_main.signal_login.connect(login.show)
    admin_main.signal_unlock.connect(unlock.show)
    admin_main.signal_setting.connect(setting.show)
    admin_main.signal_delete.connect(delete.show)

    print('界面 初始化时间:', time() - ui_start_time)

    sys.exit(app.exec_())
