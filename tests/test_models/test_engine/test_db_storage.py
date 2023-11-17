from models.state import State
from models.engine.db_storage import DBStorage
import unittest
import MySQLdb
import pep8
import os


class TestDBStorage(unittest.TestCase):
    """a class to test storage db"""

    @classmethod
    def setUp(self):
        """Set up MySQL"""
        self.db = MySQLdb.connect(host="localhost",
                                  port=3306,
                                  user='hbnb_test',
                                  passwd='hbnb_test_pwd',
                                  db='hbnb_test_db',
                                  charset='utf8')
        self.cur = self.db.cursor()
        self.storage = DBStorage()
        self.storage.reload()

    @classmethod
    def tearDown(self):
        """Tear down MySQL db"""
        self.cur.close()
        self.db.close()

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db', 'db')
    def test_pep8_DBStorage(self):
        """test pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/engine/db_storage.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db', 'db')
    def test_add(self):
        """Test add method"""
        self.cur.execute("""
        INSERT INTO states (id, created_at, updated_at, name)
        VALUES (1, '2017-11-10 00:53:19', '2017-11-10 00:53:19', "California")
        """)
        self.cur.execute('SELECT * FROM states')
        rows = self.cur.fetchall()
        self.assertEqual(len(rows), 1)


if __name__ == "__main__":
    unittest.main()
