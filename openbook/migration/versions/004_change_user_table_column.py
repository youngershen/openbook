from sqlalchemy import *
from migrate import *


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    meta = MetaData(bind=migrate_engine)
    user = Table('user', meta, autoload=True)
    last_login_column = Column('last_login', TIMESTAMP, nullable=False)
    last_login_column.create(user)

def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    meta=MetaData(bind=migrate_engine)
    user=Table('user', meta, autoload=True)
    user.c.last_login.drop()
