#!/usr/bin/python
# -*- coding:utf-8 -*-

from  urllib import urlopen, urlretrieve

def open_url(url):
    html = urlopen(url)
    htmlCode = html.read()
    html.close()
    print htmlCode
    return htmlCode

def t_download(url,localfile):
    urlretrieve(url,localfile)


open_url("http://www.baidu.com")
t_download(r'https://ss0.bdstatic.com/5aV1bjqh_Q23odCf/static/superman/img/logo/bd_logo1_31bdc765.png',r'/Users/simon/Downloads/baidu_logo.png')