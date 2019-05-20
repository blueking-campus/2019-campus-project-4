# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplyForm',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ap_status', models.IntegerField(verbose_name='\u7533\u8bf7\u8868\u72b6\u6001', choices=[(1, '\u672a\u7533\u62a5'), (2, '\u5df2\u5ba1\u6838'), (3, '\u672a\u5ba1\u6838'), (4, '\u901a\u8fc7'), (5, '\u672a\u901a\u8fc7'), (6, '\u83b7\u5956'), (7, '\u672a\u83b7\u5956')])),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4', null=True)),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='\u66f4\u65b0\u65f6\u95f4', null=True)),
                ('intro', models.TextField(verbose_name='\u4e8b\u8ff9\u4ecb\u7ecd')),
                ('comments', models.TextField(verbose_name='\u8bc4\u8bed')),
            ],
            options={
                'db_table': 'applyform',
            },
        ),
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('attach_id', models.CharField(max_length=50, verbose_name='\u9644\u4ef6ID')),
                ('attach_path', models.CharField(max_length=255, verbose_name='\u4e91\u7aef\u9644\u4ef6')),
            ],
            options={
                'db_table': 'attachment',
            },
        ),
        migrations.CreateModel(
            name='Award',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('id_award', models.CharField(max_length=50, verbose_name='\u5956\u9879\u540d\u79f0')),
                ('award_level', models.IntegerField(verbose_name='\u5956\u9879\u7ea7\u522b', choices=[(1, '\u516c\u53f8'), (2, '\u4e2d\u5fc3'), (3, '\u5c0f\u7ec4'), (4, '\u90e8\u95e8')])),
                ('status', models.BooleanField(default=True, verbose_name='\u5956\u9879\u72b6\u6001')),
                ('start_time', models.DateTimeField(default='', verbose_name='\u5f00\u59cb\u65f6\u95f4')),
                ('end_time', models.DateTimeField(default='', verbose_name='\u7ed3\u675f\u65f6\u95f4')),
                ('apply_time', models.DateTimeField(default='', verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4', null=True)),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='\u66f4\u65b0\u65f6\u95f4', null=True)),
                ('apply_number', models.IntegerField(verbose_name='\u7533\u8bf7\u4eba\u6570')),
                ('award_number', models.IntegerField(verbose_name='\u83b7\u5956\u4eba\u6570')),
                ('award_condition', models.TextField(verbose_name='\u53c2\u8bc4\u6761\u4ef6')),
            ],
            options={
                'db_table': 'award',
            },
        ),
        migrations.CreateModel(
            name='Organ_User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('organ_apply', models.CharField(max_length=50, verbose_name='\u7533\u62a5\u4eba\u5458')),
                ('organ_charge', models.CharField(max_length=50, verbose_name='\u53c2\u8bc4\u4eba\u5458')),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('id_organ', models.CharField(max_length=50, verbose_name='\u6240\u5c5e\u7ec4\u7ec7')),
                ('apply_time', models.DateTimeField(default='', verbose_name='\u7533\u62a5\u65f6\u95f4')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4', null=True)),
                ('organ_id', models.ForeignKey(verbose_name='\u66f4\u65b0\u4eba', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'organization',
            },
        ),
        migrations.AddField(
            model_name='organ_user',
            name='organ',
            field=models.ForeignKey(verbose_name='\u6240\u5c5e\u7ec4\u7ec7', to='home_application.Organization'),
        ),
        migrations.AddField(
            model_name='award',
            name='group_award',
            field=models.ForeignKey(default='', verbose_name='\u5956\u9879\u7ec4', to='home_application.Organization'),
        ),
        migrations.AddField(
            model_name='applyform',
            name='apply_award',
            field=models.ForeignKey(verbose_name='\u7533\u8bf7\u5956\u9879', to='home_application.Award'),
        ),
        migrations.AddField(
            model_name='applyform',
            name='attachment',
            field=models.ForeignKey(verbose_name='\u9644\u4ef6', to='home_application.Attachment'),
        ),
        migrations.AddField(
            model_name='applyform',
            name='group_apply',
            field=models.ManyToManyField(to='home_application.Organization', verbose_name='\u7533\u8bf7\u4eba\u6240\u5728\u7ec4\u7ec7'),
        ),
        migrations.AddField(
            model_name='applyform',
            name='id_apply',
            field=models.ForeignKey(verbose_name='\u7533\u8bf7\u4ebaID', to=settings.AUTH_USER_MODEL),
        ),
    ]
