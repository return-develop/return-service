# Generated by Django 2.1.8 on 2020-06-26 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20200626_0916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='info',
            field=models.CharField(default='', max_length=2048),
        ),
    ]
