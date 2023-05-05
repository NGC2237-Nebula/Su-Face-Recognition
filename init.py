# -*- coding: utf-8 -*-
import pymysql
import configparser

conf = configparser.ConfigParser()
conf.read('conf/dataBase.conf', encoding='gbk')
host = conf.get("mysql", 'host')
user = conf.get("mysql", 'user')
password = conf.get("mysql", 'password')
db = conf.get("mysql", 'db')
port = int(conf.get("mysql", 'port'))
charset = conf.get("mysql", 'charset')


def init_conn():
    conn = pymysql.connect(
        host=host,  # 数据库的IP地址
        user=user,  # 数据库用户名称
        password=password,  # 数据库用户密码
        db=db,  # 数据库名称
        port=port,  # 数据库端口名称
        charset=charset  # 数据库的编码方式
    )
    return conn


def execute_with_bool(sql_str, args=()):
    conn = init_conn()
    cursor = conn.cursor()
    try:
        cursor.execute(sql_str, args)
        conn.commit()
        return True
    except Exception as e:
        conn.rollback()
        print(e)
        return False
    finally:
        cursor.close()


def create_table_data():
    return execute_with_bool('''
        CREATE TABLE IF NOT EXISTS `''' + db + '''`.`user`  (
      `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
      `password` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
      `age` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
      `sex` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
      `more` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
      `face_encoding` varchar(4096) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL
    ) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;
''')


def create_table_warn():
    return execute_with_bool('''
    CREATE TABLE IF NOT EXISTS`''' + db + '''`.`warn`  (
    `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL
    ) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;
''')


def create_table_admin():
    return execute_with_bool('''
        CREATE TABLE IF NOT EXISTS `''' + db + '''`.`admin`  (
        `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
        `password` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
        PRIMARY KEY (`name`) USING BTREE
        ) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;
''')


def insert_data(name, password):
    return execute_with_bool(
        "insert into admin(name,password) values(%s,%s)", (name, password))


if __name__ == '__main__':
    create_table_data()
    create_table_admin()
    create_table_warn()
    insert_data('root', 'root')
