# Generated by Django 3.2.4 on 2021-06-25 09:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('controls', '0003_auto_20210625_1532'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='falseinformation',
            name='cheater',
        ),
    ]