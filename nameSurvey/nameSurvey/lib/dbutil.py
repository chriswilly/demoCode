import sqlite3
from sqlite3 import Error
from pathlib import Path
import os
import configparser

class dbutil:
    """provide sqlite db to dump records"""
    def __init__(self,
                 db_loc = ':memory:'):
        self.location = db_loc
        self.configLoc = Path(os.path.abspath(__file__)).parents[0]
        # self.read_config(r'db_config.txt')
        self.conn = self.create_connection()
        self.cursor = self.create_cursor()

    def read_config(self,
                    file:str = r'db_config.txt'):
        config = configparser.RawConfigParser()
        config.read(self.configLoc/file)
        self.db_url = config.get('section','url')
        self.db_port = config.get('section','port')
        self.db_name = config.get('section','database')
        self.db_user = config.get('section','username')
        self.db_password = config.get('section','password')



    def create_connection(self):
        """ create a database connection to a SQLite database """
        conn = None
        # try:
        #     sqlStmt = f'{self.db_user}/{self.db_password}@{self.db_url}/{self.db_name}''
        #     conn = sqlite3.connect(sqlStmt)
        # except Error as e:
        #     rtrn = e.args[0]+':'+e.args[1]
        #     return False
        # return conn
        try:
            conn = sqlite3.connect(self.location)
            # print(f'db is in {self.location}')
            # return conn  # if use finally stmt
        except Error as e:
            print(e)
        # finally:
        #     if conn:
        #         conn.close()
        return conn


    def create_cursor(self):
        cursor = None
        try:
            cursor = self.conn.cursor()
        except Error as e:
            rtrn = e.args[0]+':'+e.args[1]
            return False
        return cursor


    def get_cnxn(self):
        return self.conn


    def get_cursor(self):
        return self.cursor


    def close_cursor(self):
        try:
            self.cursor.close()
        except Error:
            return False
        return True


    def close_cnxn(self):
        try:
            self.conn.close()
        except Error:
            return False
        return True


    def close_all(self):
        try:
            self.cursor.close()
            self.conn.close()
        except Error:
            return False
        return True







if __name__ == '__main__':
    db_loc = Path(os.path.abspath(__file__)).parents[0] # ':memory:'
    # print(db_loc)
    aa = dbutil(db_loc/'test.db')
    aa.close_all()
