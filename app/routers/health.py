# -*- coding: utf-8 -*-
"""
@Time ： 2022/6/1 15:17
@Auth ： yongjie.su
@File ：health.py
@IDE ：PyCharm
@Motto：Design Review Coding Test

"""
from fastapi import APIRouter

health_app = APIRouter()


@health_app.get('/')
async def health():
    return 'ok'
