#!/usr/bin/python
# -*- coding:utf-8 -*-
def t_pow(n1,n2):
    return pow(n1,n2)

def t_pow1(n1,n2):
    return n1 ** n2

def t_test():
    n1 = input("输入数字1:")
    n2 = input("输入数字2:")

    n3 = t_pow(n1,n2)
    print  'pow(%s,%s) = %s' %(n1,n2,n3)

def t_test1():
    n1 = input("输入数字1:")
    n2 = input("输入数字2:")

    n3 = t_pow1(n1, n2)
    print  '%s ** %s = %s' % (n1, n2, n3)

print '第一种方法:'
t_test()

print '\n第二种方法:'
t_test1()