# 人脸识别系统
用于用户登录的安全人脸识别系统，实现人脸识别、活体检测、背景模糊、姿态检测、人脸比对等功能

## 上手指南
    实现的功能包括
        人脸识别、活体检测（静默+交互）、背景模糊、姿态检测、人脸比对
        用户登录登出注册操作、管理员相关操作
    使用包括Face_Recognition、dlib、OpenCV、MediaPipe、PyQt等开源库

## 安装要求
    安全人脸识别系统能够运行在基于PC操作系统Windows环境下，
    要求Windows操作系统安装Python 3.8 及以上环境，且已安装MySQL数据库系统。

## 安装步骤<br>
### 1.相关库安装
    在PyCharm中打开requirements.txt，按照要求安装对应的包。

### 2.创建数据库
    系统运行要求 MySQL 数据库中已创建表user、admin、warn表，初始通过脚本进行创建：
    （1）首先打开 conf/dataBase.conf 配置文件，修改相应的数据库连接参数；
    （2）点击运行 init.py 脚本，自动创建数据库以及表，并插入管理员初始账号密码；
    （3）管理员初始账号为"root",密码为"root"。

## 运行
    本项目的启动脚本为main.py,点击运行后出现开始界面，选择用户端或者管理员端进行操作。

![image](https://github.com/Usernamesisnotavailable/Su-Face-Recognition/blob/master/Logo.jpg)
