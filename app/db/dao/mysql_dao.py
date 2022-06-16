# -*- coding: utf-8 -*-
"""
@Time ： 2022/6/16 10:23
@Auth ： yongjie.su
@File ：mysql_dao.py
@IDE ：PyCharm
@Motto：Design Review Coding Test

"""
from app.db.mysql_pool_module import mysql_pool_module
from app.log_module import log


class MysqlDao:
    def __int__(self):
        self.mysql_pool = mysql_pool_module

    # 单条插入
    def insert_by_single(self, sql):
        conn, cursor = self.mysql_pool.get_db_connect()
        try:
            cursor.execute(sql)
            conn.commit()
        except Exception as e:
            # 发生错误时回滚
            log.error(e)
            conn.rollback()
        finally:
            conn.close()
            cursor.close()

    # 批量插入 demo
    # sql = "INSERT INTO EMPLOYEE(FIRST_NAME,LAST_NAME, AGE, SEX, INCOME) VALUES (%s,%s,%s,%s,%s)"
    # val = (('li', 'si', 16, 'F', 1000),('Bruse', 'Jerry', 30, 'F', 3000))
    def insert_by_batch(self, sql, values):
        conn, cursor = self.mysql_pool.get_db_connect()
        try:
            cursor.executemany(sql, values)
            conn.commit()
        except Exception as e:
            # 发生错误时回滚
            log.error(e)
            conn.rollback()
        finally:
            conn.close()
            cursor.close()

    # 使用fetchone()方法获取单条记录
    def select_by_fetchone(self, sql):
        conn, cursor = self.mysql_pool.get_db_connect()
        try:
            cursor.execute(sql)
            data = cursor.fetchone()
            return data
        except Exception as e:
            log.error(e)
            # 发生错误时回滚
            conn.rollback()
        finally:
            conn.close()
            cursor.close()

    # 使用fetchall()方法从数据库表中获取多个值。
    def select_by_fetchall(self, sql):
        conn, cursor = self.mysql_pool.get_db_connect()
        try:
            cursor.execute(sql)
            data = cursor.fetchall()
            return data
        except Exception as e:
            log.error(e)
            # 发生错误时回滚
            conn.rollback()
        finally:
            conn.close()
            cursor.close()
