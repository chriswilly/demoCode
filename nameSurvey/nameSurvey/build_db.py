
import os
from pathlib import Path

from lib.dbprocess import dbprocess
from nameView import nameView



def params():
    d = {
         'all_boys':((0,-1),1,(1800,2020),1,'M'),  # 18.9MB and took long, sql function prob
         'all_girls':((0,-1),1,(1800,2020),1,'F'), # 27.3MB
         'test_set':((0,-1),111,(1999,2011),2,None), #
         }
    return d


def load_db(df):
    for ix,row in df.iterrows():
        # print(row,'\n',row[0])
        record = (row['name'],row['sex'],row['number'],row['year'])
        # print(record)
        # bb.tbl_action('insert_rec',record)

        bb.tbl_action('insert_gen',('ssa_names',
                                   ('name','sex','number','year'),
                                   record))
    print('upld complete')


if __name__ =='__main__':
    d = params()
    names = nameView()
    df_set = names.load_names(*d['test_set'])
    db_name = 'test_set.db'
    # print(df_set.head())

    db_loc = Path(os.path.abspath(__file__)).parents[0] / 'tests'  # ':memory:'
    # print(db_loc)
    bb = dbprocess(db_loc/db_name)
    bb.tbl_action('create_tbl')
    load_db(df_set)


    errors, isOK = bb.tbl_action('simple_select',('DISTINCT id,name,year','ssa_names','id > 100 AND id < 200','id DESC'))
    # print(errors,isOK)
    # print(db.util.configLoc)
    bb.db.close_all()
