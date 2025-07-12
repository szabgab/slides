import pytest
import os, time

from app.common import get_mongo

@pytest.fixture(autouse = True)
def configuration():
    dbname = 'test_app_' + str(int(time.time()))
    os.environ['APP_DB_NAME'] = dbname

    yield

    get_mongo().drop_database(dbname)

