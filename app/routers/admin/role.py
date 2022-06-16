# -*- coding: utf-8 -*-
"""
@Time ： 2022/6/1 23:21
@Auth ： yongjie.su
@File ：role.py
@IDE ：PyCharm
@Motto：Design Review Coding Test

"""
from fastapi import APIRouter, Query

router = APIRouter()


@router.post('/insert_or_update')
async def add_user(user: str):
    pass


@router.post('/find_by_id')
async def query(id: int):
    pass


@router.post('/query_by_page')
async def query(
        page_size: int = 10,
        current: int = 1,
        name: str = Query(None),
        org_name: str = Query(None)):
    pass

@router.post('/delete_by_user_id')
async def delete(user_id: str):
    pass