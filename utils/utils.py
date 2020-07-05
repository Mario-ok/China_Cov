import os,django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "China_nCoV.settings")# project_name 项目名称
django.setup()
import time
from app01 import models

def get_time():
    time_str = time.strftime('%Y{}%m{}%d{} %X')
    return time_str.format('年','月','日')

def get_num():
    diagnosis = 0
    cure = 0
    dead = 0
    new_diagnosis = 0
    for id in range(1,35):
        obj = models.App01Detail.objects.filter(city_id=id).values('diagnosis','cure','dead','new_diagnosis').last()
        diagnosis += obj['diagnosis']
        cure += obj['cure']
        dead += obj['dead']
        new_diagnosis += obj['new_diagnosis']
    num_list = [diagnosis,cure,dead,new_diagnosis]
    return num_list

def get_all_day():
    Day_list = {}
    obj = models.App01Detail.objects.all().values('diagnosis', 'cure', 'dead','updateDate')
    day = models.App01Detail.objects.all().values('updateDate').distinct()
    for i in day:
        diagnosis = 0
        cure = 0
        dead = 0
        for j in obj:
            if j['updateDate'] == i['updateDate']:
                diagnosis += j['diagnosis']
                cure += j['cure']
                dead += j['dead']
        date = i['updateDate']
        day_list =[diagnosis,cure,dead]
        Day_list[str(date)] = day_list
    return Day_list

def get_new_cov():
    new_cov = {}
    obj = models.App01Detail.objects.all().values('new_diagnosis','updateDate')
    day = models.App01Detail.objects.all().values('updateDate').distinct()
    for i in day:
        new_diagnosis = 0
        for j in obj:
            if j['updateDate'] == i['updateDate']:
                new_diagnosis += j['new_diagnosis']
        date = i['updateDate']
        new_cov[str(date)] = new_diagnosis
    return new_cov

def get_china():
    city_list = []
    for id in range(1,35):
        city_dict = {}
        new_diagnosis = models.App01Detail.objects.filter(city_id=id).values('new_diagnosis').last()
        city_name = models.App01Cities.objects.get(id=id).city
        city_dict['name'] = city_name
        city_dict['value'] = new_diagnosis['new_diagnosis']
        city_list.append(city_dict)
    return city_list

def get_news():
    news_list = models.App01News.objects.all().values('title','url','date')
    return news_list

if __name__ == '__main__':
    get_new_cov()