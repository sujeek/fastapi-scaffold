# -*- coding: utf-8 -*-
"""
@Time ： 2022/5/25 15:14
@Auth ： yongjie.su
@File ：singleton_helper.py
@IDE ：PyCharm
@Motto：Design Review Coding Test

"""
import threading


def Singleton(cls):
    _instance = {}

    def _singleton(*args, **kargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kargs)
        return _instance[cls]

    return _singleton


class SingletonType(type):
    _instance_lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            with SingletonType._instance_lock:
                if not hasattr(cls, "_instance"):
                    cls._instance = super(SingletonType, cls).__call__(*args, **kwargs)
        return cls._instance
