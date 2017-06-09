import time

import tornado.web
from tornado import gen
from tornado.ioloop import IOLoop
from tornado.options import define  # options are required for tornado cli args parsing

define("port", default=None, help="Port for tornado application to listen on", type=int)


@gen.coroutine
def async_sleep(seconds):
    yield gen.Task(IOLoop.instance().add_timeout, time.time() + seconds)


def build_app():
    from project.tornado_app import urlpatterns

    application = tornado.web.Application(urlpatterns, autoreload=True)
    return application


def run(port=None):
    from django.conf import settings

    if port is None:
        port = settings.TORNADO_APP_PORT
    app = build_app()
    app.listen(
        port,
        address=settings.TORNADO_APP_ADDRESS
    )
    IOLoop.instance().start()
