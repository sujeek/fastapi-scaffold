# -*- coding: utf-8 -*-
"""
@Time ： 2022/6/24 15:15
@Auth ： yongjie.su
@File ：test_redis_bigkey.py
@IDE ：PyCharm
@Motto：Design Review Coding Test

"""
import random
from app.db.redis_module import redis_client

if __name__ == '__main__':
    redis_client.subscribe('channel')
