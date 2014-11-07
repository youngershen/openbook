from sqlalchemy import *
from migrate import *

meta = MetaData()

user = Table(
        'user', meta,
        Column('id', Integer, primary_key=True)
        )

board = Table(
        'board', meta,
        Column('id', Integer, primary_key=True),
        Column('name', String(255), unique=True, index=True, nullable=False),
        Column('logo', String(255), nullable=True, default=""),
        Column('description', TEXT, nullable=True, default=""),
        Column('creator', Integer, ForeignKey('user.id'), nullable=False)
        )

def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    meta.bind=migrate_engine
    board.create()

def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    meta.bind=migrate_engine
    board.drop()
