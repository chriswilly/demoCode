"""
"""
import numpy as np


def fn_cartesian(x,y,a):
    dx = a*x - y - x*(x**2+y**2) + a*x**3/np.sqrt(x**2 + y**2)
    dy = x + a*y - y*(x**2+y**2) + a*x**2*y/np.sqrt(x**2 + y**2)
    return dx,dy

def ps2_8(x,y,a,b):
    dx = -x + a*y + x**2*y
    dy = b - a*y - x**2*y
    return dx,dy

def ps2_2(x,y):
    dx = x**2 - y**2
    dy = 2*x*y
    return dx,dy

def ps2_3(x,y,a):
    dx = -x
    dy = y + a*x**3
    return dx,dy


def ps1_2a(x,y,u):
    dx = 0
    dy = u*x
    return dx,dy

def ps1_2b(x,y,u):
    dx = 0
    dy = u*y
    return dx,dy

def ps1_3(x,y,u):
    dx = u*x*(x**2+y**2) - y
    dy = x + u*y*(x**2+y**2)
    return dx,dy


def ps1_4(x,y,v):
    dx = y
    dy = (v-x**2)*y - x
    return dx,dy

def ps1_6(x,y,z,r):
    dx = 10*(-x+y)
    dy = r*x - y - x*z
    dz = -8/3*z + x*y
