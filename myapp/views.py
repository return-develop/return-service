from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.core import serializers
import json, hashlib, time
from django.conf import settings
from .models import User
from .models import Subject

@ensure_csrf_cookie
def user_login(request):
    return render(request, 'user_login.html')

def user_add_info(request):
    '''用户填写或修改个人信息'''
    dic = {}
    if request.method == 'POST':
        if request.POST:
            usernametemp = request.POST.get('username')
            sextemp = request.POST.get('sex')
            birthdaytemp = request.POST.get('birthday')
            phonetemp = request.POST.get('phone')
            realnametemp = request.POST.get('realname')
            schooltemp = request.POST.get('school')
            majortemp = request.POST.get('major')
            educationtemp = request.POST.get('education')
            infotemp = request.POST.get('info')
            hobbytemp = request.POST.get('hobby')
            prizetemp = request.POST.get('prize')
            skilltemp = request.POST.get('skill')
            alteruser = User.objects.get(username = usernametemp)
            alteruser.sex = sextemp
            alteruser.birthday = birthdaytemp
            alteruser.phone = phonetemp
            alteruser.realname = realnametemp
            alteruser.school = schooltemp
            alteruser.major = majortemp
            alteruser.education = educationtemp
            alteruser.info = infotemp
            alteruser.hobby = hobbytemp
            alteruser.prize = prizetemp
            alteruser.skill = skilltemp
            alteruser.save()
            dic['result_code'] = 200
            dic = json.dumps(dic)
            return HttpResponse(dic)
    else:
        dic['result_code'] = 400
        dic = json.dumps(dic)
        return HttpResponse(dic)

def user_view_info(request):
    '''用户查看个人信息'''
    dic = {}
    if request.method == 'POST':
        if request.POST:
            usernametemp = request.POST.get('username')
            if User.objects.filter(username__contains = usernametemp):
                usertemp = User.objects.filter(username__contains = usernametemp)
                dic['list'] = json.loads(
                    serializers.serialize("json", usertemp)
                )
                dic['result_code'] = 200
                dic = json.dumps(dic)
                return HttpResponse(dic)
    else:
        dic['result_code'] = 400
        dic = json.dumps(dic)
        return HttpResponse(dic)

def subject_add(request):
    '''新增学科分类'''
    dic = {}
    if request.method == 'POST':
        if request.POST:
            nametemp = request.POST.get('name')
            if Subject.objects.filter(name = nametemp):
                dic['result_code'] = 401
                dic = json.dumps(dic)
                return HttpResponse(dic)
            else:
                newsubject = Subject(name = nametemp)
                newsubject.save()
                dic['result_code'] = 200
                dic = json.dumps(dic)
                return HttpResponse(dic)
    else:
        dic['result_code'] = 400
        dic = json.dumps(dic)
        return HttpResponse(dic)
