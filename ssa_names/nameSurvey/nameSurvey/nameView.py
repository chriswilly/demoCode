
import os
from pathlib import Path
import argparse
import pandas as pd
import numpy as np

class nameView:
    def __init__(self):
        self.file_path()
        self.files = self.file_list(self.directory,'desc')


    def file_path(self,subdirectory:str = 'data/names'):
        self.directory = Path(os.path.abspath(__file__)).parents[2]
        self.directory = self.directory / subdirectory
        print(self.directory)
        # print(os.listdir(targetfolder))


    def file_list(self,
                  folder:str = None,
                  order = None,
                  filetype:str = 'txt'):

        out = [f for f in os.listdir(folder)
               if os.path.isfile(folder/f)
               and f.endswith(filetype)]

        if order=='desc':
            out.sort(reverse=True)

        return np.asarray(out,dtype=str)

    def load_names(self,
                   num: tuple=(0,11),
                   year: tuple=(1972,),
                   sex: str=None):
        """"""
        strip = lambda x: int((x.replace('yob','').replace('.txt','').zfill(4)))
        
        years = np.asarray([strip(y) for y in self.files],dtype=int)
        names = pd.DataFrame(columns=['name','number','year'])
        # directory containing yobYYYY.txt format "name,sex,number"
        try:
            indx = np.asarray(years>=year[0],dtype=bool) & np.asarray(years<=year[1],dtype=bool)
        except:
            indx = np.asarray(years>=year[0],dtype=bool)

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
            indy = range(num[0],num[1])
            s = 'all' if sex is None else 'male' if sex == 'M' else 'F'
            print(f'Top {num[0]} to {num[1]} {s} names in {yr}')
            print(data.iloc[indy])
            data['year'] = yr

            names = names.append(data.iloc[indy], ignore_index=True)
        return names


if __name__ == '__main__':
    # rank = (0,11)
    # year = (1910,1985)
    # sex = 'F'

    parser = argparse.ArgumentParser(description='Set name serach criteria')

    parser.add_argument('--rank', metavar=('lower_bound', 'upper_bound'),
                        type=int, nargs=2,
                        help='popularity starting and ending position, \
                            lower is more popular',
                        default=(0,11))

    parser.add_argument('--years', metavar=('year_start','year_end'),
                        type=int, nargs=2,
                        help='date range years',
                        default=(1972,))

    parser.add_argument('--sex', metavar='M/F',
                        type=str, nargs='?',
                        help='F = female, M = Male, None = Both',
                        default=None)  #const=None


    args = parser.parse_args()
    # print(args)

    aa = nameView()
    names = aa.load_names(args.rank, args.years, args.sex)
    # print(names.head())
