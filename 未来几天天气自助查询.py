# -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 16:50:01 2018

@author: Administrator
"""
import urllib.request as r
import time
print('欢迎使用天气自助查询系统')
time.sleep(3)
print('本系统将为你提供未来3小时的天气预报')
url='http://api.openweathermap.org/data/2.5/forecast?q={},cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
city=input('请输入你需要查询天气的城市(拼音)：')
info=r.urlopen(url.format(city)).read().decode('utf-8','ignore')
import json
data=json.loads(info)
lists=data['list']
for i in range(0,38,4):
    temper={'时间':lists[i]['dt_txt'],
            '当前温度':lists[i]['main']['temp'],
        '当前时段最高温度为':lists[i]['main']['temp_max'],
        '当前时段最低温度为':lists[i]['main']['temp_min'],
        '压强':lists[i]['main']['pressure'],
        '天气情况':lists[i]['weather'][0]['description'],
        '风速':lists[i]['wind']['speed']}
    print('{}\n{}的当前温度为{},当前时段的最高温度为{},当前时段的最低温度为{},压强为{},天气情况：{},风速：{}'
      .format(temper['时间'],city,temper['当前温度'],temper['当前时段最高温度为'],temper['当前时段最低温度为'],temper['压强'],temper['天气情况'],temper['风速']))

