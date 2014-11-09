#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author : younger shen
# email  : younger.x.shen@gmail.com

from openbook.account.views.IndexViews import IndexHandler
from openbook.account.apis.Apis import CheckUserNameAPI
urls = [('/index', IndexHandler),]
urls += [('/check_username_api', CheckUserNameAPI),]
