import os
from pathlib import Path
import sqlite3
from sqlite3 import Error
# local:
if __file__ == 'dbprocess.py':
    from dbutil import dbutil
    from qry import sql_stmt
else:
    from lib.dbutil import dbutil
    from lib.qry import sql_stmt


class dbprocess:
    """conduct db actions using connection in utils"""
    def __init__(self,
                 db_loc:str = ':memory:'):
        self.db = dbutil(db_loc)
        self.cnxn = self.db.get_cnxn()
        self.sql_stmt = sql_stmt()
        # self.cnxn.autocommit = False  # oracle



    def tbl_action(self,
                   *args:str):
        # print(*args)
        try:
            stmt, vals = args
        except:
            stmt = args[0]
            vals = None

        dbErr = ''
        successFlag = False
        # self.cnxn.begin()
        try:
            cur = self.cnxn.cursor()
            if vals:
                # print(self.sql_stmt[stmt].format(*vals))
                cur.execute(self.sql_stmt[stmt].format(*vals))
                if stmt == 'simple_select':
                    [print(*row) for row in cur.fetchall()]

            else:
                cur.execute(self.sql_stmt[stmt])
            self.cnxn.commit()
            successFlag = True

        except Error as e:
            print(f'trouble performing {stmt}: ', e)
            successFlag = False
            dbErr, = e.args
            self.cnxn.rollback()

        return dbErr, successFlag



if __name__ =='__main__':
    db_loc = Path(os.path.abspath(__file__)).parents[1] # ':memory:'
    # print(db_loc)
    # aa = dbutil(db_loc)
    bb = dbprocess(db_loc/'tests'/'nameset.db')
    errors, isOK = bb.tbl_action('create_tbl')
    # errors, isOK = bb.tbl_action('insert_rec',('ben','M',12,1999))
    errors, isOK = bb.tbl_action('insert_gen',
                                 ('ssa_names',
                                 ('name','sex','number','year'),
                                 ('jim','M',97718,80808))
                                 )


    errors, isOK = bb.tbl_action('simple_select',('DISTINCT id,name,year','ssa_names','id<10','id'))
    # print(errors,isOK)
    # print(db.util.configLoc)
    bb.db.close_all()





# ####
# ## sql alchemy for oracle
# from sqlalchemy import (types,
#                         create_engine)
# cnxn = create_engine('sqlitestring ~ oracle+cx_oracle://scott:tiger@host:1521/?service_name=hr')
# df.to_sql('test',cnxn,if_exists='replace')
#
# ###### other example
# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy import Column, String
# from sqlalchemy.orm import sessionmaker
# import pandas as pd
#
# dsn = cx_Oracle.makedsn('public_ip','listener_port',service_name = 'service_name')  # listener_port ~1521
# engine = create_engine('oracle+cx_oracle://{0}:{1}@{2}'.format(user, pw, dsn))
# cnxn = engine.connectr()
#
# Base = declarative_base()
# class MAPPER(Base):
#     __tablename__ = 'table_name'
#     id = Column(String(500),prinary_key = True)
#     name = Column(String(500))
#
# dbSession = sessionmaker(bind=engine)
#
# sesh = dbSession()
# lists = data.to_dict(orient='records')
# tbl = sqlalchemy.Table('saomename', Base.metadata, autoreload=True)
# cnxn.execute(tbl.insert(),lists)
# sesh.commit()
# sesh.close()
