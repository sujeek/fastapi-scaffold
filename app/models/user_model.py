# -*- coding: utf-8 -*-
"""
@Time ： 2022/6/9 15:17
@Auth ： yongjie.su
@File ：user_model.py
@IDE ：PyCharm
@Motto：Design Review Coding Test

"""
from pydantic import Field
from sqlalchemy import Column, String, Integer, DateTime, text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Model:
    def to_json(self):
        if hasattr(self, '__table__'):
            return {i.name: getattr(self, i.name) for i in self.__table__.columns}
        raise AssertionError('<%r> does not have attribute for __table__' % self)

    def to_dict(self):
        columns = {}
        columns.update(self.__dict__)
        if "_sa_instance_state" in columns:
            del columns['_sa_instance_state']
        return columns


class UserAdd(Model, Base):
    __tablename__ = 't_user'

    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    pwd = Column(String(32))
    phone = Column(String(20))
    Ids = Column(String(20))
    age = Column(Integer)
    sex = Column(String(20))
    org_id = Column(Integer)
    org_name = Column(String(20))
    email = Column(String(20))
    remark = Column(String(20))
    is_delete = Column(Integer)
    create_time = Column(DateTime)
    update_time = Column(DateTime)
