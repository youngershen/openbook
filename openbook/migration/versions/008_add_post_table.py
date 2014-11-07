from sqlalchemy import *
from migrate import *


meta = MetaData()

user = Table(
        'user', meta,
        Column('id', Integer, primary_key=True)
        )
post = Table(
        'post', meta,
        Column('id', Integer, primary_key=True),
        Column('title', String(255), index=True, nullable=True, default=""),
        Column('content', TEXT, nullable=False),
        Column('reply_id', Integer, ForeignKey('post.id'), nullable=True),
        Column('author', Integer, ForeignKey('user.id'), nullable=False),
        Column('update_time', TIMESTAMP),
        Column('create_time', TIMESTAMP),
        mysql_engine='InnoDB'
        )
def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    meta.bind=migrate_engine
    post.create()

def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    meta.bind=migrate_engine
    post.drop()
