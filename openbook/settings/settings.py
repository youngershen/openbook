#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author : younger shen
# email  : younger.x.shen@gmail.com

import os

ENV = os.getenv('OPENBOOK_ENV_STATUS')

if 'PROD' == ENV:
    from .settings_prod import settings
else:
    from .settings_dev import settings
