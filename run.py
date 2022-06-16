# -*- coding: utf-8 -*-
"""
@Time ： 2022/6/1 11:51
@Auth ： yongjie.su
@File ：run.py
@IDE ：PyCharm
@Motto：Design Review Coding Test

"""
import os
import uvicorn
from fastapi.openapi.docs import get_redoc_html, get_swagger_ui_html

from app.config import config
from app.utils import util
from app.log_module import log
from app.application import create_app

app = create_app()

port = config.get('port', 8088)
log.info(f'The server port is: {port=}')

cpu_nums = os.cpu_count()

home_path = util.get_home_dir()
util.mkdirs(home_path + '/logs')
util.mkdirs(home_path + '/data/requests')


@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title=app.title,
        oauth2_redirect_url=app.swagger_ui_oauth2_redirect_url,
        swagger_js_url="/static/swagger-ui-bundle.js",
        swagger_css_url="/static/swagger-ui.css",
    )


@app.get("/redocs", include_in_schema=False)
async def redoc_html():
    return get_redoc_html(
        openapi_url=app.openapi_url,
        title=app.title,
        redoc_js_url="/static/redoc.standalone.js",
    )


if __name__ == '__main__':
    uvicorn.run(
        workers=2 * cpu_nums,
        app='run:app',
        host='0.0.0.0',
        port=port,
        debug=False,
        reload=True,
    )
