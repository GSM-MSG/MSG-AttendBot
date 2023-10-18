import os
import pymysql
from dotenv import load_dotenv

load_dotenv()


class Connection:
    def __init__(self):
        self.host = os.getenv('DB_HOST')
        self.user = os.getenv('DB_USER')
        self.pw = os.getenv('DB_PASSWORD')
        self.db = os.getenv('DB_SCHEMA')
        self.conn = pymysql.connect(host=self.host, user=self.user, password=self.pw, database=self.db)
        self.cur = self.conn.cursor(pymysql.cursors.DictCursor)
        print("DB에 성공적으로 연결됨")

    def close_connection(self):
        self.conn.close()
        print("DB 연결을 끊음")

    def get_connection(self):
        self.conn.ping()
        return self.conn, self.cur

    def scoreboard(self):
        conn, cur = connection.getConnection()
        cur.execute('''SELECT id, point FROM Members WHERE guild=? ORDER BY point DESC''', (self.id,))
        s = ''
        point = float('inf')
        rank, count = 1, 1
        for Id, Point in c.fetchall():
            user = self.get_member(Id)
            if user is None:
                continue
            if point != Point:
                rank = count
                point = Point
            s += "{:d}. {:d}점 {:s}\n".format(rank, Point, user.display_name)
            count += 1
            if count > 10:
                break
        return s


connection = Connection()
