#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author : younger shen
# email  : younger.x.shen@gmail.com

import tornado.ioloop
import tornado.web

from settings.settings import settings

from openbook.core.mixins.jinja2mixins import Jinja2AppMixin
from openbook.urls import urls

class MainApplication(Jinja2AppMixin, tornado.web.Application):
    pass


application = MainApplication(urls,**settings['tornado'])

def main():
    application.listen(settings['tornado']['port'])
    tornado.ioloop.IOLoop.instance().start()
if __name__ == '__main__':
    main()
