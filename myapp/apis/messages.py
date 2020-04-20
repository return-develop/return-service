def user_active_message(url):
    return u'''
        <h2>用户(<a href="http://localhost:8000/" target="_blank">localhost</a>)</h2><br>
        <p>欢迎注册，请点击下面链接进行激活操作(7天后过期)：<a href="%s" target="_blank">%s</a></p>
        ''' % (url, url)

def user_active_subject():
    return u'用户账号激活'

def reset_password_message(url):
    return u'''
        <h2>用户(<a href="localhost:8000/" target="_blank">localhost</a>)</h2><br>
        <p>您正在试图重置密码，若不是本人操作，请忽略此邮件。点击下面链接进行重置操作(3天后过期)：
        <a href="%s" target="_blank">%s</a></p>
        ''' % (url, url)
