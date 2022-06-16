# -*- coding: utf-8 -*-
"""
@Time ： 2022/6/1 12:15
@Auth ： yongjie.su
@File ：log_module.py
@IDE ：PyCharm
@Motto：Design Review Coding Test

参考：https://github.com/Delgan/loguru
"""
from loguru import logger as info_logger
from loguru import logger as error_logger
from loguru import logger as access_logger

from app.utils import util


class Logger:
    def __init__(self):
        home_path = util.get_home_dir()
        format = "{time:YYYY-MM-DD HH:mm:ss,SSS} [{thread}] {level} {file} {line} - {message}"
        # 普通logger
        info_logger.add(home_path + '/logs/info.log.{time:YYYY-MM-DD HH}.log', format=format,
                        level='INFO', rotation='1 h')
        # info_logger.remove()
        error_logger.add(home_path + '/logs/error.log.{time:YYYY-MM-DD HH}.log', format=format,
                         level='ERROR', rotation='1 h')
        # error_logger.remove()
        # access log 使用和tornado相同的logger name,主动指定log的文件地址
        access_logger.add(home_path + '/logs/access.log.{time:YYYY-MM-DD HH}.log', format=format,
                          level='INFO', rotation='1 h')
        # access_logger.remove()

    def debug(self, msg):
        info_logger.debug(msg)
        return

    def info(self, msg):
        info_logger.info(msg)

    def fatal(self, msg):
        info_logger.info(msg)
        error_logger.error(msg)

    def error(self, msg):
        info_logger.info(msg)
        error_logger.error(msg)

    def warning(self, msg):
        info_logger.info(msg)
        info_logger.warning(msg)


log = Logger()
