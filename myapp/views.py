from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.core import serializers
from django.core.mail import send_mail, send_mass_mail, EmailMultiAlternatives
import json, hashlib, time, string
import random, csv
from django.conf import settings
from .models import User
from .models import Subject
from .models import Subrelation
from .models import City
from .models import Cityrelation
from .models import Work

def user_login(request):
    return render(request, 'user_login.html')

def user_update_password(request):
    info = json.loads(request.body.decode('utf8'))
    dic = {}
    emailtemp = info['email']
    oldpwdtemp = info['oldPwd']
    newpwdtemp = info['newPwd']
    if User.objects.filter(email__contains = emailtemp):
        usertemp = User.objects.get(email = emailtemp)
        md5 = hashlib.md5()
        oldpwdtemp += usertemp.salt
        md5.update(oldpwdtemp.encode('utf8'))
        if md5.hexdigest() == usertemp.password:
            alteruser = User.objects.get(email = emailtemp)
            saltnew = ''.join(random.sample(string.ascii_letters + string.digits, 8))
            newpwdtemp += saltnew
            md5 = hashlib.md5()
            md5.update(newpwdtemp.encode('utf8'))
            newpwdtemp = md5.hexdigest()
            alteruser.password = newpwdtemp
            alteruser.salt = saltnew
            alteruser.save()
            flag = 'success'
        else:
            flag = 'password wrong'
    else:
        flag = 'fail'
    dic['flag'] = flag
    dic = json.dumps(dic)
    return HttpResponse(dic)

def getback_password(request):
    """
    找回密码
    """
    password = ''
    info = json.loads(request.body.decode('utf8'))
    dic = {}
    emailtemp = info['email']
    user = User.objects.get(email = emailtemp)
    passwordtemp = ''.join(random.sample(['z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a'], 8))
    res = send_mail('"归来"助力海外学习归国找回密码',str('您的初始密码重置为'+str(passwordtemp)+'，请尽快修改您的密码'),'xmh_119@163.com',[emailtemp])
    if res == 1:
        flag = 'success'
    else:
        flag = 'fail'
    md5 = hashlib.md5()
    md5.update(str(int(time.time())).encode('utf8'))
    salt = ''.join(random.sample(string.ascii_letters + string.digits, 8))
    passwordtemp += salt
    md5 = hashlib.md5()
    md5.update(passwordtemp.encode('utf8'))
    passwordtemp = md5.hexdigest()
    user.password = passwordtemp
    user.salt = salt
    user.save()
    dic['flag'] = flag
    dic = json.dumps(dic)
    return HttpResponse(dic)

def mailcheck(request):
    """
    邮箱验证接口
    """
    info = json.loads(request.body.decode('utf8'))
    dic = {}
    if info != "":
        emailtemp = info["email"]
        messagetemp = info["message"]
        if messagetemp == "user activate":
            if User.objects.filter(email__contains = emailtemp):
                usertemp = User.objects.get(email = emailtemp)
                if usertemp.isactive == False:
                    activate_code = ''.join(random.sample(['z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a'], 5))
                    res = send_mail('"归来"助力海外学习归国邮箱验证',str('您的验证码为'+str(activate_code)),'xmh_119@163.com',[emailtemp])
                    if res == 1:
                        flag = 'success'
                    else:
                        flag = 'fail'
                else:
                    flag = 'email has been actived'
                    activate_code = ''
                dic['flag'] = flag
                dic['activate_code'] = activate_code
                dic = json.dumps(dic)
                return HttpResponse(dic)
            else:
                dic['flag'] = 'email wrong'
                dic['activate_code'] = ''
                dic = json.dumps(dic)
                return HttpResponse(dic)

def user_activate(request):
    """
    用户邮箱验证成功
    """
    info = json.loads(request.body.decode('utf8'))
    dic = {}
    if info != "":
        emailtemp = info["email"]
        isactivatetemp = info["isactivate"]
        if isactivatetemp == "true":
            if User.objects.filter(email__contains = emailtemp):
                usertemp = User.objects.get(email = emailtemp)
                if usertemp.isactive == False:
                    alteruser = User.objects.get(email = emailtemp)
                    alteruser.isactive = True
                    alteruser.save()
                    dic['flag'] = 'success'
                    dic = json.dumps(dic)
                    return HttpResponse(dic)
                else:
                    dic['flag'] = 'email has been actived'
                    dic = json.dumps(dic)
                    return HttpResponse(dic)
            else:
                dic['flag'] = 'fail'
                dic = json.dumps(dic)
                return HttpResponse(dic)


