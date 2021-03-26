import psycopg2 as psycopg2

from db.db import Get
from db.db import Close


def initDB():
    conn = Get()
    cursor = conn.cursor()
    try:
        cursor.execute("""CREATE TABLE IF NOT EXISTS messages
(
    id   bigserial unique primary key,
    name text not null,
    text text not null,
    time float
);""")
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    Close(conn, cursor)


def send_msg(name, text, tm):
    conn = Get()
    cursor = conn.cursor()

    try:
        cursor.execute("""INSERT INTO messages(name, text, time) VALUES
(%s, %s, %s);""", (name, text, tm,))
        conn.commit()
        resp = {
            'code': 200,
            'payload': tm,
            'error': ''
        }

        Close(conn, cursor)
        return resp

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        resp = {
            'code': 500,
            'payload': '',
            'error': str(error)
        }

        Close(conn, cursor)
        return resp


def get_msgs(after):
    conn = Get()
    cursor = conn.cursor()
    msg_filtered = []

    try:
        cursor.execute("""SELECT name, text, time from messages where time > %s;""", (after,))

        for row in cursor:
            tmp = {}
            msg_sender = str(row[0])
            msg_text = str(row[1])
            msg_time = float(row[2])

            tmp["name"] = msg_sender
            tmp["text"] = msg_text
            tmp["time"] = msg_time
            msg_filtered.append(tmp)
        Close(conn, cursor)

        resp = {
            'code': 200,
            'payload': msg_filtered,
            'error': ''
        }
        return resp

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        resp = {
            'code': 500,
            'payload': '',
            'error': str(error)
        }

        Close(conn, cursor)
        return resp
