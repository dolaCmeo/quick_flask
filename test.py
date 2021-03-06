import unittest
import os
import MySQLdb


class Storage:
    def __init__(self):
        self.db = MySQLdb.connect(
            user=os.getenv('MYSQL_USERNAME'),
            passwd=os.getenv('MYSQL_PASSWORD'),
            db=os.getenv('MYSQL_INSTANCE_NAME'),
            host=os.getenv('MYSQL_PORT_3306_TCP_ADDR'),
            port=int(os.getenv('MYSQL_PORT_3306_TCP_PORT'))
        )

        cur = self.db.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS scores(score INT)")

    def populate(self):
        cur = self.db.cursor()
        cur.execute("INSERT INTO scores(score) VALUES(1234)")

    def score(self):
        cur = self.db.cursor()
        cur.execute("SELECT * FROM scores")
        row = cur.fetchone()
        return row[0]


class TestSuite(unittest.TestCase):
    def test(self):
        storage = Storage()
        storage.populate()
        score = storage.score()
        self.failIf(score != 1234)


def main():
    unittest.main()


if __name__ == "__main__":
    main()
