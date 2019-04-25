# -*- coding: utf-8 -*-

# import from apps here


# import from lib
from django.db import models

#导入枚举类
import enum
from bsddb.test.test_all import verbose
from enum import Enum
from account.qloud.models import models

#定义组织列表
class Organization( models.Model ):
    id = models.CharField( max_length = 50,verbose_name = u"组织名称")
    res_name = models.ForeignKey( BkUser , verbose = u'负责人ID')
    par_name = models.ForeignKey( BkUser , verbose = u'参评人ID')
    
    class Meta:
        db_table = 'Organization'
        
    def __unicode__(self):
        return '%s' % (self.id)
    

#定义奖励表
class Award(models.Model):
    id_award = models.CharField( max_length = 50 , verbose = u'奖项名称')
    group_award = models.ManyToManyField( Organization , verbose = u'奖项组')
    #奖项级别
    level_award = enum(
                       (u'中心级'),
                       (u'部门级')
                       )
    status_award = enum(
                        (u'开启'),
                        (u'结束')
                        )
    start_time = models.DateTimeField( verbose = u'开始时间')
    end_time = models.DateTimeField( verbose = u'结束时间')
    update_time = models.DateTimeField( verbose = u'更新时间')
    apply_number = models.IntegerField( verbose = u'申请人数')
    award_number = models.IntegerField( verbose = u'获奖人数')
    award_condition = models.TextField( verbose = u'参评条件')
    #对奖项的操作
    operate_award = enum(
                       (u'查看'),
                       (u'克隆'),
                       (u'编辑'),
                       (u'删除')
                       )
    
    class Meta:
        db_table = 'Award'
        
    def __unicode__(self):
        return '%s' % (self.id_award)
    
#定义附件表
class Attachment( models.Model):
    attach_id = models.CharField( max_length = 50 , verbose = u'附件ID')
    attach_path = models.CharField( verbose = u'云端附件' )
    
    class Meta:
        db_table = 'Attachment'
        
    def __unicode__(self):
        return '%s' % (self.attach_id)


#定义申请表
class ApplyForm( models.Model):
    id_apply = models.ForeignKey( BkUser , verbose = u'申请人ID')
    group_apply = models.ManyToManyField( Organization , verbose = u'申请人所在组织')
    apply_award = models.ManyToManyField( Award , verbose = u'申请奖项')
    apply_status = enum(
                       (u'未申报'),
                       (u'审核中'),
                       (u'未通过'),
                       (u'已通过'),
                       (u'已获奖'),
                       (u'未获奖')
                       )
    apply_time = models.DateTimeField( verbose = u'申报时间')
    operator_apply = enum(
                       (u'申报'),
                       (u'编辑'),
                       (u'查看'),
                       (u'重新申请')
                       )
    introduction = models.TextField( verbose = u'事迹介绍')
    review_result = enum(
                       (u'未通过'),
                       (u'通过'),
                       (u'已获奖'),
                       (u'未获奖')
                       )
    comments = models.TextField( verbose = u'评语')
    attachment = models.ForeignKey( Attachment , verbose = u'附件')
    
    class Meta:
        db_table = 'ApplyForm'
        
    def __unicode__(self):
        return '%s' % (self.id_apply)
