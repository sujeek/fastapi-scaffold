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
from starlette.staticfiles import StaticFiles

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

app.mount('/static', StaticFiles(directory=os.path.join(home_path, 'swagger\\static')), name='swagger')

if __name__ == '__main__':
    uvicorn.run(
        workers=2 * cpu_nums,
        app='run:app',
        host='0.0.0.0',
        port=port,
        debug=False,
        reload=True,
    )
