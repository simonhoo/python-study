#!/usr/bin/python
# -*- coding:utf-8 -*-

# Months
months = [
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December'
]
print months

# 日期尾词
endings = ['st','nd','rd'] + 17 * ['th'] + ['st','nd','rd'] + 7 * ['th'] + ['st']
print endings

year = raw_input("请输入年份:")
month = raw_input("请输入月份:")
day = raw_input("请输入日期:")

month_n = int(month)
day_n = int(day)

month_name = months[month_n-1]
day_name = day + endings[day_n-1]

print '%s %s, %s' %(month_name,day_name,year)