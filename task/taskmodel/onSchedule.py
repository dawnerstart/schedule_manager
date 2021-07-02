from django.http import HttpResponse,JsonResponse
import json,time
from .models import Schedule

from django.core.serializers import serialize
# class Schedule(models.Model):
#     scheduleid = models.AutoField(primary_key=True)
#     userid = models.IntegerField()
#     scheduletime = models.DateField(auto_now_add=True)
#     scheduleevent = models.CharField(max_length=1000)
#     done = models.BooleanField(auto_created=False)
def addschedule(request):
    if request.POST:
        try:
            xhr = request.body.decode('utf-8')
            xhr = json.loads(xhr)
            print(xhr)
            usernamepost=xhr.get('username')
            scheduledatepost=xhr.get('scheduledate')
            scheduletimepost=xhr.get('scheduletime')
            print(type(scheduletimepost),scheduletimepost)
            scheduletimepost+=':00'
            print(type(scheduletimepost),scheduletimepost)
            scheduleeventpost=xhr.get('scheduleevent')
            if(scheduleeventpost==''):
                print('添加失败')
                response={'result':'False','status_code':'100'}
                return HttpResponse(json.dumps(response), content_type='application/json')
            donepost=1
            newschedule=Schedule(username=usernamepost,scheduledate=scheduledatepost,scheduletime=scheduletimepost,scheduleevent=scheduleeventpost,done = donepost)
            newschedule.save()
            res={'result':'True','status_code':'00'}
            return JsonResponse(data=res,safe=False)
            print(usernamepost,res)
        except:
            print('添加失败')
            response={'result':'False','status_code':'100'}
            return HttpResponse(json.dumps(response), content_type='application/json')
def deleteschedule(request):
    if request.POST:
        try:
            xhr = request.body.decode('utf-8')
            xhr = json.loads(xhr)
            print(xhr)
            usernamepost=xhr.get('username')
            scheduleidpost=xhr.get('scheduleid')
            delschedule=Schedule.objects.filter(username=usernamepost,scheduleid=scheduleidpost)
            if(not delschedule):
                print('删除失败')
                response={'result':'False','status_code':'100'}
                return HttpResponse(json.dumps(response), content_type='application/json')
            else:
                delschedule.delete()
                res={'result':'True','status_code':'00'}
                return JsonResponse(data=res,safe=False)
                print(usernamepost,res)
        except:
            print('删除失败')
            response={'result':'False','status_code':'100'}
            return HttpResponse(json.dumps(response), content_type='application/json')
def  updateschedule1(request):
    try:
        xhr = request.body.decode('utf-8')
        xhr = json.loads(xhr)
        print(xhr)
        usernamepost=xhr.get('username')
        scheduleidpost=int(xhr.get('scheduleid'))
        res=Schedule.objects.filter(scheduleid=scheduleidpost,username=usernamepost)
        # print(res)
        res=serialize('json',res,ensure_ascii=False)
        if not res:
            res=serialize('json',res,ensure_ascii=False)
            print('失败1')
            return HttpResponse(res)
        else:
            # res.append({'result':'True'})
            print(res)
            return HttpResponse(res)
    except:
        print('查询失败2')
        res=serialize('json',res,ensure_ascii=False)
        return HttpResponse(res)

def  updateschedule2(request):
    try:
        xhr = request.body.decode('utf-8')
        xhr = json.loads(xhr)
        print(xhr)
        scheduleidpost=xhr.get('scheduleid')
        usernamepost=xhr.get('username')
        scheduledatepost=xhr.get('scheduledate')
        scheduletimepost=xhr.get('scheduletime')
        scheduleeventpost=xhr.get('scheduleevent')
        newschedule=Schedule.objects.get(username=usernamepost,scheduleid=scheduleidpost)
        newschedule.scheduledate=scheduledatepost;
        newschedule.scheduletime=scheduletimepost;
        newschedule.scheduleevent=scheduleeventpost;
        newschedule.save()
        res={'result':'True','status_code':'00'}
        return JsonResponse(data=res,safe=False)
        print(usernamepost,res)
    except:
        print('添加失败')
        response={'result':'False','status_code':'100'}
        return HttpResponse(json.dumps(response), content_type='application/json')

def searchschedule(request):
    if request.POST:
        try:
            xhr = request.body.decode('utf-8')
            xhr = json.loads(xhr)
            print('请求',xhr)
            usernamepost=xhr.get('username')
            donepost=xhr.get('done')
            print('取得',usernamepost)
            if(donepost=='11'):
                res=Schedule.objects.filter(username = usernamepost);
            else:
                donepost=int(donepost)
                res=Schedule.objects.filter(username = usernamepost,done = donepost);
            print('搜库',res)
            res=serialize('json',res,ensure_ascii=False)
            if not res:
                res=serialize('json',res,ensure_ascii=False)
                print('失败1')
                return HttpResponse(res)
            else:
                # res.append({'result':'True'})
                print(res)
                return HttpResponse(res)
        except:
            res=serialize('json',res,ensure_ascii=False)
            return HttpResponse(res)
def set_done_schedule(request):
    if request.POST:
        try:
            xhr = request.body.decode('utf-8')
            xhr = json.loads(xhr)
            print(xhr)
            usernamepost=xhr.get('username')
            scheduleidpost=xhr.get('scheduleid')
            set_done_schedule1=Schedule.objects.get(username=usernamepost,scheduleid=scheduleidpost)
            if(not set_done_schedule1):
                print('发生问题1')
                response={'result':'False','status_code':'100'}
                return HttpResponse(json.dumps(response), content_type='application/json')
            else:
                set_done_schedule1.done=0;
                set_done_schedule1.save()
                res={'result':'True','status_code':'00'}
                return JsonResponse(data=res,safe=False)
                print(usernamepost,res)
        except:
            print('发生问题')
            response={'result':'False','status_code':'100'}
            return HttpResponse(json.dumps(response), content_type='application/json')