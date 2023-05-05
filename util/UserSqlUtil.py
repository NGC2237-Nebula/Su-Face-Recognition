# -*- coding: utf-8 -*-
import pymysql


def init_conn():
    conn = pymysql.connect(
        host="127.0.0.1",  # 数据库的IP地址
        user="root",  # 数据库用户名称
        password="root",  # 数据库用户密码
        db="contest",  # 数据库名称
        port=3306,  # 数据库端口名称
        charset="utf8"  # 数据库的编码方式
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


def execute_with_list(sql_str):
    conn = init_conn()
    cursor = conn.cursor()
    results = []
    try:
        cursor.execute(sql_str)
        results = cursor.fetchall()
    except Exception as e:
        conn.rollback()
        print(e)
    finally:
        cursor.close()
    return results


def insert_data(name, password, age, sex, more, face_encoding):
    return execute_with_bool(
        "insert into user(name,password,age,sex,more,face_encoding) values(%s,%s,%s,%s,%s,%s)",
        (name, password, age, sex, more, face_encoding))


def update_by_name(name, password, age, sex, more, face_encoding):
    return execute_with_bool(
        "update user set name=%s,password=%s,age=%s,sex=%s,more=%s,face_encoding=%s where name = %s",
        (name, password, age, sex, more, face_encoding, name))


def update_by_name_without_encoding(name, age, sex, more):
    return execute_with_bool("update user set name=%s,age=%s,sex=%s,more=%s where name = %s",
                             (name, age, sex, more, name))


def search_all_msg():
    return execute_with_list("select * from user")


def search_by_name(name):
    return execute_with_list("select * from user where name = " + name)


def search_count_name(name):
    return execute_with_list("select count(*) from user where name = " + name)[0][0]


def delete_by_name(name):
    return execute_with_bool("delete from user where name = %s", name)


def search_count_warn(name):
    return execute_with_list("select count(*) from warn where name = " + name)[0][0]


def add_name_warn(name):
    return execute_with_bool("insert into warn(name) values(%s)", name)
