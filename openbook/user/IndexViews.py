#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author : younger shen
# email  : younger.x.shen@gmail.com

from openbook.mixins.HandlerMixins import DefaultHandler

class UserIndexHandler(DefaultHandler):
    
    def get(self):
        self.render_to_response("index.html" , dict())
