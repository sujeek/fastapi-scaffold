# -*- coding: utf-8 -*-
"""
@Time ： 2022/6/2 10:11
@Auth ： yongjie.su
@File ：event.py
@IDE ：PyCharm
@Motto：Design Review Coding Test

"""
from typing import Callable
from fastapi import FastAPI
from app.log_module import log


def startup(app: FastAPI) -> Callable:
    """
    FastApi 启动完成事件
    :param app: FastAPI
    :return: start_app
    """

    async def app_start() -> None:
        # APP启动完成后触发
        log.info("fastapi已启动")

    return app_start


def shutdown(app: FastAPI) -> Callable:
    """
    FastApi 停止事件
    :param app: FastAPI
    :return: stop_app
    """

    async def stop_app() -> None:
        # APP停止时触发
        log.info("fastapi已停止")

    return stop_app
