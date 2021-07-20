# Generated by Django 3.2.4 on 2021-07-20 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messaging', '0006_alter_chatingroommessage_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='notifications',
            name='seen',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='notifications',
            name='url',
            field=models.CharField(blank=True, max_length=2040, null=True),
        ),
    ]