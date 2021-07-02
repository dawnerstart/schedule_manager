from django.test import TestCase
from django.http import HttpResponse,JsonResponse
from .models import User

from django.core.serializers import serialize
import json
# Create your tests here.
def test(request):
        try:
            return HttpResponse('test成功')
            response=User.objects.filter(username=1)
            
            print(response)
            print('\n')
            # print(json.dumps(response))
            print('\n')
            # for i in response:
            #     print(i['fields'])
            # response=HttpResponse('ok')
            # response.set_cookie('key','value') 
            # if not response:
                # return HttpResponse('搜索失败！')
            # else:
            # response.append({'result':'True'})
            response=serialize('json',response,ensure_ascii=False)
            print(response)
            return HttpResponse(response, content_type = 'application/json')
            return JsonResponse(response)
                # response=serialize('json',response,ensure_ascii=False)
                # return HttpResponse(response, content_type = 'application/json')
        except:
            return HttpResponse('搜索失败！')
# [{"model": "taskmodel.user", "pk": 1, "fields": {"username": "20170602310032", "password": "thisis111", "age": "2021-05-12", "email": "admin@1.com", "phone": "18976652082", "address": "香港仔湖北街12號裕景中心"}}, {"model": "taskmodel.user", "pk": 2, "fields": {"username": "1111", "password": "1111111", "age": "2021-05-16", "email": "g@1.com", "phone": "18976652082", "address": "香港"}}]