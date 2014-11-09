from sqlalchemy import *
from migrate import *


meta = MetaData()

def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    meta.bind = migrate_engine
    user_follow_table = Table('user_follow', meta, autoload=True) 
    user_follow_table.drop()
def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pass
