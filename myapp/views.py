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
from .models import Subrelation
from .models import City
from .models import Cityrelation

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

def subject_delete(request):
    '''删除学科分类'''
    dic = {}
    if request.method == 'POST':
        if request.POST:
            nametemp = request.POST.get('name')
            delsubject = Subject.objects.get(name = nametemp)
            delsubject.delete()
            dic['result_code'] = 200
            dic = json.dumps(dic)
            return HttpResponse(dic)
    else:
        dic['result_code'] = 400
        dic = json.dumps(dic)
        return HttpResponse(dic)

def subject_update(request):
    '''修改学科分类'''
    dic = {}
    if request.method == 'POST':
        if request.POST:
            nametemp = request.POST.get('name')
            namenew = request.POST.get('namenew')
            altersubject = Subject.objects.get(name = nametemp)
            altersubject.name = namenew
            altersubject.save()
            dic['result_code'] = 200
            dic = json.dumps(dic)
            return HttpResponse(dic)
    else:
        dic['result_code'] = 400
        dic = json.dumps(dic)
        return HttpResponse(dic)

def subject_view(request):
    '''查看学科分类'''
    dic = {}
    if request.method == 'GET':
        subjecttemp = Subject.objects.filter()
        dic['list'] = json.loads(
            serializers.serialize("json", subjecttemp)
        )
        dic['result_code'] = 200
        dic = json.dumps(dic)
        return HttpResponse(dic)
    else:
        dic['result_code'] = 400
        dic = json.dumps(dic)
        return HttpResponse(dic)

def subrelation_add(request):
    '''新增学科关系'''
    dic = {}
    if request.method == 'POST':
        if request.POST:
            fathernametemp = request.POST.get('fathername')
            sonnametemp = request.POST.get('sonname')
            if Subject.objects.filter(name = fathernametemp):
                if Subject.objects.filter(name = sonnametemp):
                    if Subrelation.objects.filter(fathername = fathernametemp, sonname = sonnametemp):
                        dic['result_code'] = 401
                        dic = json.dumps(dic)
                        return HttpResponse(dic)
                    else:
                        newsubrelation = Subrelation(fathername = fathernametemp, sonname = sonnametemp)
                        newsubrelation.save()
                        dic['result_code'] = 200
                        dic = json.dumps(dic)
                        return HttpResponse(dic)
    else:
        dic['result_code'] = 400
        dic = json.dumps(dic)
        return HttpResponse(dic)

def subrelation_delete(request):
    '''删除学科关系'''
    dic = {}
    if request.method == 'POST':
        if request.POST:
            fathernametemp = request.POST.get('fathername')
            sonnametemp = request.POST.get('sonname')
            delsubrelation = Subrelation.objects.get(fathername = fathernametemp, sonname = sonnametemp)
            delsubrelation.delete()
            dic['result_code'] = 200
            dic = json.dumps(dic)
            return HttpResponse(dic)
    else:
        dic['result_code'] = 400
        dic = json.dumps(dic)
        return HttpResponse(dic)

def subrelation_update(request):
    '''修改学科关系'''
    dic = {}
    if request.method == 'POST':
        if request.POST:
            fathernametemp = request.POST.get('fathername')
            sonnametemp = request.POST.get('sonname')
            fathernamenew = request.POST.get('fathernamenew')
            sonnamenew = request.POST.get('sonnamenew')
            altersubrelation = Subrelation.objects.get(fathername = fathernametemp, sonname = sonnametemp)
            altersubrelation.fathername = fathernamenew
            altersubrelation.sonname = sonnamenew
            altersubrelation.save()
            dic['result_code'] = 200
            dic = json.dumps(dic)
            return HttpResponse(dic)
        else:
            dic['result_code'] = 400
            dic = json.dumps(dic)
            return HttpResponse(dic)

def subrelation_view(request):
    '''查看学科关系'''
    dic = {}
    if request.method == 'GET':
        subrelationtemp = Subrelation.objects.filter()
        dic['list'] = json.loads(
            serializers.serialize("json", subrelationtemp)
        )
        dic['result_code'] = 200
        dic = json.dumps(dic)
        return HttpResponse(dic)
    else:
        dic['result_code'] = 400
        dic = json.dumps(dic)
        return HttpResponse(dic)

