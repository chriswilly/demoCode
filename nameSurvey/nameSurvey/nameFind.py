import pandas as pd
import numpy as np

from nameView import nameView


def params():
    d = {
         'olden':((0,6),1,(1890,1945),5,'M'),
         'midcentury':((0,6),1,(1946,1999),5,'M'),
         # 'comprehensive':((0,6),1,(0,0),3,'M'),
         }
    return d



if __name__ == '__main__':
    bb = nameView()
    d = params()
    # print('test1:')
    # test1 = bb.load_names(*d['olden'])
    # a = np.unique(test1['name'])

    print('\nunique names per set: ')
    [print('unique names in ',key,': ',
            np.unique(bb.load_names(*vals)['name']).shape[0])
            for key,vals in d.items() ]
