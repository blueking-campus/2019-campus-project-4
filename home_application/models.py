# -*- coding: utf-8 -*-

# import from apps here


# import from lib
from __future__ import unicode_literals
from django.db import models

#导入枚举类
import enum
from account.models import BkUser

#定义组织列表
class Organization( models.Model ):
    id_organ = models.CharField( max_length = 50,verbose_name = '组织名称')
    id_user = models.ForeignKey( BkUser , verbose_name = '负责人ID')
    #par_name = models.ForeignKey( BkUser , verbose_name = '参评人ID')
    
    class Meta:
        db_table = 'organization'
        
    def __unicode__(self):
        return '%s' % (self.id_organ)
    

#定义奖励表
class Award(models.Model):
    id_award = models.CharField( max_length = 50 , verbose_name = '奖项名称')
    group_award = models.ManyToManyField( Organization , verbose_name = '奖项组')
    #奖项级别
    level_award = (
                   ('中心级'),
                   ('部门级')
                   )
    status_award = (
                    ('开启'),
                    ('结束')
                    )
    start_time = models.DateTimeField( verbose_name = '开始时间')
    end_time = models.DateTimeField( verbose_name = '结束时间')
    update_time = models.DateTimeField( verbose_name = '更新时间')
    apply_number = models.IntegerField( verbose_name = '申请人数')
    award_number = models.IntegerField( verbose_name = '获奖人数')
    award_condition = models.TextField( verbose_name = '参评条件')
    #对奖项的操作
    operate_award = (
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
    attach_id = models.CharField( max_length = 50 , verbose_name = '附件ID')
    attach_path = models.CharField( max_length = 255,verbose_name = '云端附件' )
    
    class Meta:
        db_table = 'attachment'
        
    def __unicode__(self):
        return '%s' % (self.attach_id)


#定义申请表
class ApplyForm( models.Model):
    id_apply = models.ForeignKey( BkUser , verbose_name = '申请人ID')
    group_apply = models.ManyToManyField( Organization , verbose_name = '申请人所在组织')
    apply_award = models.ManyToManyField( Award , verbose_name = '申请奖项')
    apply_status = (
                   ('未申报'),
                   ('审核中'),
                   ('未通过'),
                   ('已通过'),
                   ('已获奖'),
                   ('未获奖')
                   )
    apply_time = models.DateTimeField( verbose_name = '申报时间')
    operator_apply = (
                   ('申报'),
                   ('编辑'),
                   ('查看'),
                   ('重新申请')
                   )
    introduction = models.TextField( verbose_name = '事迹介绍')
    review_result = (
                   ('未通过'),
                   ('通过'),
                   ('已获奖'),
                   ('未获奖')
                   )
    comments = models.TextField( verbose_name = '评语')
    attachment = models.ForeignKey( Attachment , verbose_name = '附件')
    
    class Meta:
        db_table = 'ApplyForm'
        
    def __unicode__(self):
        return '%s' % (self.id_apply)
