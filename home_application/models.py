# -*- coding: utf-8 -*-

# import from apps here
from __future__ import unicode_literals

# import from lib
from django.db import models

#导入BkUser
from account.models import BkUser




#######奖项所属级别##############
# class AwardLevelType(Enum):
#   COMPANY = '公司'
#   CENTER = '中心'
#   DEPARTMENT = '部门'
#   GROUP = '小组'
#   _KEY_VALUE_REVERSE = skip(True)
LEVEL_TYPE = (
            (1, '公司'),
            (2, '中心'),
            (3, '小组'),
            (4, '部门'),
              )




#########申请表状态#######
# class ApplyFormType(Enum):
#   Undeclared = '未申报'
#   reviewed = '已审核'
#   unaudited = '未审核'
#   passed = '通过'
#   failed = '未通过'
#   awarde = '获奖'
#   not_awarded = '未获奖'
# _KEY_VALUE_REVERSE = skip(True)

AP_STATUS = (
            (1, '未申报'),
            (2, '审核中'),
            (3, '未通过'),
            (4, '已通过'),
            (5, '未获奖'),
            (6, '已获奖'),
              )



########人员身份#########
USER_LEVEL = (
            (1, '可申请人员'),
            (2, '参评人员')
                )



#定义组织列表
class Organization( models.Model ):
    id_organ = models.CharField( max_length = 50,verbose_name = '所属组织')
    organ_id = models.ForeignKey(BkUser, verbose_name = '更新人')

    apply_time = models.DateTimeField(verbose_name = '申报时间')
    
    create_time = models.DateTimeField(
                                       auto_now_add=True, 
                                       verbose_name='创建时间',
                                       null = True
                                       )

    
    class Meta:
        db_table = 'organization'
        
    def __unicode__(self):
        return '%s' % (self.id_organ)

#组织成员
class Organ_User(models.Model):
    organ = models.ForeignKey( Organization, verbose_name = '所属组织')
    # par_name = models.ForeignKey( BkUser , verbose_name = '参评人ID')
    organ_apply = models.CharField(max_length = 50,verbose_name = '申报人员')
    organ_charge = models.CharField(max_length = 50,verbose_name = '负责人员')


#定义奖项表
class Award(models.Model):
    id_award = models.CharField( max_length = 50 , verbose_name = '奖项名称')
    group_award = models.ForeignKey( Organization , verbose_name = '奖项组')
    #奖项级别
    award_level = models.IntegerField(choices=LEVEL_TYPE, verbose_name='奖项级别')
#     award_level = models.CharField(choices=ApplyFormType.to_django_choices('公司'))
    status = models.BooleanField(verbose_name="奖项状态", default=True)

    start_time = models.DateTimeField(verbose_name = '开始时间')
    end_time = models.DateTimeField(verbose_name = '结束时间')

    apply_time = models.DateTimeField(verbose_name = '创建时间')

    create_time = models.DateTimeField(
                                       auto_now_add=True, 
                                       verbose_name='创建时间',
                                       null = True
                                       )
    update_time = models.DateTimeField(
                                       auto_now=True, 
                                       verbose_name = '更新时间',
                                       null = True
                                       )
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
    
    id_apply = models.CharField( max_length = 50 , verbose_name = '申请人/团队')
#    group_apply = models.ManyToManyField(Organization , verbose_name = '申请人所在组织')
    apply_award = models.ForeignKey(Award , verbose_name = '申请奖项')
    #申请表状态
    ap_status = models.IntegerField(choices=AP_STATUS, verbose_name='申请表状态')
    #ap_status = models.CharField(choices=AwardLevelType.to_django_choices('已审核'))
   
    create_time = models.DateTimeField(
                                       auto_now_add=True, 
                                       verbose_name="创建时间",
                                       null = True
                                       )
    update_time = models.DateTimeField(
                                       auto_now=True, 
                                       verbose_name="更新时间",
                                       null = True
                                       )

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
