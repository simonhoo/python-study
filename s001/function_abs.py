#!/usr/bin/python
# -*- coding:utf-8 -*-
def t_abs(n1):
    return abs(n1)

def t_test():
    n1 = input("请数据一个负数:")
    n2 = t_abs(n1)
    print '%s的绝对值是: %s' %(n1,n2)

t_test()