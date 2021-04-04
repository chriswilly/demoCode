#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 03:11:06 2021
modified into class on Sun Apr 4 ~13:00 2021
@author: Michael W
"""

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from operator import itemgetter
from lib.plotformat import setup


class phasePlot:

    def __init__(self,
                 function,
                 output:str = 'plot_output'):
        self.fmt = setup(output)
        self.function = function



    def phase_plane(self,
                    *args:list,
                    **kwargs:dict):
        """ use this as pplane plotting function for given input function """
        title=''
        if kwargs.items():
            # print(kwargs)
            for name,value in kwargs.items():
                title+=''.join('{0}={1} '.format(name,value))
            a =  itemgetter('a')(kwargs) # map(kwargs.get, ('a'))
        else:
            a=-1/4

        if args:
            xo,xf = args
        else:
            xo,xf = [-3,3]

        dx  = (xf-xo)/32
        xval, yval = np.meshgrid(np.arange(xo, xf, dx),
                                 np.arange(xo, xf, dx))

        scale = np.min([xo,xf])/np.sqrt(xo**2+xf**2)
        X0 = scale*np.array([
                            [0.5,0.5],
                            [-1,1],
                            [-1,-1],
                            [1,-1],
                            [1,1],
                            [-0.5,1.5],
                            [0.5,-1.5],
                            [-1.5,-0.5],
                            [1.5,0.5]
                            ])


        xdot,ydot = self.function(xval,yval,a)

        # Quiver plot
        fig = plt.figure(figsize=(20,20))
        ax = fig.add_subplot(111)
        plt.quiver(xval, yval, xdot, ydot, headwidth=2, headlength=3)
        plt.streamplot(xval, yval, xdot, ydot, color='r',
                       arrowsize=3,start_points=X0, integration_direction='both'
                       )
        plt.axis('tight')
        # ax.legend(loc=3)
        plt.title(title)
        plt.grid(b=True, which='major', axis='both')
        # plt.show()
        fig.savefig(self.fmt.plot_name(title,'png'))



def fn_cartesian(x,y,a):

    dx = a*x - y - x*(x**2+y**2) + a*x**3/np.sqrt(x**2 + y**2)
    dy = x + a*y - y*(x**2+y**2) + a*x**2*y/np.sqrt(x**2 + y**2)
    return dx,dy




def problem6():
    """AMATH502 final p6"""
    aa = phasePlot(fn_cartesian)

    cnsts = [{'a':-1/2,},
             {'a':-1/4,},
             {'a':-1/8,},
             {'a':0,},
             {'a':1/8,},
             {'a':1/4,},
             {'a':1/2,}
             ]
    [aa.phase_plane(*[-2,2],**c) for c in cnsts]


if __name__=='__main__':
    problem6()
