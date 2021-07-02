from django.http import HttpResponse,JsonResponse
import json
from .models import Note

from django.core.serializers import serialize
# class Note(models.Model):
#     noteid = models.AutoField(primary_key=True)
#     userid = models.IntegerField()
#     note = models.CharField(max_length=1000,blank=True,null=True)
def addnote1(request):
    if request.POST:
        try:
            xhr = request.body.decode('utf-8')
            xhr = json.loads(xhr)
            print(xhr)
            usernamepost=xhr.get('username')
            addnotepost=xhr.get('addnote')
            print(xhr,usernamepost,addnotepost)
            newnote=Note(username=usernamepost,note=addnotepost)
            newnote.save()
            res={'result':'True','status_code':'00'}    #构造返回消息
            # res=serialize('json',res,ensure_ascii=False)
            return JsonResponse(data=res,safe=False)
        except:
            print('修改失败')
            res={'result':'False','status_code':'100'}
            # res=serialize('json',res,ensure_ascii=False)
            return HttpResponse(json.dumps(res), content_type='application/json')
def deletenote(request):
    if request.POST:
        try:
            xhr = request.body.decode('utf-8')
            xhr = json.loads(xhr)
            print(xhr)
            usernamepost=xhr.get('username')
            noteidpost=xhr.get('noteid')
            delnote=Note.objects.filter(username=usernamepost,noteid=noteidpost)
            if(not delnote):
                print('删除失败')
                response={'result':'False','status_code':'100'}
                return HttpResponse(json.dumps(response), content_type='application/json')
            else:
                delnote.delete()
                res={'result':'True','status_code':'00'}
                return JsonResponse(data=res,safe=False)
                print(usernamepost,res)
        except:
            print('删除失败')
            response={'result':'False','status_code':'100'}
            return HttpResponse(json.dumps(response), content_type='application/json')
def updatenote1(request):
    if request.POST:
        try:
            xhr = request.body.decode('utf-8')
            xhr = json.loads(xhr)
            print(xhr)
            usernamepost=xhr.get('username')
            noteidpost=int(xhr.get('noteid'))
            res=Note.objects.filter(noteid=noteidpost,username=usernamepost)
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
            res=[]
            res=serialize('json',res,ensure_ascii=False)
            return HttpResponse(res)
def  updatenote2(request):
    try:
        xhr = request.body.decode('utf-8')
        xhr = json.loads(xhr)
        print(xhr)
        noteidpost=xhr.get('noteid')
        usernamepost=xhr.get('username')
        notepost=xhr.get('note')
        newschedule=Note.objects.get(username=usernamepost,noteid=noteidpost)
        newschedule.note=notepost;
        newschedule.save()
        res={'result':'True','status_code':'00'}
        return JsonResponse(data=res,safe=False)
        print(usernamepost,res)
    except:
        print('添加失败')
        response={'result':'False','status_code':'100'}
        return HttpResponse(json.dumps(response), content_type='application/json')
def searchnote(request):
    if request.POST:
        try:
            xhr = request.body.decode('utf-8')
            xhr = json.loads(xhr)
            print('请求',xhr)
            usernamepost=xhr.get('username')
            print('取得',usernamepost)
            res=Note.objects.filter(username = usernamepost);
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
            res=[]
            res=serialize('json',res,ensure_ascii=False)
            return HttpResponse(res)