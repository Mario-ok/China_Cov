from django.shortcuts import render,HttpResponse,redirect
import time
import json
from utils import utils
# Create your views here.
def get_time(request):
    return HttpResponse(utils.get_time())

def get_num(request):
    return HttpResponse(json.dumps(utils.get_num()),content_type='application/json')

def get_all_day(request):
    s = utils.get_all_day()
    k = list(s.keys())
    v = s.values()
    v1 = []
    v2 = []
    v3 = []
    for i in v:
        v1 = v1 + [i[0]]
        v2 = v2 + [i[1]]
        v3 = v3 + [i[2]]
    return HttpResponse(json.dumps({'key':k,'value1':v1,'value2':v2,'value3':v3}),content_type='application/json')

def get_new_cov(request):
    s = utils.get_new_cov()
    k = list(s.keys())[-20:]
    v = list(s.values())[-20:]
    return HttpResponse(json.dumps({'key': k, 'value':v}),
                        content_type='application/json')

def get_china(request):
    return HttpResponse(json.dumps(utils.get_china()),content_type='application/json')

def get_news(request):
    s = list(utils.get_news())
    for i in s:
        title = i['title']
        i['date'] = str(i['date']).split(' ')[0]
        if len(title)>19:
            i['title'] = str(title)[:19] + '...'
    return HttpResponse(json.dumps(s),content_type='application/json')

def main(request):
    return render(request,'main.html')
