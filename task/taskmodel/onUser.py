from django.http import HttpResponse,JsonResponse,response
import json,simplejson,traceback
from .models import User

from django.shortcuts import render,redirect
from django.contrib import messages
from django.core.serializers import serialize

from hashlib import sha1    ##  加密
# class User(models.Model):
#     userid=models.AutoField(primary_key=True)
#     username = models.CharField(max_length=20)
#     password = models.CharField(max_length=20)
#     age = models.DateField(auto_now_add=True,blank=True,null=True)
#     email = models.CharField(max_length=20,blank=True,null=True)
#     phone = models.CharField(max_length=20,blank=True,null=True)
#     address = models.CharField(max_length=20,blank=True,null=True)
def register(request):
    if request.POST:
        try:
            usernamepost=request.POST['username']
            passwordpost=request.POST['password']
            agepost=request.POST['age']
            emailpost=request.POST['email']
            phonepost=request.POST['phone']
            addresspost=request.POST['address']
            if(User.objects.filter(username=usernamepost) or User.objects.filter(email=emailpost)):
                print('注册失败')
                response={'result':'False','status_code':'100'}
                return HttpResponse(json.dumps(response), content_type='application/json')
            newuser=User(username=usernamepost,password=passwordpost,age=agepost,email=emailpost,phone=phonepost,address=addresspost)
            newuser.save()
            res={'result':'True','status_code':'00'}
            return JsonResponse(data=res,safe=False)
            print(usernamepost,res)
        except:
            print('注册失败')
            response={'result':'False','status_code':'100'}
            return HttpResponse(json.dumps(response), content_type='application/json')



def login1(request):
    if request.POST:
        try:
            xhr = request.body.decode('utf-8')
            xhr = json.loads(xhr)
            print(xhr)
            usernamepost=xhr.get('username')
            passwordpost=xhr.get('password')
            print(usernamepost,passwordpost)
            response=User.objects.filter(username=usernamepost,password=passwordpost)
            print(response)
            if not response:
                res={'result':'False','status_code':'00'}
                return JsonResponse(data=res,safe=False)
            else:
                res={'result':'True','status_code':'00','username':usernamepost}
                # res=redirect('/schedule.html')
                # res.set_cookie('username',usernamepost,max_age=10)
                # return(res)
                return JsonResponse(data=res,safe=False)
        except:
            res={'result':'False','status_code':'00'}
            return JsonResponse(data=res,safe=False)

def login(request):
    if request.POST:
        try:
            usernamepost=request.POST['username']
            passwordpost=request.POST['password']
            response=User.objects.filter(username=usernamepost,password=passwordpost).first()
            print(response,usernamepost)
            if not response:
                res={'result':'False1','status_code':'00'}
                return JsonResponse(data=res,safe=False)
            else:
                res={'result':'True','status_code':'00','username':usernamepost}
                # res=redirect('/schedule.html')
                # res.set_cookie('username',usernamepost,max_age=10)
                # return(res)
                return JsonResponse(data=res,safe=False)
        except:
            res={'result':'False2','status_code':'00'}
            return JsonResponse(data=res,safe=False)
def searchuser(request):
    if(request.POST):
        try:
            xhr = request.body.decode('utf-8')
            xhr = json.loads(xhr)
            print('请求',xhr)
            usernamepost=xhr.get('username')
            print('取得',usernamepost)
            res=User.objects.filter(username = usernamepost);
            print('搜库',res)
            # res=serialize('json',res,ensure_ascii=False)
            if not res:
                res=serialize('json',res,ensure_ascii=False)
                print('失败1')
                return HttpResponse(res)
            else:
                # res.append({'result':'True'})
                res=serialize('json',res,ensure_ascii=False)
                print(res)
                return HttpResponse(res)
        except:
            res=[];
            res=serialize('json',res,ensure_ascii=False)
            return HttpResponse(res)
def updateuser(request):
    if request.POST:
        try:
            xhr = request.body.decode('utf-8')
            xhr = json.loads(xhr)
            print(xhr)
            usernamepost=xhr.get('username')
            print(usernamepost)
            agepost=xhr.get('age')
            emailpost=xhr.get('email')
            phonepost=xhr.get('phone')
            addresspost=xhr.get('address')
            print(addresspost)
            upduser=User.objects.get(username=usernamepost)
            print(11111111111111111111111111,upduser)
            if (not upduser):
                print('修改失败')
                res={'result':'False','status_code':'100'}
                # res=serialize('json',res,ensure_ascii=False)
                return HttpResponse(json.dumps(res), content_type='application/json')
            else:
                upduser.age=agepost
                upduser.email=emailpost
                upduser.phone=phonepost
                upduser.address=addresspost
                print('1')
                upduser.save()
                print('保存成功')
                res={'result':'True','status_code':'00'}
                return JsonResponse(data=res,safe=False)
        except:
            traceback.print_exc()
            print('修改失败1')
            res={'result':'False','status_code':'100'}
            # res=serialize('json',res,ensure_ascii=False)
            return HttpResponse(json.dumps(res), content_type='application/json')
def deleteuser(request):
    if request.POST:
        try:
            usernamepost=request.POST['username']
            passwordpost=request.POST['password']
            deleteuser1=User.objects.filter(username=usernamepost,password=passwordpost)
            if deleteuser1==None:
                return HttpResponse('删除失败！')
            else:
                deleteuser1.delete()
                return HttpResponse('删除成功！')
        except:
            return HttpResponse('删除失败！')
def registertest(request):
    return render(request,'register.html')
def updatepassword(request):
    try:
        xhr = request.body.decode('utf-8')
        xhr = json.loads(xhr)
        print(xhr)
        emailpost=xhr.get('email')
        usernamepost=xhr.get('username')
        print(usernamepost)
        passwordpost=xhr.get('pwd1')
        upduser=User.objects.get(username=usernamepost,email=emailpost)
        print(11111111111111111111111111,upduser)
        if (not upduser):
            print('修改失败')
            res={'result':'False','status_code':'100'}
            # res=serialize('json',res,ensure_ascii=False)
            return HttpResponse(json.dumps(res), content_type='application/json')
        else:
            upduser.password=passwordpost
            print('1')
            upduser.save()
            print('保存成功')
            res={'result':'True','status_code':'00'}
            return JsonResponse(data=res,safe=False)
    except:
        traceback.print_exc()
        print('修改失败1')
        res={'result':'False','status_code':'100'}
        # res=serialize('json',res,ensure_ascii=False)
        return HttpResponse(json.dumps(res), content_type='application/json')