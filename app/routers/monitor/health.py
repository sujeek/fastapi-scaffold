# -*- coding: utf-8 -*-
"""
@Time ： 2022/6/1 15:17
@Auth ： yongjie.su
@File ：health.py
@IDE ：PyCharm
@Motto：Design Review Coding Test

"""
from fastapi import APIRouter

router = APIRouter()


@router.get('/health')
async def health():
    return 'ok'


@router.post('/health')
async def health():
    return 'ok'
