import time
import psycopg2 as psycopg2

from flask import Flask, request

app = Flask(__name__)


sqlTable = """CREATE TABLE IF NOT EXISTS messages
(
    id   bigserial unique primary key,
    name text not null,
    text text not null,
    time float
);"""

sqlSelect = """SELECT(name, text, time) from messages where time > %s;"""

sqlInsert = """INSERT INTO messages(name, text, time) VALUES
(%s, %s, %s);"""


def get_conn():
    conn = psycopg2.connect(dbname='messenger', user='user',
                        password='pass', host='localhost', port=5432)
    return conn


connInit = get_conn()
cursorInit = connInit.cursor()
try:
    # execute the INSERT statement
    cursorInit.execute(sqlTable)
    # commit the changes to the database
    connInit.commit()
except (Exception, psycopg2.DatabaseError) as error:
    print(error)

cursorInit.close()
connInit.close()


@app.route("/")
def main_Page():
    return "Hello World! from Flask by python"


@app.route("/status")
def status():
    return {
        'status': True,
        'app': "Messenger",
        'server_time': time.time()  # unix_time_stamp
    }


@app.route("/get/msgs", methods=["GET"])
def get_msgs():
    msg_filtered = []
    conn = get_conn()
    cursor = conn.cursor()

    try:
        after = float(request.args['after'])
    except:
        return {
            'code': 400,
            'payload': '',
            'error': 'after not undefined'
        }

    try:
        # execute the INSERT statement
        cursor.execute(sqlSelect, (after,))
        # commit the changes to the database
        conn.commit()

        for msg in cursor:
            msg_filtered.append(msg)

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    cursor.close()
    conn.close()
    return {
        'msgs': msg_filtered
    }


@app.route("/send/msg", methods=['POST'])
def send_msg():
    conn = get_conn()
    cursor = conn.cursor()

    data = request.json
    name = data.get('name')
    text = data.get('text')
    tm = time.time()

    try:
        cursor.execute(sqlInsert, (name, text, tm,))
        conn.commit()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    cursor.close()
    conn.close()
    return {
        'code': 200,
        'payload': tm,
        'error': ''
    }


app.run()
