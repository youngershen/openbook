#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author : younger shen
# email  : younger.x.shen@gmail.com

import tornado.ioloop
import tornado.web
from settings import settings
from mixins import Jinja2AppMixin

class MainApplication(Jinja2AppMixin, tornado.web.Application):
    pass

class MainHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get(self):
        self.write("hello world!")
        name = self.get_argument("name")
        self.write("</br> my name is  {name}".format(name=name))
        self.finish()

application = MainApplication([
    (r"/", MainHandler),
    ], **settings)

def main():
    application.listen(9999)
    tornado.ioloop.IOLoop.instance().start()
if __name__ == '__main__':
    main()
