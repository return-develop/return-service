from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie
import json, hashlib, time, random, string
from .. import models, tests, const_table
from . import helper, messages

def jrToJson(jr):
    """
    将JsonResponse对象转为Json对象\n
    * **jr** - JsonResponse对象\n
    **返回值**: 对应的Json对象\n
    """
    return json.loads(jr.content.decode('utf8'))

def signup_init(info):
    """
    初始化注册信息\n
    * **info** - 含有注册信息的字典\n
    **返回值**: 填充完整的注册信息的字典\n
    """
    md5 = hashlib.md5()
    md5.update(str(int(time.time())).encode('utf8'))
    salt = ''.join(random.sample(string.ascii_letters + string.digits, 8))
    info['password'] += salt
    md5 = hashlib.md5()
    md5.update(info['password'].encode('utf8'))
    password = md5.hexdigest()
    name_list = [
        '库', '里', '汤', '普', '森', '杜', '兰', '特',
        '格', '林', '科', '尔', '尼', '克', '杨', '麦', '基']
    return {
        'ri': 'http://www.jb51.net/images/logo.gif',
        'rn': (random.choice(name_list) + random.choice(name_list)),
        'rs': 1,
        'salt': salt,
        'email': info['email'],
        'username': info['username'],
        'password': password,
        'sex': info['sex']
        }

def signup(request):
    """
    用户注册\n
    * **request** - 前端发送的请求，包含用户名、邮箱、密码、性别\n
    **返回值**: 包含成功/失败信息的JsonResponse\n
    """
    info = json.loads(request.body.decode('utf8'))
    email = info['email']
    #检查email是否已经存在
    if len(models.User.objects.filter(email = email)) > 0:
       return JsonResponse({'flag': const_table.const.EMAIL_REGISTERED})
    info_dict = signup_init(info)
    try:
        #active_code = helper.get_active_code(email)
        #mySubject = messages.user_active_subject()
        #myMessage = messages.user_active_message(
        #    'http:/localhost:8000%s' % ('/user_active/' + active_code))
        #helper.send_active_email(email, mySubject, myMessage)
        models.User.objects.create(
            username = info_dict['username'], email = email, password = info_dict['password'],
            sex =  info_dict['sex'], salt = info_dict['salt'])
        return JsonResponse({'flag': const_table.const.SUCCESS, 'message': ''})
    except Exception:
        return JsonResponse({'flag': const_table.const.FAIL_SIGN_UP})

def login_helper(info):
    """
    用户登录预处理\n
    * **info** - 包含登录信息的字典\n
    **返回值**: 包含成功/失败信息的列表\n
    """
    try:
        email = info['email']
        password = info['password']
        user = models.User.objects.get(email = email)
        md5 = hashlib.md5()
        password += user.salt
        md5.update(password.encode('utf8'))
        if md5.hexdigest() == user.password:
            #成功
            return (1, user.username)
        else:
            #密码错误
            return (-2, const_table.const.WRONG_PASSWORD)
    except Exception:
        #账号错误
        return (-3, const_table.const.WRONG_ACCOUNT)

def login(request):
    """
    用户登录\n
    * **request** - 前端发送的请求，包含邮箱，密码\n
    **返回值**: 包含成功/失败信息的JsonResponse\n
    """
    info = json.loads(request.body.decode('utf8'))
    code = login_helper(info)
    if code[0] < 1:
        return JsonResponse({'flag': code[1]})
    else:
        request.session['username'] = code[1]
        request.session['email'] = info['email']
        return JsonResponse({'flag': const_table.const.SUCCESS, 'message': ''})

def logout(request):
    """
    用户退出登录\n
    * **request** - 前端发送的请求，包含session\n
    **返回值**: 包含成功/失败信息的JsonResponse\n
    """
    EID = 'username'
    if hasattr(request, 'body'):
        info = json.loads(request.body.decode('utf8'))
    if hasattr(request, 'session') and 'username' in request.session:
        EID = request.session['username']
    else:
        return JsonResponse({'flag': const_table.const.USERNAME_NOT_EXIST})
    del request.session['username']
    return JsonResponse({'flag': const_table.const.SUCCESS, 'message': ''})
