#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author : younger shen
# email  : younger.x.shen@gmail.com

from openbook.mixins.HandlerMixins import DefaultHandler
from openbook.user.Models import User
from openbook.utils.DBUtils import get_session
from openbook.utils.CommonUtils import make_timestamp

class UserIndexHandler(DefaultHandler):
    module_name = "user"    
    def get(self):
        #user = User(avatar="avatar", create_time=make_timestamp(), signature="sdfsdf", last_login=make_timestamp(), nick_name = 'lili')
        user= User(avatar="s", update_time=make_timestamp(), create_time=make_timestamp(), signature="ss", last_login=make_timestamp(), nick_name="younger")
        user2= User(avatar="s", update_time=make_timestamp(), create_time=make_timestamp(), signature="ss", last_login=make_timestamp(), nick_name="younger2")
        
        dbsession , engine = get_session()
        user.friends.append(user2)
        dbsession.add(user)
        dbsession.add(user2)
        dbsession.commit()
        self.render_to_response("index.html" , dict())
