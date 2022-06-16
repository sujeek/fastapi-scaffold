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
from typing import List
from fastapi import APIRouter, Query
from sqlalchemy import select
from tortoise.queryset import F

from app.db.dao.sqlalchemy_dao import SqlAlchemyDao
from app.db.dao.mysql_dao import MysqlDao
from app.entities.admin.user import User
from app.models.user_model import UserAdd, UserUpdate
from app.core.response import ApiResponse
from app.core.exception_enum import ErrorEnum
from app.log_module import log
from app.utils.util import get_md5_value

router = APIRouter()
sqlalchemy_dao = SqlAlchemyDao()
mysql_dao = MysqlDao()


@router.post('/insert_or_update')
async def add_user(user: User):
    now = datetime.datetime.now()
    user_id = user.user_id
    pwd = get_md5_value(user.pwd)
    user_add = UserAdd(
        user_id=user_id,
        name=user.name,
        pwd=pwd,
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
    try:
        if user_id is None:
            log.error(f'user_id is none, please add user_id.')
            return ApiResponse(ErrorEnum.UserIdIsNull.code, ErrorEnum.UserIdIsNull.message, {})
        res = sqlalchemy_dao.session.execute(select(UserAdd).filter_by(user_id=user_id)).first()
        if res is None:
            # 不存在则直接插入
            log.info(f'user_id is not exists, exec add.')
            sqlalchemy_dao.session.add(user_add)
        else:
            # 若存在，则更新
            log.info(f'user_id is exists, exec update.')
            data = user_add.to_dict()
            data['id'] = res[0].id
            sqlalchemy_dao.session.query(UserUpdate).filter(UserUpdate.user_id == user_id).update(data)
        return ApiResponse(ErrorEnum.Success.code, ErrorEnum.Success.message, user.json())
    except Exception as e:
        log.error(e)
        traceback.print_exc()
        return ApiResponse(ErrorEnum.Faild.code, ErrorEnum.Faild.message, {})
    finally:
        sqlalchemy_dao.session.commit()
        sqlalchemy_dao.session.close()


@router.post('/find_by_id')
async def query(id: int):
    try:
        user = sqlalchemy_dao.session.get(UserAdd, id)
        return ApiResponse(ErrorEnum.Success.code, ErrorEnum.Success.message, user)
    except Exception as e:
        log.error(e)
        traceback.print_exc()
        return ApiResponse(ErrorEnum.Faild.code, ErrorEnum.Faild.message, {})
    finally:
        sqlalchemy_dao.session.commit()
        sqlalchemy_dao.session.close()


@router.post('/query_by_user_id')
async def query(user_id: str):
    try:
        query = {"user_id": user_id, "is_delete": 0}
        user = sqlalchemy_dao.session.execute(select(UserAdd).filter_by(**query)).first()
        data = user[0].to_json() if user is not None else {}
        return ApiResponse(ErrorEnum.Success.code, ErrorEnum.Success.message, data)
    except Exception as e:
        log.error(e)
        traceback.print_exc()
        return ApiResponse(ErrorEnum.Faild.code, ErrorEnum.Faild.message, {})
    finally:
        sqlalchemy_dao.session.commit()
        sqlalchemy_dao.session.close()


@router.post('/query_by_page')
async def query(
        page_size: int = 10,
        current: int = 1,
        name: str = Query(None),
        org_name: str = Query(None)):
    # 查询条件, 目前缺失时间范围的查询
    query = {'is_delete': 0}
    if name:
        query['name'] = name
    if org_name:
        query['org_name'] = org_name
    log.info(f'query params is: {query}')
    try:
        offset = page_size * (current - 1)
        users = sqlalchemy_dao.session.execute(
            select(UserAdd).filter_by(**query).offset(offset).limit(page_size)).all()
        data = [user[0].to_json() for user in users]
        return ApiResponse(ErrorEnum.Success.code, ErrorEnum.Success.message, data)
    except Exception as e:
        log.error(e)
        traceback.print_exc()
        return ApiResponse(ErrorEnum.Faild.code, ErrorEnum.Faild.message, {})
    finally:
        sqlalchemy_dao.close()


@router.post('/delete_by_user_id')
async def delete(user_id: str):
    try:
        sqlalchemy_dao.session.query(UserUpdate).filter(UserUpdate.user_id == user_id).update({"is_delete": 1})
        return ApiResponse(ErrorEnum.Success.code, ErrorEnum.Success.message, user_id)
    except Exception as e:
        log.error(e)
        traceback.print_exc()
        return ApiResponse(ErrorEnum.Faild.code, ErrorEnum.Faild.message, {})
    finally:
        sqlalchemy_dao.session.commit()
        sqlalchemy_dao.session.close()
