##author kevingao

import logging; logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time
from datetime import datetime

from aiohttp import web

#此处很重要 body=b'<h1>Awesome</h1>',content_type='text/html', charset='UTF-8'
def index(request):
    return web.Response(body=b'<h1>Awesome</h1>',content_type='text/html', charset='UTF-8')

@asyncio.coroutine
def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    srv = yield from loop.create_server(app.make_handler(),'127.0.0.1',9000)   
    logging.info('server started at http://127.0.0.1:9000...')
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
