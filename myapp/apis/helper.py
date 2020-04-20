#coding:utf-8
'''辅助函数'''
import time
import random
import string
import hashlib
from django.core.mail import EmailMultiAlternatives
from .. import models

def encrypt(key, message):
    """
        字符串加密
    """
    bytearr = bytearray(str(message).encode('utf-8'))
    #求出 b 的字节数
    length = len(bytearr)
    c = bytearray(length * 2)
    j = 0
    for i in range(0, length):
        b1 = bytearr[i]
        b2 = b1 ^ key
        c1 = b2 % 16
        c2 = b2 // 16
        c1 = c1 + 65
        c2 = c2 + 65
        c[j] = c1
        c[j + 1] = c2
        j = j + 2
    return c.decode('utf-8').lower()

def decrypt(key, message):
    """
        字符串解密
    """
    c = bytearray(str(message).upper().encode('utf-8'))
    length = len(c)
    if length % 2 != 0:
        return ""
    length = length // 2
    bytearr = bytearray(length)
    j = 0
    try:
        for i in range(0, length):
            c1 = c[j]
            c2 = c[j + 1]
            j = j + 2
            c1 = c1 - 65
            c2 = c2 - 65
            b2 = c2 * 16 + c1
            b1 = b2 ^ key
            bytearr[i] = b1
        return bytearr.decode('utf-8')
    except Exception:
        return ""

def get_active_code(email):
    """
        获取激活码
    """
    key = 9
    encry_str = '%s|%s' % (email, time.strftime('%Y-%m-%d', time.localtime(time.time())))
    active_code = encrypt(key, encry_str)
    return active_code

def send_active_email(email, userSubject, userMessage):
    """
        发送邮件
    """
    subject = userSubject
    message = userMessage
    send_to = [email]
    #发送异常报错
    fail_silently = False
    msg = EmailMultiAlternatives(subject = subject, body = message, to = send_to)
    msg.attach_alternative(message, "text/html")
    msg.send(fail_silently)

def active_code_check(active_code):
    '''检测激活码'''
    decrypt_str = decrypt(9, active_code)
    decrypt_data = decrypt_str.split('|')
    email = decrypt_data[0]
    user = models.User.objects.filter(email = email)
    if len(user) == 0:
        #链接无效
        return -8
    create_date = time.mktime(time.strptime(decrypt_data[1], "%Y-%m-%d"))
    time_lag = time.time() - create_date
    if time_lag > 3 * 24 * 60 * 60:
        #链接过期
        return -9

def password_add_salt(password):
    '''生成盐'''
    salt = ''.join(random.sample(string.ascii_letters + string.digits, 8))
    password += salt
    md5 = hashlib.md5()
    md5.update(password.encode('utf8'))
    password_encrypyed = md5.hexdigest()
    return {
        'password': password_encrypyed,
        'salt': salt
    }
