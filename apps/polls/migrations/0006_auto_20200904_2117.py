# Generated by Django 3.1 on 2020-09-04 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_auto_20200830_1455'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tracking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('klicks', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='poll',
            name='unique_views',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='poll',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
