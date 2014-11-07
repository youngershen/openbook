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
from openbook.utils.DBUtils import get_session


Base = declarative_base()
class Association(Base):
    __tablename__ = 'association'
    left_id = Column(Integer, ForeignKey('left.id'), primary_key=True)
    right_id = Column(Integer, ForeignKey('right.id'), primary_key=True)
    extra_data = Column(String(50))
    child = relationship("Child", backref="parent_assocs")

class Parent(Base):
    __tablename__ = 'left'
    id = Column(Integer, primary_key=True)
    children = relationship("Association", backref="parent")

class Child(Base):
    __tablename__ = 'right'
    id = Column(Integer, primary_key=True)

class Association_table(Base):
    __tablename__='suser_follow'
    user_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    follow_id = Column(Integer, ForeignKey('user.id'), primary_key=True)

friendship = Table(
        'user_follow', Base.metadata,
        Column('user_id', Integer, ForeignKey('user.id')),
        Column('follow_id', Integer, ForeignKey('user.id'))
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
    friends = relationship("User", secondary=friendship, primaryjoin= id== friendship.c.user_id, secondaryjoin= id== friendship.c.follow_id)
        
    def __unicode__(self):
        return "<User(id={id}, username={username}, password={password})>".format(username=self.username, password=self.password, id=self.id)
