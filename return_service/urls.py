"""return_service URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.views.generic.base import TemplateView
from myapp import views
import sys
sys.path.append("..")
from myapp.apis import user
from myapp import api

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', api.index, name='index'),
    url(r'^user_login/$', TemplateView.as_view(template_name = 'user_login.html')),
    url(r'^user_register/$', TemplateView.as_view(template_name = 'user_register.html')),
    url(r'^user_activate/$', TemplateView.as_view(template_name = 'user_activate.html')),
    url(r'^mycenter/$', TemplateView.as_view(template_name = 'my_center.html')),
    url(r'^home/$', TemplateView.as_view(template_name = 'home_page.html')),
    url(r'^user_info/$', TemplateView.as_view(template_name = 'user_info.html')),
    url(r'^company/$', TemplateView.as_view(template_name = 'company_select.html')),
    path('user_update_password', views.user_update_password),
    path('mailcheck', views.mailcheck),
    path('getback_password', views.getback_password),
    path('user_signup/', user.signup, name = 'signup'),
    path('user_logout/', user.logout, name = 'logout'),
    path('user_update_info', views.user_update_info),
    path('user_view_info', views.user_view_info),
    path('subject_add', views.subject_add),
    path('subject_delete', views.subject_delete),
    path('subject_update', views.subject_update),
    path('subject_view', views.subject_view),
    path('subrelation_add', views.subrelation_add),
    path('subrelation_delete', views.subrelation_delete),
    path('subrelation_update', views.subrelation_update),
    path('subrelation_view', views.subrelation_view),
    path('city_add', views.city_add),
    path('city_detele', views.city_delete),
    path('city_update', views.city_update),
    path('city_view', views.city_view),
    path('cityrelation_add', views.cityrelation_add),
    path('cityrelation_delete', views.cityrelation_delete),
    path('cityrelation_update', views.cityrelation_update),
    path('cityrelation_view', views.cityrelation_view),

    # api
    url(r'^api/findback_password/$', user.logout),  #todo   
    url(r'^api/user/login/$', user.login, name = 'login'),
    url(r'^api/user/signup/$', user.signup, name = 'signup'),
    url(r'^api/user/activate/$', views.mailcheck, name = 'activate'),
    url(r'^api/user/check_activate/$', views.user_activate, name = 'check_activate'),
    url(r'^api/user/findback_password/$', views.getback_password, name = 'findback_password'),
]
