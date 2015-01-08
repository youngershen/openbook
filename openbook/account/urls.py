#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author : younger shen
# email  : younger.x.shen@gmail.com

from openbook.account.views.indexviews import IndexHandler
from openbook.account.views.indexviews import LoginHandler
from openbook.account.apis.apis import CheckUserNameAPI
urls  = [('/index', IndexHandler),]
urls += [('/check_username_api', CheckUserNameAPI),]
urls += [('/login', LoginHandler),]
