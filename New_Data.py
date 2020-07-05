import os,django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "China_nCoV.settings")# project_name 项目名称
django.setup()
import requests
import json
import re
from app01.models import *
import time,datetime

def get_All_Data():
    url = 'https://voice.baidu.com/newpneumonia/get?target=trend&isCaseIn=0&stage=publish&callback=jsonp_1593671378926_622'
    r = requests.get(url)
    list_cov = re.findall('\((.*?)\)',r.text)[0]
    s = json.loads(list_cov)['data']

    for city in s:
        city_name = city['name']
        trend = city['trend']
        updateDate_list = trend['updateDate']
        diagnosis_list = trend['list'][0]['data']
        cure_list = trend['list'][1]['data']
        dead_list = trend['list'][2]['data']
        new_diagnosis_list = trend['list'][3]['data']
        model_id = App01Cities.objects.get(city=city_name).id
        sql_update = App01Detail.objects.filter(city_id=model_id).values('updateDate')
        for updateDate,diagnosis,cure,dead,new_diagnosis in zip(updateDate_list,diagnosis_list,cure_list,dead_list,new_diagnosis_list):
            flag = 0
            updateDate = '2020.{}'.format(updateDate).replace('.','-')
            date_str = datetime.datetime.strptime(updateDate,'%Y-%m-%d')
            updateDate = str(date_str).split(' ')[0]
            for sql in sql_update:
                if str(sql['updateDate']) == updateDate:
                    flag = 1
                    break
            if flag == 0:
                detail_models = App01Detail(updateDate=updateDate,diagnosis=diagnosis,cure=cure,dead=dead,new_diagnosis=new_diagnosis,city_id=model_id)
                detail_models.save()
    print('success')

def get_News():
    url = 'https://opendata.baidu.com/data/inner?tn=reserved_all_res_tn&dspName=iphone&from_sf=1&dsp=iphone&resource_id=28565&alr=1&query=%E8%82%BA%E7%82%8E&cb=jsonp_1593687822778_60442'
    r = requests.get(url)
    s = re.findall('\((.*?)\)',r.text)[0]
    news_list = json.loads(s)['Result'][0]['DisplayData']['result']['items']
    for news in news_list:
        flag = 0
        news_title = news['eventDescription']
        news_url = news['eventUrl']
        news_time = time.localtime(int(news['eventTime']))
        news_time = time.strftime('%Y-%m-%d %H:%M:%S',news_time)
        for sql in App01News.objects.all().values('title'):
            if sql['title'] == news_title:
                flag = 1
                break
        if flag == 0:
            news_models = App01News(title=news_title,url=news_url,date=news_time)
            news_models.save()
    print('success')

if __name__ == '__main__':
    # get_All_Data() #插入全部历史数据
    get_All_Data() #插入所有新冠新闻
    # pass