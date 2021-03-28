
import os
from pathlib import Path
import argparse
import pandas as pd
import numpy as np

class nameView:
    def __init__(self):
        self.file_path('data/names',1)
        self.files = self.file_list(self.directory,'desc')


    def file_path(self,
                  subdirectory:str = 'data/names', 
                  level:int = 1):
        self.directory = Path(os.path.abspath(__file__)).parents[level] / subdirectory #look for data dir one level up
        print(self.directory)
        # print(os.listdir(self.directory))


    def file_list(self,
                  folder:str = None,
                  order:str = None,
                  filetype:str = 'txt'):

        out = [f for f in os.listdir(folder)
               if os.path.isfile(folder/f)
               and f.endswith(filetype)]

        if order=='desc':
            out.sort(reverse=True)

        return np.asarray(out,dtype=str)

    def load_names(self,
                   rank:tuple = (0,11),
                   space:int = 1,
                   year:tuple = (1972,),
                   skip:int = 1,
                   sex:str = None):
        """"""
        # clean intervals to non zero
        space = 1 if space <= 0 else space
        skip = 1 if skip <= 0 else skip

        # string fmt
        strip = lambda x: int((x.replace('yob','').replace('.txt','').zfill(4)))

        years = np.asarray([strip(y) for y in self.files],dtype=int)
        names = pd.DataFrame(columns=['name','number','year'])
        # yobYYYY.txt format "name,sex,number"
        try:
            indx = np.asarray(years>=year[0],dtype=bool) & np.asarray(years<=year[1],dtype=bool)
        except:
            indx = np.asarray(years>=year[0],dtype=bool)
        if indx[indx].shape[0]==0:
            print('error finding range specified, include full year range')
            indx = np.ones(years.shape[0],dtype=bool)

        indz = np.arange(indx.shape[0])[indx] # set of in range years
        indx = np.zeros(indx.shape[0],dtype=bool) # reset indx
        indx[indz[::skip]]  = 1 # keep vals in range at interval
        # print(indz[::skip])


        for file in self.files[indx]:
            data = pd.read_csv(self.directory/file,sep=',',header=None)
            data.columns=['name','sex','number']
            if sex:
                data.drop(data[data['sex']!=sex].index,inplace=True)
            else:
                print('all sexes included')
                pass

            data.drop(columns='sex',inplace=True)
            data.sort_values(by=['number'],inplace=True, ascending=False)
            data.reset_index(drop=True,inplace=True)

            # print(data.head())
            yr = strip(file)
            indy = range(rank[0],rank[1],space)
            s = 'all' if sex is None else 'male' if sex == 'M' else 'female'
            print(f'Top {rank[0]} to {rank[1]} {s} names in {yr}')
            print(data.iloc[indy])
            data['year'] = yr

            names = names.append(data.iloc[indy], ignore_index=True)
        return names


if __name__ == '__main__':
    # rank = (0,11)
    # space = 1
    # year = (1910,1985)
    # skip = 2
    # sex = 'F'

    parser = argparse.ArgumentParser(description='Set name serach criteria')

    parser.add_argument('--rank', metavar=('lower bound', 'upper bound'),
                        type=int, nargs=2,
                        help='popularity starting and ending position, \
                            lower is more popular',
                        default=(0,11))

    parser.add_argument('--space', metavar='rank spacing',
                        type=int, nargs='?',
                        help='rank spacing: 0,1,2..., 0,2,4...',
                        default=1)

    parser.add_argument('--years', metavar=('year start','year end'),
                        type=int, nargs=2,
                        help='date range years',
                        default=(1972,))

    parser.add_argument('--skip', metavar='year spacing',
                        type=int, nargs='?',
                        help='year spacing: 1999, 2000, 2001,... 1998, 2000, 2002,...',
                        default=1)

    parser.add_argument('--sex', metavar='M/F/B',
                        type=str, nargs='?',
                        help='F = Female, M = Male, None = Both',
                        default=None)  #const=None


    args = parser.parse_args()
    # print(args)

    aa = nameView()
    names = aa.load_names(args.rank, args.space,
                          args.years, args.skip,
                          args.sex)
    uniques = np.unique(names['name'])
    # print(names.head())
