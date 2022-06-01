# -*- coding: utf-8 -*-
"""
@Time ： 2022/6/1 12:51
@Auth ： yongjie.su
@File ：application.py
@IDE ：PyCharm
@Motto：Design Review Coding Test

"""
from fastapi import FastAPI
from knowledge_points.fastapi_demo import demo_app
from app.routers.health import health_app


class Application:
    app = FastAPI(
        title='Service-Framework API Docs',
        version='1.0.0',
        docs_url='/docs',
        redoc_url='/redocs',
    )

    def __init__(self):
        # 注册业务router
        self._init_router()

        # # 注册trace_id
        # self._init_trace_id()
        #
        # # 请求参数校验
        # self._init_middleware()

    def _init_router(self):
        self.app.include_router(demo_app, prefix='/demo_app', tags=['测试Demo'])
        self.app.include_router(health_app, prefix='/health', tags=['健康检查'])

    # def _init_trace_id(self):
    #     from app.middleware.trace_id_middlerware import TraceIdMiddleware
    #     self.app.add_middleware(TraceIdMiddleware)
    #
    # def _init_middleware(self):
    #     from app.middleware.auth_middleware import AuthMiddleware
    #     self.app.add_middleware(AuthMiddleware)


def create_app():
    server_app = Application()
    # 返回fastapi的App对象
    return server_app.app
