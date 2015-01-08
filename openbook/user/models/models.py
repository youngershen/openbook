#!/usr/bin/env python
# -*- coding:utf-8 -*-  
# author : younger shen
# email  : younger.x.shen@gmail.com

from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy import ForeignKey
from sqlalchemy import Table
from sqlalchemy import TIMESTAMP
from sqlalchemy import TEXT
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from openbook.utils.dbutils import get_session
from openbook.utils.dbutils import Base
from openbook.account.models.models import Account


#Base = declarative_base()

friendship = Table(
        'user_relation', Base.metadata,
        Column('left_id', Integer, ForeignKey('user.id')),
        Column('right_id', Integer, ForeignKey('user.id')),
        )

class User(Base):
    __tablename__='user'
    id = Column(Integer, primary_key=True)
    avatar = Column('avatar', String(255))
    update_time = Column('update_time', TIMESTAMP)
    create_time = Column('create_time', TIMESTAMP)
    signature = Column('signature', TEXT)
    last_login = Column('last_login', TIMESTAMP, nullable=False)    
    nick_name = Column('nick_name', String(255))
    following = relationship("User", secondary=friendship, primaryjoin= id== friendship.c.left_id, secondaryjoin= id== friendship.c.right_id, backref="followed")
    account = relationship(Account, backref='user', uselist=False)
    

    def __unicode__(self):
        return "<User(id={id}, username={username}, password={password})>".format(username=self.username, password=self.password, id=self.id)
