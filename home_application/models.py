# -*- coding: utf-8 -*-

# import from apps here
from __future__ import unicode_literals

# import from lib
from django.db import models

#导入BkUser
from account.models import BkUser

#定义组织列表
class Organization( models.Model ):
    id_organ = models.CharField( max_length = 50,verbose_name = '组织名称')
    id_user = models.ManyToManyField( BkUser , verbose_name = '负责人ID',default='')
    #par_name = models.ForeignKey( BkUser , verbose_name = '参评人ID')
    
    class Meta:
        db_table = 'organization'
        
    def __unicode__(self):
        return '%s' % (self.id_organ)



#######奖项所属级别##############
level_type = (
            (1, "company"),
            (2, "center"),
            (3, "department"),
            (4, "group")
              )

#########申请表状态#######
ap_status = (
            (1, "Undeclared"),
            (2, "reviewed"),
            (3, "unaudited"),
            (4, "failed"),
            (5, "passed"),
            (6, "awarded"),
            (7, "not_awarded")
              )




    

#定义奖励表
class Award(models.Model):
    id_award = models.CharField( max_length = 50 , verbose_name = '奖项名称')
    group_award = models.ForeignKey( Organization , verbose_name = '奖项组',default='')
    #奖项级别
    award_level = models.IntegerField(choices=level_type, verbose_name='奖项级别',default='1')
    status = models.BooleanField(verbose_name="奖项状态", default=True)

    start_time = models.DateTimeField(verbose_name = '开始时间')
    end_time = models.DateTimeField(verbose_name = '结束时间')
    create_time = models.DateTimeField(auto_now=True, verbose_name='创建时间',null=True)
    update_time = models.DateTimeField(auto_now=True, verbose_name = '更新时间',null=True)
    apply_number = models.IntegerField(verbose_name = '申请人数')
    award_number = models.IntegerField(verbose_name = '获奖人数')
    award_condition = models.TextField(verbose_name = '参评条件')

    class Meta:
        db_table = 'award'
        
    def __unicode__(self):
        return '%s' % (self.id_award)
    
#定义附件表
class Attachment( models.Model):
    attach_id = models.CharField(max_length = 50, verbose_name = '附件ID')
    attach_path = models.CharField(max_length = 255, verbose_name = '云端附件' )
    
    class Meta:
        db_table = 'attachment'
        
    def __unicode__(self):
        return '%s' % (self.attach_id)


#定义申请表
class ApplyForm( models.Model):
    id_apply = models.ForeignKey(BkUser , verbose_name = '申请人ID')
    group_apply = models.ManyToManyField(Organization , verbose_name = '申请人所在组织')
    apply_award = models.ManyToManyField(Award , verbose_name = '申请奖项')
    #申请表状态
    ap_status = models.IntegerField(choices=ap_status, verbose_name='申请表状态',default='')
   
    create_time = models.DateTimeField(auto_now=True, verbose_name="创建时间",null=True)
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间",null=True)

    intro = models.TextField(verbose_name = '事迹介绍')
    # review_result = (
    #                ('未通过'),
    #                ('通过'),
    #                ('已获奖'),
    #                ('未获奖')
    #                )
    comments = models.TextField(verbose_name = '评语')
    attachment = models.ForeignKey(Attachment, verbose_name = '附件')
    
    class Meta:
        db_table = 'applyform'
        
    def __unicode__(self):
        return '%s' % (self.id_apply)
