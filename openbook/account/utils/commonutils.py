#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author : younger shen
# email  : younger.x.shen@gmail.com

from sqlalchemy import func
from sqlalchemy import exists
from openbook.account.models.models import Account
from openbook.core.utils.dbutils import get_session


session, engine = get_session()

def check_username(username):
    query = session.query(Account).filter(Account.username == username).exists()
    ret = session.query(Account.username).filter(query).scalar()
    return False if ret is None else True

def check_email(email):
    query = session.query(Account).filter(Account.email == email).exists()
    ret = session.query(Account.username).filter(query).scalar()
    return False if ret is None else True

def check_account(username, email):
    return not check_username(username) and not check_email(email)
