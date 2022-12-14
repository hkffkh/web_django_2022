# Generated by Django 3.2 on 2022-09-06 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Scene',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='场景名称')),
                ('engname', models.CharField(max_length=100, verbose_name='场景英文简称')),
                ('img_url', models.ImageField(blank=True, max_length=255, null=True, upload_to='scene', verbose_name='场景图片')),
                ('intro', models.TextField(verbose_name='场景介绍')),
            ],
            options={
                'verbose_name': '地点场景',
                'verbose_name_plural': '地点场景',
                'db_table': 'scene',
            },
        ),
    ]
