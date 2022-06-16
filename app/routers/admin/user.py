# -*- coding: utf-8 -*-
"""
@Time ： 2022/6/1 23:21
@Auth ： yongjie.su
@File ：user.py
@IDE ：PyCharm
@Motto：Design Review Coding Test

"""
import datetime
import traceback
from fastapi import APIRouter
from sqlalchemy import select

from app.db.sqlalchemy_dao import SqlAlchemyDao
from app.entities.admin.user import User
from app.models.user_model import UserAdd
from app.core.response import ApiResponse
from app.core.exception_enum import ErrorEnum
from app.log_module import log

router = APIRouter()
session = SqlAlchemyDao()


@router.post('/add')
async def add_user(user: User):
    now = datetime.datetime.now()
    user_add = UserAdd(
        name=user.name,
        pwd=user.pwd,
        phone=user.phone,
        Ids=user.Ids,
        age=user.age,
        sex=user.sex,
        org_id=user.org_id,
        org_name=user.org_name,
        email=user.email,
        remark=user.remark,
        is_delete=user.is_delete,
        create_time=now,
        update_time=now
    )
    # 严谨的做法先判断是否存在，然后再插入
    try:
        session.insert(user_add)
        return ApiResponse(ErrorEnum.Success.code, ErrorEnum.Success.message, user.json())
    except Exception as e:
        log.error(e)
        traceback.print_exc()
        return ApiResponse(ErrorEnum.Faild.code, ErrorEnum.Faild.message, {})


@router.post('/find_by_id')
async def query(id: int):
    try:
        user = session.get_by_id(UserAdd, id)
        return ApiResponse(ErrorEnum.Success.code, ErrorEnum.Success.message, user)
    except Exception as e:
        log.error(e)
        traceback.print_exc()
        return ApiResponse(ErrorEnum.Faild.code, ErrorEnum.Faild.message, {})
    finally:
        session.close()


@router.post('/query_by_id')
async def query(num: int):
    # 严谨的做法先判断是否存在，然后再插入
    try:
        user = session.session.execute(select(UserAdd).filter_by(id=num)).first()
        data = user[0].to_json() if user is not None else {}
        return ApiResponse(ErrorEnum.Success.code, ErrorEnum.Success.message, data)
    except Exception as e:
        log.error(e)
        traceback.print_exc()
        return ApiResponse(ErrorEnum.Faild.code, ErrorEnum.Faild.message, {})
    finally:
        session.close()


@router.post('/query')
async def query(num: int):
    # 严谨的做法先判断是否存在，然后再插入
    try:
        user = session.session.execute(select(UserAdd).filter_by(id=num)).first()
        data = user[0].to_json() if user is not None else {}
        return ApiResponse(ErrorEnum.Success.code, ErrorEnum.Success.message, data)
    except Exception as e:
        log.error(e)
        traceback.print_exc()
        return ApiResponse(ErrorEnum.Faild.code, ErrorEnum.Faild.message, {})
    finally:
        session.close()


@router.post('/update')
async def update(name: str):
    try:
        user = session.session.execute(update(UserAdd).where(id=num)).first()
        data = user[0].to_json() if user is not None else {}
        return ApiResponse(ErrorEnum.Success.code, ErrorEnum.Success.message, data)
    except Exception as e:
        log.error(e)
        traceback.print_exc()
        return ApiResponse(ErrorEnum.Faild.code, ErrorEnum.Faild.message, {})
    finally:
        session.close()
    return 1


@router.post('/delete')
async def delete(name: str):
    print(name)
    return 1
