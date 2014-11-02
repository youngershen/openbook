#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author : younger shen
# email  : younger.x.shen@gmail.com

import tornado.ioloop
import tornado.web
from settings import settings
from openbook.mixins.Jinja2Mixins import Jinja2AppMixin
from openbook.mixins.Jinja2Mixins import Jinja2HandlerMixin

class MainApplication(Jinja2AppMixin, tornado.web.Application):
    pass

class MainHandler(Jinja2HandlerMixin, tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get(self):
        self.render_to_response("index.html", **dict())
        self.finish()

application = MainApplication(
        [(r"/", MainHandler),],
        **settings['tornado'])

def main():
    application.listen(9999)
    tornado.ioloop.IOLoop.instance().start()
if __name__ == '__main__':
    main()
