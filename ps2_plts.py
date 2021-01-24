#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 19:22:15 2021

@author: Michael
"""
import matplotlib as mpl
import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np

#matplotlibparameters
mpl.rcParams['axes.labelsize'] = 34
mpl.rcParams['axes.titlesize'] = 34
mpl.rcParams['xtick.labelsize'] = 30
mpl.rcParams['ytick.labelsize'] = 30
mpl.rcParams['lines.linewidth'] = 2
mpl.rcParams['lines.markersize'] = 18
mpl.rcParams['legend.framealpha'] = 0.95
mpl.rcParams['legend.fontsize'] = 26  #title_fontsize

def ps2_1a():
    title = 'PS2_1a'
    xo,xf = [-1, 2]
    ro,rf = [-1.5,1.5]
    R = np.linspace(ro,rf,7)

    X = np.linspace(xo,xf,1000)
    y = lambda x,r: x-r*x*(1-x)

    
    fig = plt.figure(figsize=(20,20))
    ax = fig.add_subplot(111)
    
    [ax.plot(X,y(X,r),label = 'f(x) = x-r*x*(1-x); r = {}'.format(round(r,2))) for r in R]

    plt.axis('tight')
    plt.title(title)
    ax.legend(loc=0)#7,2,6
    plt.grid(b=True, which='major', axis='both')
    ax.plot([X[0]-1,X[-1]+1],[0,0],'k')

    timestamp = datetime.now().strftime("%y%m%d_%H%M%S%f")
    plt.show()
    fig.savefig('plot_output/'+title+'_'+timestamp+'.png')
    plt.close(fig)


def ps2_1a_bif():
    title = 'PS2_1a_bif'
    xo,xf = [-1, 2]
    ro,rf = [-2,2]
    R = np.linspace(ro,rf,100)

    #X = np.linspace(xo,xf,1000)
    #y = lambda x,r: x-r*x*(1-x)
    g = lambda r: 1-1/r
    
    fig = plt.figure(figsize=(20,20))
    ax = fig.add_subplot(111)
    
    [ax.plot(R,g(R),label = 'x = 1-1/r')]

    plt.axis('tight')
    plt.title(title)
    ax.legend(loc=0)#7,2,6
    plt.grid(b=True, which='major', axis='both')
    ax.plot([R[0]-1,R[-1]+1],[0,0],'k')

    timestamp = datetime.now().strftime("%y%m%d_%H%M%S%f")
    plt.show()
    fig.savefig('plot_output/'+title+'_'+timestamp+'.png')
    plt.close(fig)



def ps2_1b():
    title = 'PS2_1b'
    xo,xf = [-2, 2]
    ro,rf = [-0.25,1.25]
    R = np.linspace(ro,rf,7)

    X = np.linspace(xo,xf,1000)
    y = lambda x,r: r*x-x/(1+x**2)

    
    fig = plt.figure(figsize=(20,20))
    ax = fig.add_subplot(111)
    
    [ax.plot(X,y(X,r),label = 'f(x) = r*x-x/(1+x$^2$); r = {}'.format(round(r,2))) for r in R]

    plt.axis('tight')
    plt.title(title)
    ax.legend(loc=0)#7,2,6
    plt.grid(b=True, which='major', axis='both')
    ax.plot([X[0]-1,X[-1]+1],[0,0],'k')

    timestamp = datetime.now().strftime("%y%m%d_%H%M%S%f")
    plt.show()
    fig.savefig('plot_output/'+title+'_'+timestamp+'.png')
    plt.close(fig)

def ps2_1c():
    title = 'PS2_1c'
    xo,xf = [-3, 3]
    ro,rf = [-3,3]
    R = np.linspace(ro,rf,7)

    X = np.linspace(xo,xf,1000)
    y = lambda x,r: 1+r*x+x**2

    
    fig = plt.figure(figsize=(20,20))
    ax = fig.add_subplot(111)
    
    [ax.plot(X,y(X,r),label = 'f(x) = 1+r*x+x$^2$; r = {}'.format(round(r,2))) for r in R]

    plt.axis('tight')
    plt.title(title)
    ax.legend(loc=0)#7,2,6
    plt.grid(b=True, which='major', axis='both')
    ax.plot([X[0]-1,X[-1]+1],[0,0],'k')

    timestamp = datetime.now().strftime("%y%m%d_%H%M%S%f")
    plt.show()
    fig.savefig('plot_output/'+title+'_'+timestamp+'.png')
    plt.close(fig)


def ps2_1d():
    title = 'PS2_1d'
    xo,xf = [-2, 2]
    ro,rf = [0,1]
    R = np.linspace(ro,rf,5)

    X = np.linspace(xo,xf,1000)
    y = lambda x,r: r**2-x**2

    
    fig = plt.figure(figsize=(20,20))
    ax = fig.add_subplot(111)
    
    [ax.plot(X,y(X,r),label = 'f(x) = r$^2$-x$^2$; r = {}'.format(round(r,2))) for r in R]

    plt.axis('tight')
    plt.title(title)
    ax.legend(loc=0)#7,2,6
    plt.grid(b=True, which='major', axis='both')
    ax.plot([X[0]-1,X[-1]+1],[0,0],'k')

    timestamp = datetime.now().strftime("%y%m%d_%H%M%S%f")
    plt.show()
    fig.savefig('plot_output/'+title+'_'+timestamp+'.png')
    plt.close(fig)


def ps2_2():
    title = 'PS2_2'
    xo,xf = [-1.75, 1.75]
    ro,rf = [-2.5,0.5]
    R = np.linspace(ro,rf,7)

    X = np.linspace(xo,xf,1000)
    y = lambda x,r: (r*x+x**3)*(r+2-x**2)

    
    fig = plt.figure(figsize=(20,20))
    ax = fig.add_subplot(111)
    
    [ax.plot(X,y(X,r),label = 'f(x) = (r*x+x$^3$)*(r+2-x$^2$); r = {}'.format(round(r,2))) for r in R]

    plt.axis('tight')
    plt.title(title)
    ax.legend(loc=0)#7,2,6
    plt.grid(b=True, which='major', axis='both')
    ax.plot([X[0]-1,X[-1]+1],[0,0],'k')

    timestamp = datetime.now().strftime("%y%m%d_%H%M%S%f")
    plt.show()
    fig.savefig('plot_output/'+title+'_'+timestamp+'.png')
    plt.close(fig)


def ps2_3b():
    title = 'PS2_3b'
    xo,xf = [-1,2]
    H = np.array([1/16,1/8, 1/4, 1/2, 1])
    X = np.linspace(xo,xf,1000)
    y = lambda x,h: x*(1-x)-h

    
    fig = plt.figure(figsize=(20,20))
    ax = fig.add_subplot(111)
    
    [ax.plot(X,y(X,h), label = 'f(x) = x*(1-x)-h; h = {}'.format('1/'+str(int(1/h)))) for h in H]

    plt.axis('tight')
    plt.title(title)
    ax.legend(loc=0)#7,2,6
    plt.grid(b=True, which='major', axis='both')
    ax.plot([X[0]-1,X[-1]+1],[0,0],'k')
    timestamp = datetime.now().strftime("%y%m%d_%H%M%S%f")
    plt.show()
    fig.savefig('plot_output/'+title+'_'+timestamp+'.png')
    plt.close(fig)

def ps2_4c():
    title = 'PS2_4c'
    xo,xf = [-1, 4]
    ro,rf = [0.1,0.7]
    R = np.linspace(ro,rf,4)

    X = np.linspace(xo,xf,1000)
    y = lambda x,r: -r*x+x**2/(1+x**2)

    
    fig = plt.figure(figsize=(20,20))
    ax = fig.add_subplot(111)
    
    [ax.plot(X,y(X,r),label = 'f(x) = -r*x+x$^2$/(1+x$^2$); r = {}'.format(round(r,2))) for r in R]

    plt.axis('tight')
    plt.title(title)
    ax.legend(loc=0)#7,2,6
    plt.grid(b=True, which='major', axis='both')
    ax.plot([X[0]-1,X[-1]+1],[0,0],'k')

    timestamp = datetime.now().strftime("%y%m%d_%H%M%S%f")
    plt.show()
    fig.savefig('plot_output/'+title+'_'+timestamp+'.png')
    plt.close(fig)





def ps2_5b():
    k=2
    
    title = 'PS2_5b' if k==1 else 'PS2_5c'
    xo,xf = [0, 2]
    ao,af = [0,1.2]
    #A = np.linspace(ao,af,9)
    A = np.arange(ao,af,2/9)

    X = np.linspace(xo,xf,1000)
    y = lambda x,a,k: a*x*(1-x/k)-x/(1+x)

    
    fig = plt.figure(figsize=(20,20))
    ax = fig.add_subplot(111)
    
    [ax.plot(X,y(X,a,k),label = 'f(x) = a*x*(1-x/k)-x/(1+x); k = {0}, a = {1}'.format(k,round(a,2))) for a in A]

    plt.axis('tight')
    plt.title(title)
    ax.legend(loc=0)#7,2,6
    plt.grid(b=True, which='major', axis='both')
    ax.plot([X[0]-1,X[-1]+1],[0,0],'k')

    timestamp = datetime.now().strftime("%y%m%d_%H%M%S%f")
    plt.show()
    fig.savefig('plot_output/'+title+'_'+timestamp+'.png')
    plt.close(fig)
    
    


if __name__ == "__main__":
    #ps2_1a()
    #ps2_1a_bif()
    #ps2_1b()
    #ps2_1c()
    #ps2_1d()
    #ps2_2()
    #ps2_3b()
    #ps2_4c()
    ps2_5b()
