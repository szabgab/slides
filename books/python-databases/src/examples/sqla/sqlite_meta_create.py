from sqlalchemy import create_engine
import os
from sqlite_meta_schema import get_meta

dbname = 'test.db'
if os.path.exists(dbname):
    os.unlink(dbname)
engine = create_engine('sqlite:///test.db')

metadata = get_meta()
metadata.create_all(engine)
