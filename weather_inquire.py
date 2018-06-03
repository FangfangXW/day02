# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 18:37:00 2018

@author: Administrator
"""

def weather(info):
#把info改成json类型
    import json
    data=json.loads(info)
#提取所需内容并打印
    lists=data['list']
    print('更新时间：{}'.format(lists[2]['dt_txt']))
    temper={'当前温度':lists[2]['main']['temp'],
        '最高温度为':lists[2]['main']['temp_max'],
        '最低温度为':lists[2]['main']['temp_min'],
        '压强':lists[2]['main']['pressure'],
        '天气情况':lists[2]['weather'][0]['description'],
        '风速':lists[2]['wind']['speed']}
    wearesult=('天气情况\t{}\n当前温度\t{}\n最高温度\t{}\n最低温度\t{}\n压强\t{}\n风速\t{}\n'
      .format(temper['天气情况'],temper['当前温度'],temper['最高温度为'],temper['最低温度为'],temper['压强'],temper['风速']))
    return print(wearesult)

def weather1(info):
    print('\n未来几天天气情况:')
    import json
    data1=json.loads(info)
    lists1=data1['list']
    print('更新时间：{}'.format(lists1[2]['dt_txt']))
    for i in range(0,len(lists1)):
        day=lists1[i]
        time=day['dt_txt']
        temp=day['main']['temp']
        description=day['weather'][0]['description']
        temp_max=day['main']['temp_max']
        pressure=day['main']['pressure']
        if lists1[i]['dt_txt'][9]==lists1[i-1]['dt_txt'][9]:
            print('时间：{}-温度{}-天气情况[{}]-最高温度{}-气压为{}'
              .format(time[11:19],temp,description,temp_max,pressure))
        else:
            print('\n')
            print('日期：{}\n'.format(time[0:10]))
            print('时间：{}-温度{}-天气情况[{}]-最高温度{}-气压为{}'
              .format(time[11:19],temp,description,temp_max,pressure))

    
    

#联网
import urllib.request as r
print('欢迎使用天气自助查询系统\n')
print('本系统将为你提供未来3小时的天气预报\n')
print('当前城市：北京\n')
print('菜单:\n1.查看当前城市天气\n2.查看其它城市天气')
menno=input('请输入菜单选择你说需要的服务：')
if menno=='1':
    url='http://api.openweathermap.org/data/2.5/forecast?q=beijing,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
    info1=r.urlopen(url).read().decode('utf-8','ignore')
    weather(info1)
    weather1(info1)
elif menno=='2':
    url='http://api.openweathermap.org/data/2.5/forecast?q={},cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
    city=input('请输入你需要查询天气的城市(拼音)：')
    info2=r.urlopen(url.format(city)).read().decode('utf-8','ignore')
    weather(info2)
    weather1(info2)
    
else:
    print('你输入的菜单有误,请重新输入：')


input('请输入OK退出:')



