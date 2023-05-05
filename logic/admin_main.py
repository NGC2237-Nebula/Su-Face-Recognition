# -*- coding: utf-8 -*-
import os
import sys
import configparser
from shutil import copyfile
from time import time

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QDialog

from ui.admin_setting_ui import AdminSettingUi
from ui.admin_main_ui import AdminMainUi
from ui.admin_login_ui import AdminLoginUi
from ui.admin_delete_ui import AdminDeleteUi
from ui.admin_unload_ui import AdminUnloadUi

from util import AdminSqlUtil
from util import UserSqlUtil

# 文件目录
curPath = os.path.abspath(os.path.dirname(__file__))
# 项目根路径
rootPath = curPath[:curPath.rindex('logic')]
# 配置文件夹路径
CONF_FOLDER_PATH = rootPath + 'conf\\'
# 数据文件夹路径
DATA_FOLDER_PATH = rootPath + 'data\\'

conf = configparser.ConfigParser()
conf.read(CONF_FOLDER_PATH + 'setting.conf', encoding='gbk')
CAPTURE_SOURCE = conf.get('image_config', 'capture_source')
if CAPTURE_SOURCE == '0':
    CAPTURE_SOURCE = int(CAPTURE_SOURCE)
TOLERANCE = float(conf.get('image_config', 'tolerance'))
SET_SIZE = float(conf.get('image_config', 'set_size'))
HISTORY_FOLDER_PATH = conf.get('image_config', 'export_path')

ADMIN_LOGIN_FLAG = False


# 主界面
class AdminMainWindow(QMainWindow, AdminMainUi):
    signal_login = pyqtSignal()  # 管理员登录 界面信号
    signal_unlock = pyqtSignal()  # 用户解锁 界面信号
    signal_delete = pyqtSignal()  # 用户注销 界面信号
    signal_setting = pyqtSignal()  # 系统设置 界面信号

    def __init__(self, parent=None):
        super(AdminMainWindow, self).__init__(parent)
        self.setupUi(self)

        self.close_button.clicked.connect(self.close)  # 关闭窗口
        self.minimize_button.clicked.connect(self.showMinimized)  # 最小化窗口

        self.login_button.clicked.connect(self.admin_login)
        self.unlock_button.clicked.connect(self.user_unlock)
        self.delete_button.clicked.connect(self.user_delete)
        self.query_records_button.clicked.connect(self.open_record)
        self.setting_button.clicked.connect(self.setting)

    def send_signal_login(self):
        self.signal_login.emit()

    def send_signal_unlock(self):
        self.signal_unlock.emit()

    def send_signal_delete(self):
        self.signal_delete.emit()

    def send_signal_setting(self):
        self.signal_setting.emit()

    # 管理员登录
    def admin_login(self):
        global ADMIN_LOGIN_FLAG
        if not ADMIN_LOGIN_FLAG:
            QApplication.processEvents()
            login_win = LoginWindow(self)
            login_win.exec_()
            login_win.destroy()
        else:
            QMessageBox.about(self, '提示', '管理员已经登录')

    # 用户解锁
    def user_unlock(self):
        global ADMIN_LOGIN_FLAG
        if not ADMIN_LOGIN_FLAG:
            QMessageBox.about(self, '提示', '请先登录管理员身份')
        else:
            self.send_signal_unlock()

    # 用户注销
    def user_delete(self):
        global ADMIN_LOGIN_FLAG
        if not ADMIN_LOGIN_FLAG:
            QMessageBox.about(self, '提示', '请先登录管理员身份')
        else:
            self.send_signal_delete()

    # 历史记录
    def open_record(self):
        global ADMIN_LOGIN_FLAG
        if not ADMIN_LOGIN_FLAG:
            QMessageBox.about(self, '提示', '请先登录管理员身份')
        else:
            self.export_excel()

    # 设置
    def setting(self):
        global ADMIN_LOGIN_FLAG
        if not ADMIN_LOGIN_FLAG:
            QMessageBox.about(self, '提示', '请先登录管理员身份')
        else:
            self.send_signal_setting()

    # 导出历史记录
    def export_excel(self):
        global DATA_FOLDER_PATH
        global HISTORY_FOLDER_PATH
        local_path = DATA_FOLDER_PATH + "history.xls"
        export_path = HISTORY_FOLDER_PATH + "历史记录.xls"
        if os.path.exists(export_path):
            os.remove(export_path)
        try:
            copyfile(local_path, export_path)
        except IOError:
            QMessageBox.about(self, '提示', '历史记录导出失败，请重试')
            exit(1)
        os.popen(export_path)

