# -*- coding: utf-8 -*-
"""
@Time ： 2022/6/16 10:18
@Auth ： yongjie.su
@File ：mysql_pool_module.py
@IDE ：PyCharm
@Motto：Design Review Coding Test

"""
import time
import pymysql
from dbutils.pooled_db import PooledDB
from app.utils.singleton_helper import Singleton
from app.log_module import log
from app.config import config


@Singleton
class MysqlPoolModule:
    def __init__(self, **kwargs):
        self._db_args = {
            'host': kwargs.get('hostname', 'localhost'),
            'user': kwargs.get('username'),
            'password': kwargs.get('password'),
            'database': kwargs.get('database'),
            'port': kwargs.get('port', 3306)
        }
        self.conn = None
        self.cursor = None
        self._pool = None

    def get_db_connect(self):
        if self._pool:
            self.conn = self._pool.connection()
            self.cursor = self.conn.cursor()
            return self.conn, self.cursor

        retry_count = 0
        while retry_count < 3:
            retry_count += 1
            t = time.perf_counter()
            try:
                self._pool = PooledDB(
                    creator=pymysql,
                    maxconnections=5,
                    mincached=2,
                    maxcached=5,
                    charset='utf8',
                    **self._db_args
                )
                log.info(f'get_db_connect_success, cost time={(time.perf_counter() - t) * 1000}ms, {retry_count=}')
                self.conn = self._pool.connection()
                self.cursor = self.conn.cursor()
                return self.conn, self.cursor
            except Exception as e:
                log.error(f"connect {self._db_args['database']} is failed. {retry_count=}, {e}")
                log.info(f'get_db_connect_error, cost time={(time.perf_counter() - t) * 1000}ms')
        return None, None

    def close_connect(self):
        self.cursor.close()
        self.conn.close()


mysql_pool_module = MysqlPoolModule(**config['mysql'])
