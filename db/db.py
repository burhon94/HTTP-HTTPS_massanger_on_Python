import os
import sys
from urllib.parse import urlparse

import psycopg2 as psycopg2

db_url = os.environ.get('DATABASE_URL')
if db_url is None:
    sys.exit('db env not accept')
    # db_url = "postgres://esgzabmdfxgbev:4aa3757628bbdb5c6fb149e9e5699985b9f5a2b65ef0f22d0f82de2a52f3eda5@ec2-54-161-239-198.compute-1.amazonaws.com:5432/d7u8mb88fc2j9h"

result = urlparse(db_url)
username = result.username
password = result.password
database = result.path[1:]
hostname = result.hostname
port = result.port


def Get():
    conn = psycopg2.connect(dbname=database, user=username,
                            password=password, host=hostname, port=port)
    return conn


def Close(conn, cursor):
    cursor.close()
    conn.close()
