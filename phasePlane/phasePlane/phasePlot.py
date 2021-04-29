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
        self.title = output.replace('plot_output','')
        self.fmt = setup(self.title)
        self.function = function



    def phase_plane(self,
                    *args:list,
                    **kwargs:dict):
        """ use this as pplane plotting function for given input function """
        plot_title = self.title
        if kwargs.items():
            # print(kwargs)
            for name,value in kwargs.items():
                plot_title+=''.join('{0}={1} '.format(name,value))
            if len(kwargs.values()) == 2:
                a,b =  itemgetter('a','b')(kwargs) # map(kwargs.get, ('a'))
            if len(kwargs.values()) == 1:
                a =  itemgetter('a')(kwargs) # map(kwargs.get, ('a'))
                b = None
        else:
            a,b= [1,0]

        if args:
            xo,xf = args
        else:
            xo,xf = [-3,3]

        dx  = (xf-xo)/64
        xval, yval = np.meshgrid(np.arange(xo, xf, dx),
                                 np.arange(xo, xf, dx))

        # scale = (xf-xo)/np.sqrt(xo**2+xf**2)
        nx = 6
        dd = (xf-xo)/nx/2
        x0,y0 = np.meshgrid(np.linspace(xo+dd,xf-dd,nx),
                            np.linspace(xo+dd,xf-dd,nx))
        X0 = np.array([x0.flatten(),y0.flatten()]).T

        if kwargs.items():
            if len(kwargs.values()) == 2:
                xdot,ydot = self.function(xval,yval,a,b)
            if len(kwargs.values()) == 1:
                xdot,ydot = self.function(xval,yval,a)
        else:
            xdot,ydot = self.function(xval,yval)

        # Quiver plot
        fig = plt.figure(figsize=(20,20))
        ax = fig.add_subplot(111)
        plt.quiver(xval, yval, xdot, ydot, headwidth=1, headlength=2)
        plt.streamplot(xval, yval, xdot, ydot, color='r',
                       arrowsize=3,start_points=X0, integration_direction='forward'
                       )
        ax.plot(X0[...,0],X0[...,1],'ro',fillstyle='none')
        # fixed point
        if b:
            if not b<0:
                ax.plot(b,b/(a+b**2),'bo')
        plt.axis('tight')
        # ax.legend(loc=3)
        plt.title(plot_title)
        plt.grid(b=True, which='major', axis='both')
        # plt.show()
        fig.savefig(self.fmt.plot_name(plot_title,'png'))

#########################


if __name__=='__main__':
    print('internal unit test not set up :(')
