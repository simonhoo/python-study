#!/usr/bin/python
# -*- coding:utf-8 -*-

from Tkinter import  *
import tkMessageBox
import urllib
import urllib2

def btn_command():
    if inputNmae.get() =='':
        tkMessageBox.showinfo('提示','请输入姓名。')
    else:
        design(inputNmae.get().encode('utf-8'))


def post(url, data):
    request = urllib2.Request(url)
    urllib.urlencode(data)
    html = urllib2.urlopen(url, data)
    print html.read()

def design(inputName):
    url = 'http://www.jiqie.com/a/re22.php'

    formData = {
        'id': inputName,
        'id1607': 'pihun',
        'id1606': 'jiqie',
        'id1': '800',
        'id2': '905',
        'id3': '#000000',
        'id4': '#000000',
        'id5': '#000000',
        'id6': '#000000'
    }

    post(url,formData)


if __name__ == '__main__':
    top = Tk() #创建一个窗口,并赋值给top
    top.title("生成个性签名")
    top.geometry("600x300+500+400")# 600x300: 长和宽, 500: 左为圆心,300: 上边
    #top.geometry("+500+400")
    top.resizable(width=False,height=False)

    labName = Label(top,text="姓名:")
    labName.grid(row=0,column=0)

    inputNmae = Entry(top)
    inputNmae.grid(row=0,column=1)

    btn = Button(top,text="设计签名",command=btn_command)
    btn.grid(row=0,column=2)


    top.mainloop()#不停循环给系统发消息
