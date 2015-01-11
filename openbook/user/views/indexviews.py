#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author : younger shen
# email  : younger.x.shen@gmail.com

from openbook.mixins.handlermixins import DefaultHandler
from openbook.user.models.models import User
from openbook.core.utils.dbutils import get_session
from openbook.core.utils.commonutils import make_timestamp

class IndexHandler(DefaultHandler):
    module_name = "user"    
    def get(self):
        #user = User(avatar="avatar", create_time=make_timestamp(), signature="sdfsdf", last_login=make_timestamp(), nick_name = 'lili')
        user= User(avatar="s", update_time=make_timestamp(), create_time=make_timestamp(), signature="ss", last_login=make_timestamp(), nick_name="younger")
        user2= User(avatar="s", update_time=make_timestamp(), create_time=make_timestamp(), signature="ss", last_login=make_timestamp(), nick_name="younger2")
        
        session , engine = get_session()
        
        #user.following.append(user2)
        #session.add(user)
        #session.add(user2)
        #session.commit()
        #user1 = session.query(User).filter(User.id==1).all()[0]
        #user3 = session.query(User).filter(User.id==3).all()[0]
        #user4 = session.query(User).filter(User.id==4).all()[0]

        #user3.following.append(user1)
        #session.commit()
        #user3_following = user3.following
        #print user4.followed[0].id
        self.session()
        self.session_add('test', 'test')
        #self.session_add('username', 'younger')
        #self.session_add('password', 'younger')
        self.write(self.session_get('test'))
        self.write('fuck')
        #self.render_to_response("index.html" , dict())
