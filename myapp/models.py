from django.db import models

# Create your models here.
class User(models.Model):
    gender = (
        ('male', '男'),
        ('female', '女'),
    )

    usename = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=256)
    salt = models.CharField(max_length = 8)
    email = models.EmailField(unique=True)
    sex = models.CharField(max_length=32, choices=gender, default='男')
    '''
    birth_date = models.DateField()
    phone = models.CharField(max_length = 128, unique=True)
    graduate_university = models.CharField(max_length=128)
    education = models.CharField(max_length=128)
    desired_position = models.CharField(max_length=128)
    desired_salary = models.CharField(max_length=128)
    '''
    # c_time = models.DateTimeField(auto_now_add=True)
    
    # 人性化显示对象信息
    def __unicode__(self):
        return self.name
