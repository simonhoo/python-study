#!/usr/bin/python
# -*- coding:utf-8 -*-

import  web

urls = {
    '/','Index',
    'login','Login',
}

app = web.application(urls,globals())

render = web.template.render('templates')

class Index():
    def GET(self):
        return render.index()

class Login():
    def POST(self):
        web.header('Content-Type', 'text/html; charset=utf-8')
        data = web.input()
        userName = data.get('userName')
        password = data.get('password')

        if userName == 'admin' and password == '123456':
            return '登录成功'
        return '账号或密码错误'

        return render.login()

if __name__ == '__main__':
    app.run()