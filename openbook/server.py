#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author : younger shen
# email  : younger.x.shen@gmail.com

import tornado.ioloop
import tornado.web
from settings import settings
from openbook.mixins.Jinja2Mixins import Jinja2AppMixin
from openbook.urls import urls
from openbook.vendor.session.YSession import YSessionManager


class MainApplication(Jinja2AppMixin, tornado.web.Application):
    pass


application = MainApplication(urls,**settings['tornado'])

def main():
    application.listen(9999)
    tornado.ioloop.IOLoop.instance().start()
if __name__ == '__main__':
    main()
