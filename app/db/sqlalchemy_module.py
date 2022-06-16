# -*- coding: utf-8 -*-
"""
@Time ： 2022/5/31 10:37
@Auth ： yongjie.su
@File ：sqlalchemy_module.py
@IDE ：PyCharm
@Motto：Design Review Coding Test

"""
import traceback
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

from app.config import config
from app.log_module import log
from app.utils.singleton_helper import Singleton
from app.utils.timer_helper import timer


@Singleton
class SqlAlchemyModule:
    def __init__(self, **kwargs):
        _host = kwargs.get('hostname', None)
        _user = kwargs.get('username')
        _password = kwargs.get('password')
        _database = kwargs.get('database')
        _port = kwargs.get('port', 3306)
        self.mysql_url = f"mysql+pymysql://{_user}:{_password}@{_host}:{_port}/{_database}"
        self.session = None

    @timer
    def get_session(self):
        if self.session:
            return self.session
        retry_count = 0
        while retry_count < 3:
            retry_count += 1
            try:
                self.engine = create_engine(self.mysql_url,
                                            encoding='utf-8', echo=True)
                session_factory = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
                self.session = scoped_session(session_factory)
                return self.session
            except Exception as e:
                log.info(f'mysql connect get session is error: {e}')
                traceback.print_exc()
        return None


sqlalchemy_module = SqlAlchemyModule(**config['mysql'])
