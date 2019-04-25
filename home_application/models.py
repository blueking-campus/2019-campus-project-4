# -*- coding: utf-8 -*-

# import from apps here


# import from lib
from __future__ import unicode_literals
from django.db import models

#导入枚举类
from enum import Enum
from account.qloud.models import models

#定义组织列表
class Organization( models.Model ):
    id = models.CharField( max_length = 50,verbose_name = '组织名称')
    res_name = models.ForeignKey( BkUser , verbose = '负责人ID')
    par_name = models.ForeignKey( BkUser , verbose = '参评人ID')
    
    class Meta:
        db_table = 'organization'
        
    def __unicode__(self):
        return '%s' % (self.id)
    

#定义奖励表
class Award(models.Model):
    id_award = models.CharField( max_length = 50 , verbose = '奖项名称')
    group_award = models.ManyToManyField( Organization , verbose = '奖项组')
    #奖项级别
    level_award = enum(
                       ('中心级'),
                       ('部门级')
                       )
    status_award = enum(
                        ('开启'),
                        ('结束')
                        )
    start_time = models.DateTimeField( verbose = '开始时间')
    end_time = models.DateTimeField( verbose = '结束时间')
    update_time = models.DateTimeField( verbose = '更新时间')
    apply_number = models.IntegerField( verbose = '申请人数')
    award_number = models.IntegerField( verbose = '获奖人数')
    award_condition = models.TextField( verbose = '参评条件')
    #对奖项的操作
    operate_award = enum(
                       ('查看'),
                       ('克隆'),
                       ('编辑'),
                       ('删除')
                       )
    
    class Meta:
        db_table = 'award'
        
    def __unicode__(self):
        return '%s' % (self.id_award)
    
#定义附件表
class Attachment( models.Model):
    attach_id = models.CharField( max_length = 50 , verbose = '附件ID')
    attach_path = models.CharField( verbose = '云端附件' )
    
    class Meta:
        db_table = 'attachment'
        
    def __unicode__(self):
        return '%s' % (self.attach_id)


#定义申请表
class ApplyForm( models.Model):
    id_apply = models.ForeignKey( BkUser , verbose = '申请人ID')
    group_apply = models.ManyToManyField( Organization , verbose = '申请人所在组织')
    apply_award = models.ManyToManyField( Award , verbose = '申请奖项')
    apply_status = enum(
                       ('未申报'),
                       ('审核中'),
                       ('未通过'),
                       ('已通过'),
                       ('已获奖'),
                       ('未获奖')
                       )
    apply_time = models.DateTimeField( verbose = '申报时间')
    operator_apply = enum(
                       ('申报'),
                       ('编辑'),
                       ('查看'),
                       ('重新申请')
                       )
    introduction = models.TextField( verbose = '事迹介绍')
    review_result = enum(
                       ('未通过'),
                       ('通过'),
                       ('已获奖'),
                       ('未获奖')
                       )
    comments = models.TextField( verbose = '评语')
    attachment = models.ForeignKey( Attachment , verbose = '附件')
    
    class Meta:
        db_table = 'ApplyForm'
        
    def __unicode__(self):
        return '%s' % (self.id_apply)
