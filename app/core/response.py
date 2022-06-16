# -*- coding: utf-8 -*-
"""
@Time ： 2022/6/9 17:46
@Auth ： yongjie.su
@File ：response.py
@IDE ：PyCharm
@Motto：Design Review Coding Test

"""
import time
from fastapi import status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder


class ApiResponse(JSONResponse):
    # 默认其实都是200可以不写
    http_status_code = status.HTTP_200_OK
    code = 0
    message = "success"
    timestamp = int(time.time() * 1000)

    def __init__(self, code, message, data, **kwargs):
        self.code = code
        self.message = message
        self.data = data

        body = dict(
            code=self.code,
            message=self.message,
            timestamp=self.timestamp,
            data=self.data
        )

        super(ApiResponse, self).__init__(status_code=self.http_status_code, content=jsonable_encoder(body),
                                          **kwargs)
