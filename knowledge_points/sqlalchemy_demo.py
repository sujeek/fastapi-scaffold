# -*- coding: utf-8 -*-
"""
@Time ： 2022/6/1 11:43
@Auth ： yongjie.su
@File ：sqlalchemy_demo.py
@IDE ：PyCharm
@Motto：Design Review Coding Test

"""
from typing import List
from pydantic import BaseModel, constr
from sqlalchemy import Column, String, Integer
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class CompanyOrm(Base):
    __tablename__ = 'companies'
    id = Column(Integer, primary_key=True, nullable=False)
    public_key = Column(String(20), index=True, nullable=False, unique=True)
    name = Column(String(63), unique=True)
    domains = Column(ARRAY(String(255)))


class CompanyModel(BaseModel):
    id: int
    public_key: constr(max_length=20)
    name: constr(max_length=63)
    domains: List[constr(max_length=255)]

    class Config:
        orm_mode = True


co_orm = CompanyOrm(
    id=123,
    public_key='foobar',
    name='Testing',
    domains=['example.com', 'foobar.com'],
)

print(CompanyModel.from_orm(co_orm))
