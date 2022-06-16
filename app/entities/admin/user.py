# -*- coding: utf-8 -*-
"""
@Time ： 2022/6/8 20:15
@Auth ： yongjie.su
@File ：user.py
@IDE ：PyCharm
@Motto：Design Review Coding Test

"""
from pydantic import BaseModel, validator, Field, StrictInt, StrictStr


class User(BaseModel):
    user_id: StrictStr
    name: StrictStr
    pwd: StrictStr
    phone: StrictStr
    Ids: StrictStr
    age: StrictInt = 18
    sex: StrictStr
    org_id: StrictInt
    org_name: StrictStr
    email: StrictStr
    remark: StrictStr
    is_delete: StrictInt = 0
