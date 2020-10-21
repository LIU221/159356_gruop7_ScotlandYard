from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.db.models import Max
from django.http.response import JsonResponse
import json
from .models import *

def register(request):
    # if (request.method == 'POST'):
    post = json.loads(request.body)
    userId = post.get('userId')
    sex = post.get('sex')
    phone = post.get('phone')
    password = post.get('password')

    try:
        if Users.objects.get(userId=userId) is not None:
            return HttpResponse(-1)
    except:
        pass
    print("用户信息添加")

    # 创建数据库对象
    users = Users()
    users.userId = userId
    users.sex = sex
    users.phone = phone
    users.password = password
    try:
        users.save()
    except:
        print("异常====")
        return HttpResponse(-2)
    return HttpResponse(1)
    # context['hello'] = 'Hello World!'
    # return render(request, 'hello.html', context)


def login(request):
    print("===dologin==")
    body = json.loads(request.body)
    userId = body.get('userId')
    password = body.get('password')
    print(password, userId)
    print("userId===" + userId + ",password==" + password)
    # 对用户名和密码进行校验
    users = Users.objects.filter(userId=userId)
    if len(users) == 1:
        print(users[0].password, password)
        if users[0].password == password:
            print("true password:" + users[0].password)
            #  登陆成功  1
            return HttpResponse(1)
        else:
            # 你输入的用户密码有误 -1
            return HttpResponse(-1)
    else:
        # 你输入的用户名称不正确 -2
        return HttpResponse(-2)
