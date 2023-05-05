# Su-Face-Recognition
A face recognition for user logining.



1.基本环境
    安全人脸识别系统能够运行在基于PC操作系统Windows环境下，要求Windows操作系统安装Python 3.8 及以上环境，且已安装MySQL数据库系统。

2.库引入
    在PyCharm中打开requirements.txt，按照要求安装对应的包

3.数据库
    要求MySQL数据库中已创建表user、admin、warn表，通过脚本创建。
    （1）首先打开 conf/dataBase.conf 配置文件，修改相应的数据库连接参数
    （2）点击运行 init_tables.py 脚本，自动创建数据库以及表，并插入管理员初始账号密码
    （3）管理员初始账号为"root",密码为"root"

4.运行
    本项目的启动脚本为main.py,点击运行后出现开始界面，选择用户端或者管理员端进行操作。