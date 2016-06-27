#!/usr/bin/python
# -*- coding:utf-8 -*-
def keybord_input():
    v = raw_input('请录入字符串:')
    print v

    n1 = input('请录入数字a:')
    n2 = input('请录入数字b:')
    nr = n1 * n2
    print "%d * %d = %d" %(n1,n2,nr)


keybord_input()