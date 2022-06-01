# -*- coding: utf-8 -*-
"""
@Time ： 2022/6/1 11:17
@Auth ： yongjie.su
@File ：pydantic_demo.py
@IDE ：PyCharm
@Motto：Design Review Coding Test

"""
import json
from pathlib import Path
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime


class UserInfo(BaseModel):
    id: int
    name: str
    age: int
    sex: str
    labels: List[str] = []


mock_data = {
    'id': 1,
    'name': 'lilei',
    'age': 18,
    'sex': 'man',
    'labels': ['music', 'movie']
}

user = UserInfo(**mock_data)
print(user.json())
print(user.dict())
# 还可以从文件中读取
print(UserInfo.parse_file(Path('pydantic_tutorial.json')))
print(UserInfo.parse_raw(json.dumps(mock_data)))
print(UserInfo.parse_obj(mock_data))


# pydantic 嵌套

class Animal(BaseModel):
    foot: int


class Dog(BaseModel):
    birthday: datetime
    foot: Animal


dog = Dog(birthday=datetime.now(), foot=Animal(foot=4))
print(dog.birthday, dog.foot)

