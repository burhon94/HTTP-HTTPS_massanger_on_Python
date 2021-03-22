import psycopg2 as psycopg2


def Get():
    conn = psycopg2.connect(dbname='messenger', user='user',
                            password='pass', host='localhost', port=5432)
    return conn


def Close(conn, cursor):
    cursor.close()
    conn.close()
