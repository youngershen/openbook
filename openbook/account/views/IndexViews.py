#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author : younger shen
# email  : younger.x.shen@gmail.com

from openbook.mixins.HandlerMixins import DefaultHandler
from openbook.utils.DBUtils import get_session
from openbook.account.models.Models import Account
from openbook.user.models.Models import User

class IndexHandler(DefaultHandler):
    module_name='account'

    def get(self):
        
        session, engine = get_session()
        account = Account()
        user = User()
        account.email = 'younger.x.shen@gmail.com'
        account.username = 'younger'
        account.password = 'younger'
        account.user = user
        #session.add(user)
        #session.add(account)
        #session.commit()
        user = session.query(User).filter(User.id == 5).all()[0]
        
        print user.account.id
        self.write("index from account")

    def post(self):
        pass
