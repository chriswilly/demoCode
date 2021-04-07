
import os
import csv
from datetime import datetime
from pathlib import Path

class errorlogger:
    def __init__(self,
                 file:str = 'test',
                 id:str = 'tester',
                 batch:int = 88):
        self.filename = file
        self.user = id
        self.job = batch

        self.logbook = []
        current_time = datetime.now().strftime('%Y%m%d_%H%M%S')
        self.filedest = self.filepath(3) # 3 folders up
        self.outputfile = self.filedest/f'record_{self.user}_{self.job}_{current_time}.csv'


    def filepath(self,
                 level:int=2):
        outDir = Path(os.path.abspath(__file__)).parents[level]/'errorlog'
        if os.path.exists(outDir):
            return outDir
        else:
            try:
                os.mkdir(outDir)
                return outDir
            except:
                print(f'unable to create error log output in {outDir}')
                return None

    def errorFilename(self):
        return self.outputfile


    def writeLog(self,*details):
        self.logbook.append((datetime.now().strftime('%Y%m%d_%H:%M:%S'),
                             self.job,
                             str(self.filename),
                             self.user,
                             # ','.join(*details),
                             *details
                             )
                            )
    def finalizeLog(self):
        with open(self.outputfile,'w',newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['datetime','job','file','user','detail:...'])
            writer.writerows(self.logbook)


if __name__=='__main__':
    tt = errorlogger('testy','mw',999)
    tt.writeLog(*['do','re','mi','fa','so','la','ti','do'])
    tt.finalizeLog()
    print(tt.filedest)