def city_add(request):
    '''新增城市分类'''
    dic = {}
    if request.method == 'POST':
        if request.POST:
            nametemp = request.POST.get('name')
            if City.objects.filter(name = nametemp):
                dic['result_code'] = 401
                dic = json.dumps(dic)
                return HttpResponse(dic)
            else:
                newcity = City(name = nametemp)
                newcity.save()
                dic['result_code'] = 200
                dic = json.dumps(dic)
                return HttpResponse(dic)
    else:
        dic['result_code'] = 400
        dic = json.dumps(dic)
        return HttpResponse(dic)

def city_delete(request):
    '''删除城市分类'''
    dic = {}
    if request.method == 'POST':
        if request.POST:
            nametemp = request.POST.get('name')
            delcity = City.objects.get(name = nametemp)
            delcity.delete()
            dic['result_code'] = 200
            dic = json.dumps(dic)
            return HttpResponse(dic)
    else:
        dic['result_code'] = 400
        dic = json.dumps(dic)
        return HttpResponse(dic)

def city_update(request):
    '''修改城市分类'''
    dic = {}
    if request.method == 'POST':
        if request.POST:
            nametemp = request.POST.get('name')
            namenew = request.POST.get('namenew')
            altercity = City.objects.get(name = nametemp)
            altercity.name = namenew
            altercity.save()
            dic['result_code'] = 200
            dic = json.dumps(dic)
            return HttpResponse(dic)
    else:
        dic['result_code'] = 400
        dic = json.dumps(dic)
        return HttpResponse(dic)

def city_view(request):
    '''查看城市分类'''
    dic = {}
    if request.method == 'GET':
        citytemp = City.objects.filter()
        dic['list'] = json.loads(
            serializers.serialize("json", citytemp)
        )
        dic['result_code'] = 200
        dic = json.dumps(dic)
        return HttpResponse(dic)
    else:
        dic['result_code'] = 400
        dic = json.dumps(dic)
        return HttpResponse(dic)

def cityrelation_add(request):
    '''新增城市关系'''
    dic = {}
    if request.method == 'POST':
        if request.POST:
            fathercitytemp = request.POST.get('fathercity')
            soncitytemp = request.POST.get('soncity')
            if City.objects.filter(name = fathercitytemp):
                if City.objects.filter(name = soncitytemp):
                    if Cityrelation.objects.filter(fathercity = fathercitytemp, soncity = soncitytemp):
                        dic['result_code'] = 401
                        dic = json.dumps(dic)
                        return HttpResponse(dic)
                    else:
                        newcityrelation = Cityrelation(fathercity = fathercitytemp, soncity = soncitytemp)
                        newcityrelation.save()
                        dic['result_code'] = 200
                        dic = json.dumps(dic)
                        return HttpResponse(dic)
        else:
            dic['result_code'] = 400
            dic = json.dumps(dic)
            return HttpResponse(dic)

def cityrelation_delete(request):
    '''删除城市关系'''
    dic = {}
    if request.method == 'POST':
        if request.POST:
            fathercitytemp = request.POST.get('fathercity')
            soncitytemp = request.POST.get('soncity')
            delcityrelation = Cityrelation.objects.get(fathercity = fathercitytemp, soncity = soncitytemp)
            delcityrelation.delete()
            dic['result_code'] = 200
            dic = json.dumps(dic)
            return HttpResponse(dic)
    else:
        dic['result_code'] = 400
        dic =json.dumps(dic)
        return HttpResponse(dic)

def cityrelation_update(request):
    '''修改城市关系'''
    dic = {}
    if request.method == 'POST':
        if request.POST:
            fathercitytemp = request.POST.get('fathercity')
            soncitytemp = request.POST.get('soncity')
            fathercitynew = request.POST.get('fathercitynew')
            soncitynew = request.POST.get('soncitynew')
            altercityrelation = Cityrelation.objects.get(fathercity = fathercitytemp, soncity = soncitytemp)
            altercityrelation.fathercity = fathercitynew
            altercityrelation.soncity = soncitynew
            altercityrelation.save()
            dic['result_code'] = 200
            dic = json.dumps(dic)
            return HttpResponse(dic)
        else:
            dic['result_code'] = 400
            dic = json.dumps(dic)
            return HttpResponse(dic)

def cityrelation_view(request):
    '''查看城市关系'''
    dic = {}
    if request.method == 'GET':
        cityrelationtemp = Cityrelation.objects.filter()
        dic['list'] = json.loads(
            serializers.serialize("json", cityrelationtemp)
        )
        dic['result_code'] = 200
        dic = json.dumps(dic)
        return HttpResponse(dic)
    else:
        dic['result_code'] = 400
        dic = json.dumps(dic)
        return HttpResponse(dic)
