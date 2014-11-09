#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author : younger shen
# email  : younger.x.shen@gmail.com

from openbook.user.Urls import urls as user_urls
from openbook.account.Urls import urls as account_urls
from openbook.utils.CommonUtils import  make_urls_util

urls  = make_urls_util(r"/user", user_urls)
urls += make_urls_util(r"/account", account_urls)
