#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author : younger shen
# email  : younger.x.shen@gmail.com

from openbook.mixins.HandlerMixins import DefaultHandler
from openbook.user.Models import User
from openbook.utils.DBUtils import get_session

class UserIndexHandler(DefaultHandler):
    module_name = "user"    
    def get(self):
        username = self.get_argument("username")
        password = self.get_argument("password")
        user = User(username=username, password=password, desc="sdfsdfs")
        dbsession , engine = get_session()
        dbsession.add(user)
        dbsession.commit()
        self.render_to_response("index.html" , dict(user = user))
