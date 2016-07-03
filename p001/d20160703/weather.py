#!/usr/bin/python
# -*- coding:utf-8 -*-

#import modules:
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import urllib,urllib2,json

#创建一个类
class Weather(object):
    # 初始化函数,程序一启动就会执行
    def __init__(self):
        self.url = 'http://www.zuimeitianqi.com/zuimei/queryWeather'
        self.headers = {}
        self.headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.84 Safari/537.36'
        self.cities = {}
        self.cities['深圳'] = '01010715'
        self.cities['武汉'] = '01011410'
        self.cities['北京'] = '01010101'
        self.cities['襄樊'] = '01011412'
        self.data = {}
        self.city = '深圳'


    def query(self,city='深圳'):
        if city not in self.cities:
            print '当前城市暂不支持查询。'
            return None
        self.city = city;
        data = urllib.urlencode({'cityCode':self.cities[self.city]}).encode('utf-8')
        request = urllib2.Request(self.url,data,self.headers)
        response = urllib2.urlopen(request)
        html = response.read().decode('utf-8')
        #print  html

        return html

    def json_parser(self,html):
        target = json.loads(html)
        higth_temp = target['data'][0]['actual']['high']
        low_temp = target['data'][0]['actual']['low']
        current_tm = target['data'][0]['actual']['PTm']
        current_desc = target['data'][0]['actual']['desc']
        air = target['data'][0]['air']['aqigrad']

        #print higth_temp + '\n' + low_temp + '\n' + current_tm + '\n' + current_desc + '\n' + air
        print '城市:%s\n气温:%s-%s摄氏度\n当前时间:%s\n出行建议:%s\n空气质量:%s' %(self.city,low_temp,higth_temp,current_tm,current_desc,air)

if __name__ == '__main__':
    weather = Weather()
    html = weather.query("深圳")
    if html is not None:
        weather.json_parser(html)
