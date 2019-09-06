import pymysql


class Config:
    def __init__(self, type, host, port, username, password, database, encoding):
        self.type = type
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.database = database
        self.encoding = encoding

    def to_string(self):
        return 'type : ' + self.type + '\n' + \
               'host : ' + self.host + '\n' + \
               'port : ' + self.port + '\n' + \
               'username : ' + self.username + '\n' + \
               'password : ' + self.password + '\n' + \
               'database : ' + self.database + '\n' + \
               'encoding : ' + self.encoding + '\n'


class Connection:
    def __init__(self, conf):
        self.conn = self.get_conn(conf)

    def get_conn(self, conf):
        pass

    def execute(self, sql):
        cursor = self.conn.cursor()
        cursor.execute(sql)
        cursor.close()
        return cursor

    def query(self, sql):
        cursor = self.conn.cursor()
        cursor.execute(sql)
        res = cursor.fetchall()
        cursor.close()
        return res

    def close(self):
        self.conn.close()


class MySQLConn(Connection):
    def __init__(self, conf):
        super().__init__(conf)

    def get_conn(self, conf):
        return pymysql.connect(
            host=conf.host,
            port=int(conf.port),
            user=conf.username,
            password=conf.password,
            db=conf.database,
            charset=conf.encoding)


class GreenPlumConn(Connection):
    def __init__(self, conf):
        super().__init__(conf)

    def get_conn(self, conf):
        pass


class OracleConn(Connection):
    def __init__(self, conf):
        super().__init__(conf)

    def get_conn(self, conf):
        pass


class SQLServerConn(Connection):
    def __init__(self, conf):
        super().__init__(conf)

    def get_conn(self, conf):
        pass


class HiveConn(Connection):
    def __init__(self, conf):
        super().__init__(conf)

    def get_conn(self, conf):
        pass


class MongoDBConn(Connection):
    def __init__(self, conf):
        super().__init__(conf)

    def get_conn(self, conf):
        pass


def get_conn(conf):
    conn_dict = {
        "mysql": MySQLConn,
        "postgres": GreenPlumConn,
        "greenplum": GreenPlumConn,
        "oracle": OracleConn,
        "sqlserver": SQLServerConn,
        "hive": HiveConn,
        "mongodb": MongoDBConn
    }

    return conn_dict.get(conf.type)(conf)
