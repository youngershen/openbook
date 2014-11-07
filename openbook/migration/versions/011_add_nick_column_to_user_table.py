from sqlalchemy import *
from migrate import *

meta = MetaData()
def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    meta.bind=migrate_engine
    user=Table('user', meta, autoload=True)
    nick_name_column = Column('nick_name', String(255))
    print dir(user)
    nick_name_column.create(user)
def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pass
