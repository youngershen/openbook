from sqlalchemy import *
from migrate import *
import time

def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    meta = MetaData(bind=migrate_engine)
    user = Table('user', meta, autoload=True)
    #define new column
    avatar_column = Column('avatar', String(255))
    update_time_column = Column('update_time', TIMESTAMP)
    create_time_column = Column('create_time', TIMESTAMP, default=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())))
    signature_column = Column('signature', TEXT)

    avatar_column.create(user)
    update_time_column.create(user)
    create_time_column.create(user)
    signature_column.create(user)

def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pass
