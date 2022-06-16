# -*- coding: utf-8 -*-
"""
@Time ： 2022/5/26 10:04
@Auth ： yongjie.su
@File ：timer_helper.py
@IDE ：PyCharm
@Motto：Design Review Coding Test

"""
import time
from app.log_module import log


def timer(function):
    """
    对函数进行耗时监控
    :param function:
    :return:
    """

    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = function(*args, **kwargs)
        # 耗时显示为毫秒保留两位小数
        cost = round((time.perf_counter() - start_time) * 1000, 2)
        log.info(f'[function={function.__name__}] - [time={cost}ms]')
        return result

    return wrapper
