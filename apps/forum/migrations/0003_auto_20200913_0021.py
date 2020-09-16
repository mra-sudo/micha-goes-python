# Generated by Django 3.1 on 2020-09-12 22:21

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_auto_20200912_2330'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='posting',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='topic',
            name='publish_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 12, 22, 21, 4, 905436, tzinfo=utc)),
        ),
    ]
