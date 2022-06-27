# -*- coding: utf-8 -*-
"""
@Time ： 2022/6/27 11:44
@Auth ： yongjie.su
@File ：redis_dao.py
@IDE ：PyCharm
@Motto：Design Review Coding Test

"""
import time

from app.db.redis_module import redis_client

if __name__ == '__main__':
    while True:
        time.sleep(2)
        redis_client.subscribe('channel')
        response = redis_client.pub_sub.parse_response()
        if b'message' in response:
            print(response)
