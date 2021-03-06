from django.db import models

# Create your models here.
class User(models.Model):
    gender = (
        ('male', '男'),
        ('female', '女'),
    )
    id = models.AutoField(primary_key = True)
    username = models.CharField(max_length = 128, default = '')
    password = models.CharField(max_length = 256, default = '')
    salt = models.CharField(max_length = 8, default = '')
    sex = models.CharField(max_length = 32, choices = gender, default = '男')
    birthday = models.CharField(max_length = 16, default='')
    phone = models.CharField(max_length = 16, default = '')
    email = models.EmailField(unique = True, default = '')
    realname = models.CharField(max_length = 128, default = '')
    school = models.CharField(max_length = 128, default = '')
    major = models.CharField(max_length = 128, default = '')
    education = models.CharField(max_length =128, default = '')
    goal = models.CharField(max_length = 128, default = '')
    graduate_time = models.CharField(max_length = 16, default='')
    city = models.CharField(max_length = 128, default = '')
    salary = models.CharField(max_length = 128, default = '')
    info = models.CharField(max_length = 256, default = '')
    hobby = models.CharField(max_length = 256, default = '')
    prize = models.CharField(max_length = 256, default = '')
    skill = models.CharField(max_length = 256, default = '')
    url = models.CharField(max_length = 256, default = '')
    isactive = models.BooleanField(default = False)
    
    def __unicode__(self):
        return self.id

class Subject(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 128, unique = True, default = '')
    url = models.CharField(max_length = 256, default = '')
    count = models.IntegerField(default = 0)
    
    def __unicode__(self):
        return self.id
        
class Subrelation(models.Model):
    id = models.AutoField(primary_key = True)
    fathername = models.CharField(max_length = 128, default = '')
    sonname = models.CharField(max_length = 128, default = '')
    
    def __unicode__(self):
        return self.id
        
class City(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 128, unique = True, default = '')
    count = models.IntegerField(default = 0)
    
    def __unicode__(self):
        return self.id
        
class Cityrelation(models.Model):
    id = models.AutoField(primary_key = True)
    fathercity = models.CharField(max_length = 128, default = '')
    soncity = models.CharField(max_length = 128, default = '')
    
    def __unicode__(self):
        return self.id
        
class Work(models.Model):
    id = models.AutoField(primary_key = True)
    company_name = models.CharField(max_length = 128, default = '')
    name = models.CharField(max_length = 128, default = '')
    education = models.CharField(max_length = 128, default = '')
    subject = models.CharField(max_length = 128, default = '')
    place = models.CharField(max_length = 128, default = '')
    salary = models.CharField(max_length = 128, default = '')
    exp = models.CharField(max_length = 128, default = '')
    info = models.CharField(max_length = 8192, default = '')
    
    def __unicode__(self):
        return self.id
        
class Company(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 128, default = '')
    url = models.CharField(max_length = 256, default = '')
    bannerurl = models.CharField(max_length = 256, default = '')
    brief = models.CharField(max_length = 128, default = '')
    website = models.CharField(max_length = 128, default = '')
    email = models.EmailField(unique = True, default = '')
    phone = models.CharField(max_length = 16, unique = True, default = '')
    heat = models.IntegerField(default = 0)
    
    def __unicode__(self):
        return self.id

class Course(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 128, default = '')
    teacher_id = models.IntegerField(default = 0)
    time = models.CharField(max_length = 128, default = '')
    originalprice = models.IntegerField(default = 0)
    currentprice = models.IntegerField(default = 0)
    info = models.CharField(max_length = 256, default = '')

    def __unicode__(self):
        return self.id

class Teacher(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 128, default = '')
    info = models.CharField(max_length = 256, default = '')

    def __unicode__(self):
        return self.id

class Order(models.Model):
    orderstatus = (
        ('ready', '有效'),
        ('cancel', '已取消'),
        ('expire', '已过期'),
    )
    id = models.AutoField(primary_key = True)
    email = models.EmailField(unique = True, default = '')
    course_id = models.IntegerField(default = 0)
    platform = models.CharField(max_length = 128, default = '')
    account = models.CharField(max_length = 128, default = '')
    date = models.CharField(max_length = 128, default = '')
    time = models.CharField(max_length = 128, default = '')
    status = models.CharField(max_length = 32, choices = orderstatus, default = '有效')
    
    def __unicode__(self):
        return self.id
