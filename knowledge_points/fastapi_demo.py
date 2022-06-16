# -*- coding: utf-8 -*-
"""
@Time ： 2022/6/1 12:01
@Auth ： yongjie.su
@File ：fastapi_demo.py
@IDE ：PyCharm
@Motto：Design Review Coding Test

"""
from fastapi import APIRouter
from pydantic import BaseModel


class Person(BaseModel):
    age: int
    name: str


router = APIRouter()


@router.post('/v1')
def get_person(version: str, person: Person):
    return {"version": version, "person": person.name}
