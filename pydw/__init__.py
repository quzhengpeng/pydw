from pydw.utils import config
from pydw.utils import connection


def connect(db_conn):
    conf = config.get_config(db_conn)
    conn = connection.get_conn(conf)
    return conn.conn


def create(db_conn):
    conf = config.get_config(db_conn)
    conn = connection.get_conn(conf)
    return conn
