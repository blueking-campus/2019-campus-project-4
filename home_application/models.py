# -*- coding: utf-8 -*-

# import from apps here


# import from lib
from django.db import models
class applicant( models.Model ):
    id_applicant = models.ForeignKey( person , on_delete = models.cascade,verbose_name = '申请人ID')
    company = models.CharField( max_length = 12 , verbose_name = '所属组织')
    apply_status = (
                    (u'0',u'未申请'),
                    (u'1',u'审核中'),
                    (u'2',u'已通过'),
                    (u'3',u'未通过'),
                    (u'4',u'已获奖'),
                    (u'5',u'未获奖')
                    )
    apply_time = models.DateTimeField( auto_now = True , verbose_name = "申请时间")
    id_my_apply = models.ForeignKey( my_apply , on_delete = models.cascade,verbose_name = '申请奖项')
    operate = (
               (u'0',u'申报')
               (u'1',u'编辑')
               (u'2',u'查看')
               (u'3',u'重新申报')
               )
    
    class Meta:
        db_table = "applicatant"

class my_apply :
    introduction = models.TextField( verbose_name = '事迹介绍' , primary_key = True)
    comments = models.CharField( max_length = 100 , verbose_name = '评语', primary_key = True)
    attachment = models.CharField( max_length = 50 , verbose_name = '附件链接', primary_key = True)
    id_my_apply = models.ForeignKey( award , on_delete = models.cascade,verbose_name = '申请奖项名称')

    class Meta:
        db_table = "my_apply"
    
class reviewer( models.Model ):
    id_reviewer = models.ForeignKey( person , on_delete = models.cascade,verbose_name = '审核人ID')
    company = models.CharField( max_length = 12 , verbose_name = '所属组织')
    id_applicatant = models.ForeignKey( applicatant , on_delete = models.cascade,verbose_name = '申请人ID')
    id_my_apply = models.ForeignKey( my_apply , on_delete = models.cascade,verbose_name = '申请奖项')
    review_result = (
                     (u'0',u'通过')
                     (u'1',u'驳回')
                     (u'2',u'评奖')
                     )
    
    
    class Meta:
        db_table = "reviewer"
        
class participant( models.Model ):
    id_participant = models.CharField( max_length = 12 , verbose_name = '参评人员ID' , primary_key = True)
    company = models.CharField( max_length = 12 , verbose_name = '所属组织')
    id_my_apply = models.ForeignKey( my_apply , on_delete = models.cascade,verbose_name = '申请奖项')
    
 
    class Meta:
        db_table = "participant"
        
class person( models.Model ):
    id_person = models.CharField( max_length = 12 , verbose_name = '人员ID' , primary_key = True)
    company = models.CharField( max_length = 12 , verbose_name = '所属组织')
    email = models.CharField( max_length = 20 , verbose_name = '邮箱')
    team = models.CharField( max_length = 20 , verbose_name = '团队')
    
    class Meta:
        db_table = "person"

class award( models.Model ):
    id_award = models.CharField( max_length = 20 , verbose_name = '申请奖项名称' , primary_key = True)
    award_company = models.CharField( max_length = 12 , verbose_name = '奖项所属组织')
    award_status = (
             (u'0',u'开始')
             (u'1',u'结束')
             )
    award_level = (
             (u'0',u'中心级')
             (u'1',u'部门级')
             )
    start_time = models.DateTimeField( auto_now = True , verbose_name = "开始时间")
    apply_time = models.DateTimeField( auto_now = True , verbose_name = "申请时间")
    apply_number = models.IntegerField( verbose_name = "申请人数" )
    award_number = models.IntegerField( verbose_name = "获奖人数" )
    
    class Meta:
        db_table = "award"
