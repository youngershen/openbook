#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author : younger shen
# email  : younger.x.shen@gmail.com

import tornado.ioloop
import tornado.web

from settings.settings import settings

from openbook.mixins.jinja2mixins import Jinja2AppMixin
from openbook.urls import urls
from openbook.vendor.session.ysession import YSessionManager

settings['SESSION']['MANAGER'] = YSessionManager(settings)

class MainApplication(Jinja2AppMixin, tornado.web.Application):
    pass


application = MainApplication(urls,**settings['tornado'])

def main():
    application.listen(9999)
    tornado.ioloop.IOLoop.instance().start()
if __name__ == '__main__':
    main()
