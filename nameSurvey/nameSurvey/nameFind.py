import pandas as pd
import numpy as np

from nameView import nameView


if __name__ == '__main__':
    bb = nameView()
    print('test1:')
    test1 = bb.load_names((0,6),1,(1890,1945),3,'M')
    print('test2:')
    test2 = bb.load_names((0,6),1,(1946,1999),3,'M')
    print('test3:')
    test3 = bb.load_names((0,6),1,(0,0),3,'M')


    a = np.unique(test1['name'])
    b = np.unique(test2['name'])
    c = np.unique(test3['name'])

    print('\nunique names:',
            a.shape[0],
            b.shape[0],
            c.shape[0])