# 用户解锁
class UnloadWindow(QDialog, AdminUnloadUi):
    def __init__(self, parent=None):
        super(UnloadWindow, self).__init__(parent)
        self.setupUi(self)

        self.minimize_button.clicked.connect(self.showMinimized)
        self.close_button.clicked.connect(self.close_window)

        self.confirm_button.clicked.connect(self.unload_user)
        self.cancel_button.clicked.connect(self.close_window)

    # 解锁用户
    def unload_user(self):
        input_name = self.name_lineEdit.text()
        input_password = self.password_lineEdit.text()

        if input_name == "":
            QMessageBox.about(self, '提示', '姓名不能为空')
        elif input_password == "":
            QMessageBox.about(self, '提示', '密码不能为空')
        else:
            row = UserSqlUtil.search_by_name("\"" + input_name + "\"")
            if row:
                result = row[0]
                password = result[1]
                if input_password != password:
                    QMessageBox.about(self, '提示', '密码输入错误')
                else:
                    if AdminSqlUtil.delete_by_name(row[0]):
                        QMessageBox.about(self, '提示', '解锁成功')
                    else:
                        QMessageBox.about(self, '提示', '解锁失败，请重试')
                    self.close_window()
            else:
                QMessageBox.about(self, '提示', '该用户不存在')

    # 关闭窗口
    def close_window(self):
        self.name_lineEdit.setPlaceholderText("请输入姓名")
        self.password_lineEdit.setPlaceholderText("请输入密码")
        self.close()


# 用户删除
class DeleteWindow(QDialog, AdminDeleteUi):
    def __init__(self, parent=None):
        super(DeleteWindow, self).__init__(parent)
        self.setupUi(self)

        self.minimize_button.clicked.connect(self.showMinimized)
        self.close_button.clicked.connect(self.close_window)

        self.confirm_button.clicked.connect(self.user_delete)
        self.cancel_button.clicked.connect(self.close_window)

    def user_delete(self):
        input_name = self.name_lineEdit.text()
        input_password = self.password_lineEdit.text()

        if input_name == "":
            QMessageBox.about(self, '提示', '姓名不能为空')
        elif input_password == "":
            QMessageBox.about(self, '提示', '密码不能为空')
        else:
            row = UserSqlUtil.search_by_name("\"" + input_name + "\"")
            if row:
                result = row[0]
                password = result[1]
                if input_password != password:
                    QMessageBox.about(self, '提示', '密码输入错误')
                else:
                    flag = UserSqlUtil.delete_by_name(input_name)
                    if flag:
                        QMessageBox.about(self, '提示', '删除成功')
                    else:
                        QMessageBox.about(self, '提示', '删除失败，请重试')
                    self.close_window()
            else:
                QMessageBox.about(self, '提示', '该用户不存在')

    # 关闭窗口
    def close_window(self):
        self.name_lineEdit.setPlaceholderText("请输入姓名")
        self.password_lineEdit.setPlaceholderText("请输入密码")
        self.close()


