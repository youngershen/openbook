from sqlalchemy import *
from migrate import *
import time
now = time.strftime("%Y-%m-%d $H:%M:%S", time.localtime(time.time()))

meta = MetaData()

user = Table(
        'user', meta,
        Column('id', Integer, primary_key=True),
        )

account = Table(
        'account', meta,
        Column('id', Integer, primary_key=True),
        Column('user_id', Integer, ForeignKey('user.id')),
        Column('email', String(255),  index=True, unique=True, nullable=False),
        Column('username', String(255), index=True, unique=True, nullable=False),
        Column('password', String(255), nullable=False),
        Column('update_time', TIMESTAMP ),
        Column('create_time', TIMESTAMP, default=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))),
        Column('is_avaliable', BOOLEAN, nullable=False, default=True),
        mysql_engine='InnoDB'
        )

def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    meta.bind=migrate_engine
    account.create()

def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    meta.bind=migrate_engine
    account.drop()
