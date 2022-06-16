# -*- coding: utf-8 -*-
"""
@Time ： 2022/6/9 18:51
@Auth ： yongjie.su
@File ：exception_enum.py
@IDE ：PyCharm
@Motto：Design Review Coding Test

"""
from enum import Enum


class ErrorEnum(Enum):
    Success = 0, 'success'
    Faild = -1, 'faild'

    def __init__(self, code, message):
        self.code = code
        self.message = message

    def json(self):
        return {'code': self.code, 'message': self.message}
