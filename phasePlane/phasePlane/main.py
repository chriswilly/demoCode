from phasePlot import phasePlot
# from lib.plotformat import setup
from lib.functions import (ps2_8 as problem8,
                           ps2_2 as problem2,
                           ps2_3 as problem3,
                           fn_cartesian,
                           )


"""acting unittests file for now"""

if __name__=='__main__':
    # print('will transfer calls to this file')
    # fmt = setup()
    # print(fmt.directory)
    acnst = 1/8/2
    cnsts = [
             {'a':acnst,'b':-1/8,},
             {'a':acnst,'b':0,},
             {'a':acnst,'b':1/8,},
             {'a':acnst,'b':1/4,},
             {'a':acnst,'b':1/2,},
             {'a':acnst,'b':3/4,},
             {'a':acnst,'b':1,},
             ]

    aa = phasePlot(problem8,'problem 8 ')
    bb = phasePlot(problem2,'problem 2 ')
    cc = phasePlot(problem3,'problem 3 ')
    # [aa.phase_plane(*[0,3],**c) for c in cnsts]
    # bb.phase_plane()
    cc.phase_plane(**{'a' : 1/10})
