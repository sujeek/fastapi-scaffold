# -*- coding: utf-8 -*-
"""
@Time ： 2022/6/1 12:51
@Auth ： yongjie.su
@File ：application.py
@IDE ：PyCharm
@Motto：Design Review Coding Test

"""
import os

from fastapi import FastAPI
from starlette.staticfiles import StaticFiles

from knowledge_points import fastapi_demo
from app.routers import health
from app.routers.admin import user, role, access, org
from app.core import event
from app.utils import util


class Application:
    app = FastAPI(
        title='Service-Framework API Docs',
        version='1.0.0',
        docs_url=None,
        redoc_url=None,
    )

    def __init__(self):
        self.home_path = util.get_home_dir()

        self._init_event()
        # 注册业务router
        self._init_router()

        #
        self._init_middleware()

        #
        self._init_mount()

    def _init_event(self):
        self.app.add_event_handler("startup", event.startup(self.app))
        self.app.add_event_handler("shutdown", event.shutdown(self.app))

    # 注册 router
    def _init_router(self):
        self.app.include_router(fastapi_demo.router, prefix='/test', tags=['测试Demo'])
        self.app.include_router(health.router, prefix='/health', tags=['健康检查'])
        self.app.include_router(user.router, prefix='/admin', tags=['用户管理'])
        self.app.include_router(role.router, prefix='/role', tags=['角色管理'])
        self.app.include_router(access.router, prefix='/access', tags=['权限管理'])
        self.app.include_router(org.router, prefix='/org', tags=['组织单位'])

    def _init_middleware(self):
        pass

    # 初始化挂载
    def _init_mount(self):
        self.app.mount('/static', StaticFiles(directory=os.path.join(self.home_path, 'static')), name='static')


def create_app():
    server_app = Application()
    # 返回fastapi的App对象
    return server_app.app
