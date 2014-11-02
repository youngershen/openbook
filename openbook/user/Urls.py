#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author : younger shen
# email  : younger.x.shen@gmail.com

from openbook.user.IndexViews import UserIndexHandler

urls = [('/index/[0-9]+', UserIndexHandler),]
