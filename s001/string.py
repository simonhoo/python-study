#!/usr/bin/python
# -*- coding:utf-8 -*-

def t_str():
    print  str(1000)

def t_repr():
    print repr('1000L')

def t_backquote():
    print `1000L`

def t_long_str():
    print '''这是第一行,
这是第二行,
这是第三行,
这是最后一行。
'''

def t_r_str():
    print r'C:\test\adfd\fa'

t_str()
t_repr()
t_backquote()
t_long_str()
t_r_str()