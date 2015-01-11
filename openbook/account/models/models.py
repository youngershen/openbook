#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author : younger shen
# email  : younger.x.shen@gmail.com

from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import backref
from openbook.core.utils.dbutils import get_session
from openbook.core.utils.dbutils import Base


class Account(Base):
    __tablename__='account'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    email = Column(String(255), index=True, unique=True, nullable=False)
    username = Column(String(255), index=True, unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    update_time = Column(TIMESTAMP)
    create_time = Column(TIMESTAMP)
    is_avaliable = Column(BOOLEAN, nullable=False, default=True)

