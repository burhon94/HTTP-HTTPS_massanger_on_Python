import os
import sys
from urllib.parse import urlparse

import psycopg2 as psycopg2

db_url = os.environ.get('DATABASE_URL')
if db_url is None:
    sys.exit('db env not accept')

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
