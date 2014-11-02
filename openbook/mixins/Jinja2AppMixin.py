#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author : younger shen
# email  : younger.x.shen@gmail.com

import sys
from jinja2 import Environment
from openbook.settings import settings


class Jinja2AppMixin(object):
    def __init__(self, *args, **settings):
        super(Jinja2AppMixin, self).__init__(self, *args, **settings)

