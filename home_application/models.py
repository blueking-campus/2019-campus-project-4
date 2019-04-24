# -*- coding: utf-8 -*-

# import from apps here




from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.admin.filters import ChoicesFieldListFilter
from numpy.random.mtrand import choice
from django.db.models.fields import CharField


class user_reward(models.Model):
    user_id = models.IntegerField(verbose_name=u"用户名")
    user_pwd = models.CharField(max_length=30,verbose_name=u"用户密码")
    team = models.CharField(verbose_name=u"团队")
    real_name = models.CharField(verbose_name=u"真实姓名")
    user_age = models.IntegerField(verbose_name=u"年龄")
    post = models.CharField(verbose_name=u"岗位")
    type =(
           (1, u"申请人"),
           (2, u"评委"),
           (3, u"管理员")
           
           )
    levels = models.IntegerField(choices=type,verbose_name = u"操作")
    class Meta:
        db_table = 'user_reward'
    
class admin(models.Model):
    admin_id = models.ForeignKey(user_reward, related_name="user_id",verbose_name = u"管理人员id")
    type = (
            (1, u"编辑")
            (2, u"删除")
            (3, u"查看")
            
            )
    admin_opt = models.IntegerField(choices=type, verbose_name = u"操作")
    
    class Meta:
        da_table = 'admin'

class applicant(models.Model):
    ap_id = models.ForeignKey(user_reward, related_name="user_id", verbose_name = u"申请人id")
    status_type = (
                   (1, u"未申报")
                   (2, u"审核中")
                   (3, u"未审核")
                   (4, u"未通过")
                   (5, u"已通过")
                   (6, u"已获奖")
                   (7, u"未获奖")
                   )
    ap_status = models.IntegerField(choices=status_type, verbose_name=u"状态")
    ap_time = models.DateTimeField(auto_now=True, verbose_name=u"创建时间")
    opt_type = (
                (1, u"申报")
                (2, u"编辑")
                (3, u"重新申请")
                (4, u"查看")
                )
    ap_opt = models.IntegerField(choices=opt_type, verbose_name=u"操作")
    ap_intro = models.TextField(verbose_name=u"事迹介绍")
    ap_annex = models.FileField(upload_to="file/%Y/%m/%d/", verbose_name=u"上传附件", blank=True)
    
    class Meta:
        db_table = u"applicant"
    
    
    
class reviewer(models.Model):
    reviewer_id = models.ForeignKey(user_reward, related_name="user_id", verbose_name=u"评委id")
    result_type = (
                   (1, u"获奖")
                   (2, u"未获奖")
                   )
    result = models.IntegerField(choices=result_type, verbose_name=u"结果")
    comment = models.TextField(verbose_name=u"评语")
    status_type = (
                   (1, u"审核中")
                   (2, u"未审核")
                   (3, u"未通过")
                   (4, u"已通过")
                   )
    approval_status = models.IntegerField(choices=status_type, verbose_name=u"状态")
    opt_type = (
                   (1, u"通过")
                   (2, u"驳回")
                   (3, u"评奖")
                   )
    review_opt = models.IntegerField(choices=opt_type, verbose_name=u"操作")
    
    class Meta:
        db_table = u"reviewer"

class rewards(models.Model):
    reward_id = models.IntegerField(verbose_name = u"奖项编号")
    reward_name = models.CharField(max_length=30, verbose_name=u"奖项名称")
    reward_request = models.TextField(verbose_name=u"奖项要求")
    level_type = (
                   (1, u"公司级")
                   (2, u"中心级")
                   (1, u"部门级")
                   (2, u"小组级")
                   )
    reward_level = models.IntegerField(choices=level_type, verbose_name=u"奖项级别")
    center_name = models.CharField(max_length=30, verbose_name=u"所属中心")
    status_type = (
                   (1, u"生效")
                   (2, u"未生效")
                   )
    status = models.IntegerField(choices=status_type, verbose_name=u"奖项状态")
    start_time = moedels.DateField(verbose_name=u"开始时间")
    end_time = models.DateField(verbose_name=u"结束时间")
    create_time = models.DateTimeField(auto_now=True, verbose_name=u"创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name=u"更新时间")
    opt_type = (
                   (1, u"编辑")
                   (2, u"删除")
                   (3, u"查看")
                   )
    reward_opt = models.IntegerField(choices=opt_type, verbose_name=u"操作")
    replacement_name = models.CharField(max_length=30, verbose_name=u"替换后奖项名称")
    approval_status = models.ForeignKey(reviwer, related_name=approval_status, verbose_name=u"审核状态")
    admin_id = models.ForeignKey(admin_id, related_name="admin_id", verbose_name=u"评委id")
    
    class Meta:
        db_table = u"rewards"

class applied_reward(models.Model):
    reward_id = models.ForeignKey(rewards, related_name="reward_id", verbose_name=u"奖项id")
    ap_id = models.ManyToManyField(applicany, related_name="ap_id", verbose_name=u"申请人id")
    reviewer_id = models.ManyToManyField(reviewer, related_name="reviewer_id", verbose_name=u"评委id")
    
    class Meta:
        db_table = u"applied_reward"