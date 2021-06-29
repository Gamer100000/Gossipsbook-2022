# Generated by Django 3.2.4 on 2021-06-29 16:32

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gossips', '0006_auto_20210629_2231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gossipsmodel',
            name='false',
            field=models.ManyToManyField(blank=True, related_name='false', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='gossipsmodel',
            name='true',
            field=models.ManyToManyField(blank=True, related_name='true', to=settings.AUTH_USER_MODEL),
        ),
    ]
