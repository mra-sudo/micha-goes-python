# Generated by Django 3.1 on 2020-09-14 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0004_auto_20200913_0027'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='author',
            field=models.CharField(default='root', max_length=256),
        ),
    ]