def user_update_info(request):
    '''用户填写或修改个人信息'''
    info = json.loads(request.body.decode('utf8'))['content']
    dic = {}
    if info != "":
        usernametemp = info['username']
        realnametemp = info['realname']
        sextemp = info['sex']
        schooltemp = info['school']
        majortemp = info['major']
        educationtemp = info['education']
        goaltemp = info['goal']
        goaltemp = str(goaltemp).strip('[')
        goaltemp = str(goaltemp).strip(']')
        goaltemp = str(goaltemp).replace(" ","")
        goaltemp = str(goaltemp).replace("'","")
        graduate_timetemp = info['graduate_time']
        citytemp = info['city']
        citytemp = str(citytemp).strip('[')
        citytemp = str(citytemp).strip(']')
        citytemp = str(citytemp).replace(" ","")
        citytemp = str(citytemp).replace("'","")
        salarytemp = info['salary']
        birthdaytemp = info['birthday']
        phonetemp = info['phone']
        emailtemp = info['email']
        hobbytemp = info['hobby']
        prizetemp = info['prize']
        skilltemp = info['skill']
        try:
            alteruser = User.objects.get(email = emailtemp)
            alteruser.username = usernametemp       
            alteruser.realname = realnametemp       
            alteruser.sex = sextemp       
            alteruser.school = schooltemp       
            alteruser.major = majortemp        
            alteruser.education = educationtemp        
            alteruser.goal = goaltemp        
            alteruser.graduate_time = graduate_timetemp       
            alteruser.city = citytemp
            alteruser.salary = salarytemp  
            alteruser.birthday = birthdaytemp       
            alteruser.phone = phonetemp      
            alteruser.hobby = hobbytemp      
            alteruser.prize = prizetemp    
            alteruser.skill = skilltemp
            alteruser.save()
            dic['flag'] = 'success'
            dic = json.dumps(dic)
            return HttpResponse(dic)
        except:
            dic['flag'] = 'fail'
            dic = json.dumps(dic)
            return HttpResponse(dic)
    else:
        dic['flag'] = 'fail'
        dic = json.dumps(dic)
        return HttpResponse(dic)

def user_view_info(request):
    '''用户查看个人信息'''
    info = json.loads(request.body.decode('utf8'))
    dic = {}
    emailtemp = info['email']
    if User.objects.filter(email__contains = emailtemp):
        dic['flag'] = 'success'
        usertemp = User.objects.get(email = emailtemp)
        dic['username'] = usertemp.username
        dic['sex'] = usertemp.sex
        dic['birthday'] = usertemp.birthday
        dic['phone'] = usertemp.phone
        dic['email'] = usertemp.email
        dic['realname'] = usertemp.realname
        dic['school'] = usertemp.school
        dic['major'] = usertemp.major
        dic['education'] = usertemp.education
        dic['goal'] = usertemp.goal.split(",")
        dic['graduate_time'] = usertemp.graduate_time
        dic['city'] = usertemp.city.split(",")
        dic['salary'] = usertemp.salary
        dic['info'] = usertemp.info
        dic['hobby'] = usertemp.hobby
        dic['prize'] = usertemp.prize
        dic['skill'] = usertemp.skill
        dic['url'] = usertemp.url
        dic = json.dumps(dic)
        return HttpResponse(dic)
    else:
        dic['flag'] = 'fail'
        dic = json.dumps(dic)
        return HttpResponse(dic)

def subject_add(request):
    '''新增学科分类'''
    info = json.loads(request.body.decode('utf8'))
    dic = {}
    if info != "":
        nametemp = info['name']
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

def importcsv(request):
    for i in range(1,129):
        csvfile_path = 'C:/Users/XieMinghao/Documents/GitHub/return-service/' + str(i) + '.csv'
        try:
            with open(csvfile_path) as f:
                reader = csv.reader(f)
                for row in reader:
                    Work.objects.create(
                        # field1是字段名，row[0]是csv文件的第1列，以此类推
                        name = row[0],
                        salary = row[1],
                        place = row[2],
                        education = row[3],
                        exp = row[4],
                        company_name = row[5],
                        subject = row[6],
                        info = row[7]
                    )
        except:
            continue