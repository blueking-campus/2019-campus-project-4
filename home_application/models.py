# -*- coding: utf-8 -*-

# import from apps here


# import from lib

from __future__ import unicode_literals


from django.db import models
from account.models import BkUser
from enum import Enum



#######奖项所属级别##############
# class level_type(Enum):
#     company = 1
#     center = 2
#     department = 3
#     group = 4

level_type = (
            (1, "company"),
            (2, "center"),
            (3, "department"),
            (4, "group")
              )
                   
                   


########奖项相关操作#########
# class award_opt(Enum):
#     award_edit = 1
#     award_delete = 2
#     award_view = 3               
    
award_opt = (
            (1, "award_edit"),
            (2, "award_delete"),
            (3, "award_view")
              )

#########申请表状态#######
# class ap_status(Enum):    
#     Undeclared = 1
#     reviewed = 2
#     unaudited = 3
#     failed = 4
#     passed = 5
#     awarded = 6
#     not_awarded = 7

ap_status = (
            (1, "Undeclared"),
            (2, "reviewed"),
            (3, "unaudited"),
            (4, "failed"),
            (5, "passed"),
            (6, "awarded"),
            (7, "not_awarded")
              )


#########申请人员对申请表相关操作#######
# class ap_opt(Enum):
#     applicant = 1 #申请
#     edit = 2
#     re_ap = 3 #重新申请
#     view = 4

ap_opt = (
          (1, "applicant"),
          (2, "edit"),
          (3, "re_ap"),
          (4, "view")
          )


############评委操作#################
# class review_opt(Enum):
#     ap_pass = 1
#     ap_reject = 2
#     award = 3

review_opt = (
              (1, "ap_pass"),
              (2, "ap_reject"),
              (3, "award")
              )





##############################
#
#账户表                                                            
#名称：Accounts                   
#                           
#功能：将蓝鲸用户表和表中信息关联
#  
##############################

class Accounts(models.Model):
    User_name = models.CharField(max_length=30, verbose_name="用户姓名")
    user_id = models.OneToOneField(
                                   BkUser,
                                   on_delete=models.CASCADE,
                                   primary_key=True,
                                   verbose_name="用户id"
                                   )
    #权限？
    class Meta:
        db_table = 'accounts'

##############################
#
#组织表                                                            
#名称：ORG                   
#                           
#功能：存储所属组织及组织成员  
#  
##############################
class Org(models.Model):
    Org_name = models.CharField(max_length=30, verbose_name="组织名称")
    teammate = models.ManyToManyField(Accounts, verbose_name="组织人员")
    #如何区分申报人员和评委
    create_time = models.DateTimeField(auto_now=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    
    class Meta:
        db_table = 'Org'
        
    def __unicode__(self):
        return "organization name: %s, reviewer: %s, applicant: %s" % (self.Org_name, self.reviewer, self.applicant)
        

##############################
#
#奖项表                                                            
#名称：Award                   
#                           
#功能：存储奖项信息  
#  
##############################

class Awards(models.Model):
    award_name = models.CharField(max_length=30, verbose_name="奖项名称")
    award_request = models.TextField(verbose_name="奖项要求")
    #award_level = models.ForeignKey(level_type, verbose_name="奖项级别")
    award_level = models.IntegerField(choices=level_type, verbose_name="奖项级别")
    org_name = models.OneToOneField(Org, verbose_name="所属中心")
    status = models.BooleanField(verbose_name="奖项状态", default=True)
    
    start_time = models.DateField(verbose_name="开始时间")
    end_time = models.DateField(verbose_name="结束时间")
    create_time = models.DateTimeField(auto_now=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    
    #award_opt = models.ForeignKey(award_opt, verbose_name="奖项操作")
    award_opt = models.IntegerField(choices=award_opt, verbose_name="奖项操作")
  
    replacement_name = models.CharField(max_length=30, verbose_name="替换后奖项名称")
    
    class Meta:
        db_table = "awards"
        ordering = ["-start_time"]
    
    def __unicode__(self):
        return "award name: %s" % (self.award_name)


##############################
#
#附件表                                                            
#名称：attachment                   
#                           
#功能：存储附件
#  
##############################

#定义附件表
class Attachment( models.Model):
    attachment_name = models.CharField( max_length = 50 , verbose_name = "附件ID")
    attachment_path = models.CharField( max_length = 255,verbose_name = "云端附件" )
    
    class Meta:
        db_table = "attachment"
        ordering = ["attachment_name"]

##############################
#
#申报表                                                            
#名称：applicant                   
#                           
#功能：存储申报表信息  
#  
##############################

class Applicant(models.Model):
    ap_id = models.ForeignKey(Accounts, verbose_name="申请人")
    
    #ap_status = models.ForeignKey(ap_status, verbose_name="申请表状态")
    ap_status = models.IntegerField(choices=ap_status, verbose_name="申请表状态")
    
    create_time = models.DateTimeField(auto_now=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    
    ap_intro = models.TextField(verbose_name="事迹介绍")
    
    #ap_opt = models.ForeignKey(ap_opt, verbose_name="操作")
    ap_opt = models.IntegerField(choices=ap_opt, verbose_name="操作")
    attachment = models.ForeignKey(Attachment, verbose_name="附件")
    comment = models.TextField(verbose_name="评语")
    #review_opt = models.ForeignKey(review_opt, verbose_name="操作")
    review_opt = models.IntegerField(choices=review_opt, verbose_name="评委操作")
    
    
    class Meta:
        db_table = "applicant"
    


      