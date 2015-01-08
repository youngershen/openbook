#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author : younger shen
# email  : younger.x.shen@gmail.com

import cjson
from tornado.web import RequestHandler
from openbook.mixins.jinja2mixins import Jinja2HandlerMixin
from openbook.mixins.jinja2mixins import TemplateLocateMixin
from openbook.settings.settings import settings

manager = settings['SESSION']['MANAGER'](settings)

class JsonHandlerMixin(object):
    def return_to_json(self, context):
        json = cjson.encode(context)
        self.set_header('Content-Type', 'application/json')
        self.write(json)


class SessionHandlerMixin(object):
    def session(self):
        session_id = self.get_cookie('session_id')
        if session_id is None:
            session_id = manager.get_session()
            self.set_cookie('session_id', session_id)
            return session_id
        else:
            return session_id

    def session_add(self, key, value):
        session_id = self.session()
        manager.session_add(session_id, key, value)
    
    def session_get(self, key):
        session_id = self.session()
        return manager.session_get(session_id, key)


class RESTHandler(JsonHandlerMixin, RequestHandler):
    pass
    
class DefaultHandler(SessionHandlerMixin, TemplateLocateMixin, JsonHandlerMixin, Jinja2HandlerMixin, RequestHandler):
    pass


