# Generated by Django 3.0.2 on 2020-07-04 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=128, unique=True)),
                ('count', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Cityrelation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fathercity', models.CharField(default='', max_length=128)),
                ('soncity', models.CharField(default='', max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=128)),
                ('url', models.CharField(default='', max_length=256)),
                ('bannerurl', models.CharField(default='', max_length=256)),
                ('brief', models.CharField(default='', max_length=128)),
                ('website', models.CharField(default='', max_length=128)),
                ('email', models.EmailField(default='', max_length=254, unique=True)),
                ('phone', models.CharField(default='', max_length=16, unique=True)),
                ('heat', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=128)),
                ('teacher_id', models.IntegerField(default=0)),
                ('time', models.CharField(default='', max_length=128)),
                ('originalprice', models.IntegerField(default=0)),
                ('currentprice', models.IntegerField(default=0)),
                ('info', models.CharField(default='', max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(default='', max_length=254, unique=True)),
                ('course_id', models.IntegerField(default=0)),
                ('status', models.CharField(choices=[('ready', '有效'), ('cancel', '已取消'), ('expire', '已过期')], default='有效', max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=128, unique=True)),
                ('url', models.CharField(default='', max_length=256)),
                ('count', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Subrelation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fathername', models.CharField(default='', max_length=128)),
                ('sonname', models.CharField(default='', max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=128)),
                ('info', models.CharField(default='', max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(default='', max_length=128)),
                ('password', models.CharField(default='', max_length=256)),
                ('salt', models.CharField(default='', max_length=8)),
                ('sex', models.CharField(choices=[('male', '男'), ('female', '女')], default='男', max_length=32)),
                ('birthday', models.CharField(default='', max_length=16)),
                ('phone', models.CharField(default='', max_length=16)),
                ('email', models.EmailField(default='', max_length=254, unique=True)),
                ('realname', models.CharField(default='', max_length=128)),
                ('school', models.CharField(default='', max_length=128)),
                ('major', models.CharField(default='', max_length=128)),
                ('education', models.CharField(default='', max_length=128)),
                ('goal', models.CharField(default='', max_length=128)),
                ('graduate_time', models.CharField(default='', max_length=16)),
                ('city', models.CharField(default='', max_length=128)),
                ('salary', models.CharField(default='', max_length=128)),
                ('info', models.CharField(default='', max_length=256)),
                ('hobby', models.CharField(default='', max_length=256)),
                ('prize', models.CharField(default='', max_length=256)),
                ('skill', models.CharField(default='', max_length=256)),
                ('url', models.CharField(default='', max_length=256)),
                ('isactive', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('company_name', models.CharField(default='', max_length=128)),
                ('name', models.CharField(default='', max_length=128)),
                ('education', models.CharField(default='', max_length=128)),
                ('subject', models.CharField(default='', max_length=128)),
                ('place', models.CharField(default='', max_length=128)),
                ('salary', models.CharField(default='', max_length=128)),
                ('exp', models.CharField(default='', max_length=128)),
                ('info', models.CharField(default='', max_length=8192)),
            ],
        ),
    ]
