def sqlTable():
    return """CREATE TABLE IF NOT EXISTS messages
(
    id   bigserial unique primary key,
    name text not null,
    text text not null,
    time float
);"""


def sqlSelect():
    return """SELECT(name, text, time) from messages where time > %s;"""


def sqlInsert():
    return """INSERT INTO messages(name, text, time) VALUES
(%s, %s, %s);"""
