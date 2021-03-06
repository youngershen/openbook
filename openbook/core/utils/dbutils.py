# -*- coding: utf-8 -*-
# author  : younger shen
# email   : younger.x.shen@gmail.com
# project : Playwork
# date    : 15/1/11 下午9:22

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from openbook.settings.settings import settings

from sqlalchemy.ext.declarative import declarative_base


DBURL = "{dbtype}://{user}:{pwd}@{host}:{port}/{dbname}"

Base = declarative_base()

def get_session():

    dburl = DBURL.format(dbtype=settings['DATABASE'],\
        user=settings['DBUSER'],\
        pwd=settings['DBPASS'],\
        host=settings['DBHOST'],\
        dbname=settings['DBNAME'],\
        port=settings['DBPORT'],\
        )
    engine = create_engine(dburl, **settings['DBCONFIG'])
    Session = sessionmaker(bind=engine)
    session = Session()
    return session, engine
