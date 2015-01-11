#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author : younger shen
# email  : younger.x.shen@gmail.com

from openbook.mixins.handlermixins import DefaultHandler
from openbook.utils.dbutils import get_session

class IndexHandler(DefaultHandler):
    module_name=MODULE_NAME

    def get(self):
        pass

    def post(self):
        pass
