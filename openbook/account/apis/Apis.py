#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author : younger shen
# email  : younger.x.shen@gmail.com

from openbook.mixins.HandlerMixins import RESTHandler
from openbook.account.utils.CommonUtils import check_account

class CheckUserNameAPI(RESTHandler):
    def get(self):
        ret = check_account('youngers', 'younger.x.shen@gmail.com')
        self.return_to_json(dict(state=ret,message='love'))
