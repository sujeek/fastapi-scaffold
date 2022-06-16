# -*- coding: utf-8 -*-
"""
@Time ： 2022/6/9 14:30
@Auth ： yongjie.su
@File ：sqlalchemy_dao.py
@IDE ：PyCharm
@Motto：Design Review Coding Test

"""
import sqlalchemy
from typing import TypeVar, Optional, List
from app.db.sqlalchemy_module import sqlalchemy_module

from app.log_module import log

T = TypeVar("T")


class SqlAlchemyDao:
    def __init__(self):
        self.session = sqlalchemy_module.get_session()

    def insert(self, obj) -> T:
        """
        插入单条数据
        :param obj:
        :return:
        """
        try:
            self.session.add(obj)
        except Exception as e:
            log.error(e)
        finally:
            self.commit()
        return obj

    def bulk_insert(self, objs) -> List[T]:
        """
        批量插入数据
        :param objs:
        :return:
        """
        try:
            self.session.bulk_save_objects(objs)
        except Exception as e:
            log.error(e)
        finally:
            self.commit()
        return objs

    def get_by_id(self, clz: T, id: int) -> Optional[T]:
        """
        根据id查询
        :param clz:
        :param id:
        :return:
        """
        try:
            obj = self.session.get(clz, id)
        except Exception as e:
            log.error(e)
            obj = None
        return obj

    def bulk_get_by_ids(self, clz: T, ids: List[int]) -> List[T]:
        return (
            self.session.execute(sqlalchemy.select(clz).where(clz.id.in_(ids))).scalars().all()
        )

    def commit(self):
        try:
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            log.error(e)
            raise

    def close(self):
        self.session.close()
