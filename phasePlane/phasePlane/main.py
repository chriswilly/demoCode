from phasePlot import phasePlot
# from lib.plotformat import setup
from lib.functions import (ps1_3 as problem3,
                           ps1_4 as problem4,
                           fn_cartesian,
                           )


"""acting unittests file for now"""

if __name__=='__main__':
    # print('will transfer calls to this file')
    # fmt = setup()
    # print(fmt.directory)

    cnsts = [{'a':-4,},
             {'a':-1/4,},
             {'a':-1/8,},
             {'a':0,},
             {'a':1/8,},
             {'a':1/2,},
             {'a':2,}
             ]

    aa = phasePlot(problem3,'problem3')
    bb = phasePlot(problem4,'problem4')

    [aa.phase_plane(*[-2,2],**c) for c in cnsts]
    [bb.phase_plane(*[-4,4],**c) for c in cnsts]