# 管理员登录界面
class LoginWindow(QDialog, AdminLoginUi):
    def __init__(self, parent=None):
        super(LoginWindow, self).__init__(parent)
        self.setupUi(self)

        self.minimize_button.clicked.connect(self.showMinimized)
        self.close_button.clicked.connect(self.cancel_login)

        self.confirm_button.clicked.connect(self.search_user)
        self.cancel_button.clicked.connect(self.cancel_login)

    # 点击确认，搜索管理员
    def search_user(self):
        input_name = self.name_lineEdit.text()
        input_password = self.password_lineEdit.text()

        if input_name == "":
            QMessageBox.about(self, '提示', '姓名不能为空')
        elif input_password == "":
            QMessageBox.about(self, '提示', '密码不能为空')
        else:
            row = AdminSqlUtil.search_by_name("\"" + input_name + "\"")
            if row:
                result = row[0]
                password = result[1]
                if input_password != password:
                    QMessageBox.about(self, '提示', '密码输入错误')
                else:
                    global ADMIN_LOGIN_FLAG
                    ADMIN_LOGIN_FLAG = True
                    QMessageBox.about(self, '提示', '登录成功')
                    self.close_window()
            else:
                QMessageBox.about(self, '提示', '该用户不存在')

    # 点击取消按钮
    def cancel_login(self):
        global ADMIN_LOGIN_FLAG
        ADMIN_LOGIN_FLAG = False
        self.close_window()

    # 关闭窗口
    def close_window(self):
        self.name_lineEdit.setPlaceholderText("请输入姓名")
        self.password_lineEdit.setPlaceholderText("请输入密码")
        self.close()


# 设置界面
class AdminSettingWindow(QMainWindow, AdminSettingUi):
    def __init__(self, parent=None):
        super(AdminSettingWindow, self).__init__(parent)
        self.setupUi(self)
        self.close_button.clicked.connect(self.close)  # 关闭窗口
        self.minimize_button.clicked.connect(self.showMinimized)  # 最小化窗口

        self.camera_address_lineEdit.setPlaceholderText(str(CAPTURE_SOURCE))  # 摄像头地址
        self.img_size_lineEdit.setPlaceholderText(str(SET_SIZE))  # 处理图像大小
        self.recognition_threshold_lineEdit.setPlaceholderText(str(TOLERANCE))  # 人脸识别阈值

        self.cancel_button.clicked.connect(self.close)
        self.confirm_button.clicked.connect(self.change_config)

    # 修改配置
    def change_config(self):
        flag = 0
        setting_conf = configparser.ConfigParser()
        setting_conf.read(CONF_FOLDER_PATH + 'setting.conf', encoding='gbk')

        size = self.img_size_lineEdit.text()
        address = self.camera_address_lineEdit.text()
        threshold = self.recognition_threshold_lineEdit.text()

        if address != '':
            setting_conf.set('image_config', 'capture_source', address)
            flag = 1
        if size != '':
            try:
                if 0 < float(size) < 1:
                    setting_conf.set('image_config', 'set_size', size)
                    flag = 1
                else:
                    QMessageBox.about(self, '提示', '处理图像大小-取值在0到1之间')
            except:
                QMessageBox.about(self, '提示', '处理图像大小-输入格式有问题')
        if threshold != '':
            try:
                if 0 < float(threshold) < 1:
                    setting_conf.set('image_config', 'tolerance', threshold)
                    flag = 1
                else:
                    QMessageBox.about(self, '提示', '人脸识别阈值-取值在0到1之间')
            except:
                QMessageBox.about(self, '提示', '人脸识别阈值-输入格式有误')

        setting_conf.write(open(CONF_FOLDER_PATH + "setting.conf", "w"))
        if flag == 1:
            QMessageBox.about(self, 'news', '配置已重置')
            self.close()


if __name__ == "__main__":
    ui_start_time = time()
    app = QApplication(sys.argv)

    # 主界面
    admin_main = AdminMainWindow()
    # 次界面
    login = LoginWindow()
    delete = DeleteWindow()
    unlock = UnloadWindow()
    setting = AdminSettingWindow()

    admin_main.signal_login.connect(login.show)
    admin_main.signal_unlock.connect(unlock.show)
    admin_main.signal_setting.connect(setting.show)
    admin_main.signal_delete.connect(delete.show)

    admin_main.show()

    print('管理费界面 初始化时间:', time() - ui_start_time)

    sys.exit(app.exec_())
