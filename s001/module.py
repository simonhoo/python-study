#!/usr/bin/python
# -*- coding:utf-8 -*-

import math

def t_math(n1):
    nf = math.ceil(n1)
    ng = math.floor(n1)
    nh = math.frexp(n1)

    print 'ceil:%s,floor:%s,frexp:%s' %(nf,ng,nh)

def t_test():
    n1 = input("请输入一个数字:")
    t_math(n1)

t_test()