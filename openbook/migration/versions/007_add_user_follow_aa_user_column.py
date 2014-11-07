from sqlalchemy import *
from migrate import *

meta = MetaData()

user = Table(
        'user', meta,
        Column('id', Integer, primary_key=True)
        )
user_follow =  Table(
        'user_follow', meta,
        Column('id', Integer, primary_key=True),
        Column('user_id', Integer, ForeignKey('user.id'), nullable=False),
        Column('follow_id', Integer, ForeignKey('user.id'), nullable=False),
        Column('update_time', TIMESTAMP),
        Column('create_time', TIMESTAMP),
        mysql_engine='InnoDB'
        )

def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    meta.bind=migrate_engine
    user_follow.create() 
def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    meta.bind=migrate_engine
    user_follow.drop()
