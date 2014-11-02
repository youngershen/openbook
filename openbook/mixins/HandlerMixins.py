#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author : younger shen
# email  : younger.x.shen@gmail.com

import cjson
from tornado.web import RequestHandler
from openbook.mixins.Jinja2Mixins import Jinja2HandlerMixin

class JsonHandlerMixin(object):
    
    def return_to_json(context):
        json = cjson.encode(context)
        self.write(json)

class DefaultHandler(Jinja2HandlerMixin, RequestHandler):
    pass
