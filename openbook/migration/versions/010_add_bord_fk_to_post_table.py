from sqlalchemy import *
from migrate import *

meta = MetaData()

board = Table('board', meta,
        Column('id', Integer, primary_key=True))

def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    meta.bind=migrate_engine
    post = Table('post', meta, autoload=True)
    board = Column('board_id', Integer, ForeignKey('board.id'), nullable=True)
    board.create(post)
def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pass
