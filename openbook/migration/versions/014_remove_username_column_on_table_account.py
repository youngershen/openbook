from sqlalchemy import *
from migrate import *

meta = MetaData()

def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    meta.bind=migrate_engine
    account = Table('account', meta, autoload=True)
    account.c.username.drop()

def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    meta.bind=migrate_engine
    account=Table('account', meta, autolaod=True)
    username_column = Column('username', String(255), index=True, unique=True, nullable=False),
    username_column.create(account)
