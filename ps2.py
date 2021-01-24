#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 21:44:04 2021

@author: Michael
"""

from sympy import symbols, solve, expand, diff


def ps2_1():
    x, r = symbols('x, r')
    f = []
    f.append(x - r*x*(1-x))  #a
    f.append(r*x - x/(1+x**2))  #b
    f.append(1+ r*x + x**2)  #c
    f.append(r**2 - x**2)  #d
    print('\n______1______')
    [print('xo: ',solve(eqn,x),
           '\ndf/dx: ',expand(diff(eqn,'x')),
           '\nd2f/dx2: ',expand(diff(diff(eqn,'x'),'x')),
           '\ndf/dr: ',expand(diff(eqn,'r')),
           '\nd2f/dr2 : ',expand(diff(diff(eqn,'r'),'r')),
           '\nd2f/dxdr : ',expand(diff(diff(eqn,'x'),'r')),
           '\n') for eqn in f]
    # [print('df/dx: ',diff(eqn,'x')) for eqn in f]

def ps2_2():
    x, r = symbols('x, r')
    f = (r*x+x**3)*(r+2-x**2)
    print('\n______2______')
    print('f(x): ',expand(f))
    [print('xo: ',solve(f,x))]
    [print('df/dx: ',diff(f,'x'))]


def ps2_3b():
    x, h = symbols('x, h')
    f = x*(1-x)+h
    print('\n______3b______')
    print('f(x): ',expand(f))
    [print('xo: ',solve(f,x))]
    [print('df/dx: ',diff(f,'x'))]

def ps2_4b():
    x, r = symbols('x, r')
    f = -r*x+x**2/(1+x**2)
    print('\n______4b______')
    print('f(x): ',expand(f))
    [print('xo: ',solve(f,x))]
    [print('df/dx: ',diff(f,'x'))]

def ps2_5c():
    x, a = symbols('x, a')
    k=2
    f = a*x*(1-x/k)-x/(1+x)
    print('\n______5c______')
    print('f(x): ',expand(f))
    [print('xo: ',solve(f,a))]
    [print('df/dx: ',diff(f,'x'))]


if __name__=='__main__':
    ps2_1()
    ps2_2()
    ps2_3b()
    ps2_4b()
    ps2_5c()