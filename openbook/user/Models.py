#!/usr/bin/env python
# -*- coding:utf-8 -*-  
# author : younger shen
# email  : younger.x.shen@gmail.com

from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy.ext.declarative import declarative_base

from openbook.utils.DBUtils import get_session
Base = declarative_base()

class User(Base):
    __tablename__='user'
    id = Column(Integer, primary_key=True)
    username = Column(String(255))
    password = Column(String(255))
    desc     = Column(String(255))
    
    def __unicode__(self):
        return "<User(id={id}, username={username}, password={password})>".format(username=self.username, password=self.password, id=self.id)
