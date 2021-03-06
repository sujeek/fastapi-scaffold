# -*- coding: utf-8 -*-
"""
@Time ： 2022/6/1 12:33
@Auth ： yongjie.su
@File ：util.py
@IDE ：PyCharm
@Motto：Design Review Coding Test

"""
import os
import hashlib

CURRENT_PATH = os.path.realpath(__file__)


def get_home_dir():
    path = CURRENT_PATH
    for _ in range(2):
        path = os.path.dirname(path)
    return path


def mkdirs(dirs):
    if not os.path.exists(dirs):
        os.makedirs(dirs)


def get_md5_value(msg: str):
    return hashlib.md5(msg.encode('utf-8')).hexdigest()
