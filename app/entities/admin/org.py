# -*- coding: utf-8 -*-
"""
@Time ： 2022/6/17 10:56
@Auth ： yongjie.su
@File ：org.py
@IDE ：PyCharm
@Motto：Design Review Coding Test

"""
from pydantic import BaseModel, StrictInt, StrictStr


class User(BaseModel):
    org_code: StrictStr
    org_name: StrictStr
    parent_id: StrictInt
    is_delete: StrictInt = 0
    remark: StrictStr
