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


def search_by_name(name):
    return execute_with_list("select * from admin where name = " + name)


def delete_by_name(name):
    return execute_with_bool("delete from warn where name = %s", name)
