#!/usr/bin/env python
#-*- coding: utf-8 -*-
from sqlalchemy import *
from migrate import *

meta = MetaData()

user = Table(
        'user', meta,
        Column('id', Integer, primary_key=True),
        )
user_relation=Table(
                    'user_relation', meta,
                    Column('id', Integer, primary_key = True),
                    Column('left_id', Integer, ForeignKey('user.id'), nullable = False),
                    Column('right_id',Integer, ForeignKey('user.id'), nullable = False ),
                )

def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    meta.bind=migrate_engine
    user_relation.create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    meta.bind=migrate_engine
    user_relation.drop()
