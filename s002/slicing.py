#!/usr/bin/python
# -*- coding:utf-8 -*-

def t_slicing_str():
    s = 'http://www.cottsoft.com'
    print s[7:]

def t_slicing_arry():
    ar = [1,2,3,4,5,6,7,8,9,0]
    print ar[4:]
    print ar[4:-2]
    print ar[-2:]
    print ar[:7]

def t_slicing_input():
    s = raw_input("请输入字符串:")
    n1 = input("请输入要截取的开始下标:")
    n2 = input("请输入要截取的结束下标:")

    if n1 >0 and n2>0:
        print s[n1:n2]
    elif n1 >0 and n2<=0:
        print s[n1:]
    elif n1<0 and n2>=0:
        print s[:n2]
    else:
        print s

def t_slicing_step_len():
    ar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    print ar[0:-1:2]

t_slicing_str()
t_slicing_arry()
t_slicing_input()
t_slicing_step_len()