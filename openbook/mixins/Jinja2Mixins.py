#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author : younger shen
# email  : younger.x.shen@gmail.com
import sys
from jinja2 import Environment
from openbook.settings import settings
from tornado import escape

class Jinja2AppMixin(object):
    def __init__(self, *args, **kwargs):
        super(Jinja2AppMixin, self).__init__(*args, **kwargs)
        self.jinja2_env = Environment(**settings['JINJA2']) 


class TemplateLocateMixin(object):
    def get_module_template(self, template_name):
        if self.module_name:
            return self.module_name + "/" + template_name
        else:
            return template_name

class Jinja2HandlerMixin(object):
    def render_to_response(self, template_name, context):
        default_context = {
            'handler': self,
            'request': self.request,
            'current_user': self.current_user,
            'static_url': self.static_url,
            'xsrf_form_html': self.xsrf_form_html,
            'reverse_url': self.reverse_url,
        }
        escape_context = {
            'escape': escape.xhtml_escape,
            'xhtml_escape': escape.xhtml_escape,
            'url_escape': escape.url_escape,
            'json_encode': escape.json_encode,
            'squeeze': escape.squeeze,
            'linkify': escape.linkify,
        }
        context.update(default_context)
        context.update(escape_context)
        context.update(self.ui) 
        
        template_full_name = self.get_module_template(template_name)
        template = self.application.jinja2_env.get_template(
            template_full_name)
        html = template.render(**context)
        self.write(html)
