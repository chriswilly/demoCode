"""
"""
import numpy as np


def fn_cartesian(x,y,a):
    dx = a*x - y - x*(x**2+y**2) + a*x**3/np.sqrt(x**2 + y**2)
    dy = x + a*y - y*(x**2+y**2) + a*x**2*y/np.sqrt(x**2 + y**2)
    return dx,dy




def ps1_3(x,y,u):
    dx = u*x*(x**2+y**2) - y
    dy = x + u*y*(x**2+y**2)
    return dx,dy


def ps1_4(x,y,v):
    dx = y
    dy = (v-x**2)*y - x
    return dx,dy
