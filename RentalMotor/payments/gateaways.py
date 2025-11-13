import threading
import MySQLdb   # provided by mysqlclient

class MySQLSingleton:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            with cls._lock:
                if not cls._instance:
                    cls._instance = super().__new__(cls)
                    cls._instance._init_conn(*args, **kwargs)
        return cls._instance

    def _init_conn(self, host, user, passwd, db, port=3306):
        self.conn = MySQLdb.connect(host=host, user=user, passwd=passwd, db=db, port=port)
        self.cursor = self.conn.cursor()

    def query(self, q, params=None):
        self.cursor.execute(q, params or ())
        return self.cursor.fetchall()

    def close(self):
        self.cursor.close()
        self.conn.close()
        MySQLSingleton._instance = None
