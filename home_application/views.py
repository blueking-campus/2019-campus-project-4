# -*- coding: utf-8 -*-
from account.models import BkUser
from home_application.models import *
from common.mymako import render_mako_context , render_json
from sqlalchemy.types import Boolean
from datetime import datetime
from celery.worker.job import Request


# 开发框架中通过中间件默认是需要登录态的，如有不需要登录的，可添加装饰器login_exempt【装饰器引入from account.decorators import login_exempt】
def home(request):
    """
    首页
    """
    data = [];
    last_getAward = Award.objects.all()
    
#     for item in last_getAward :
#         data.append( {
#                       'organ' : item.id_organ,
#                       'award': item.award.id_award,
#                       'applyTime' : item.applyform.apply_time,
#                       'team' : item.applyform.group_apply,
#                       
#                       })
    
    return render_mako_context(request, '/home_application/home.html')


def dev_guide(request):
    """
    开发指引
    """
    return render_mako_context(request, '/home_application/dev_guide.html')


def contact(request):
    """
    联系我们
    """
    return render_mako_context(request, '/home_application/contact.html')

def myApply(request):
    """
    个人中心-我的申请页面
    """
    
    all_record = ApplyForm.objects.all();
    return render_mako_context(request, '/home_application/myApply.html',{'all_record': all_record})

def myReview(request):
    """
    个人中心-我的审核页面
    """
    return render_mako_context(request, '/home_application/myReview.html')


def awards(request):
    """
    系统管理-奖项信息页面
    """
    
    awards_information = Award.objects.all();
    return render_mako_context(request, '/home_application/awards.html',{"awards_information":awards_information})

def ApplyAwards(request):
    """
    首页-查看奖项（我的申请页面下查看申请）
    """
    
    all_record = ApplyForm.objects.all();
    return render_mako_context(request, '/home_application/ApplyAwards.html',{'all_record': all_record})

def ReviewAwards(request):
    """
    我的审核-评奖
    """
    return render_mako_context(request, '/home_application/ReviewAwards.html')

def ApplyCheck(request):
    """
    （我的申请页面下查看）
    """
    
    
    return render_mako_context(request, '/home_application/ApplyCheck.html')


def OrganManage(request):
    """
    （单位管理）
    """
    return render_mako_context(request, '/home_application/OrganManage.html')

def newAddAwards(request):
    """
    系统管理-新增奖项
    """
    return render_mako_context(request, '/home_application/newAddAwards.html')

def batchCloning(request):
    """
    批量克隆
    """
    return render_mako_context(request, '/home_application/batchCloning.html')

def CheckAwards(request):
    """
    查看奖项详情
    """
    return render_mako_context(request, '/home_application/CheckAwards.html')


#我的申请-我要申报按钮
def my_apply(request):
    apply_name = str(request.GET.get('apply_name'))
    introduction = str(request.GET.get('introduction'))
    attachment = str(request.GET.get('attachment'))
    award_name = str(request.GET.get('award_name'))

    
    apply_record = ApplyForm.objects.create(
                                         id_apply = apply_name, 
                                         intro = introduction,
                                         attachment = attachment
                                          )
#     apply_record2 = Award.objects.create(
#                                          id_award = award_name
#                                           )
    
    return render_json({'result': True, 
                        'organ': "BK",
#                         'award': apply_record2.id_award,
                       # 'award_status': awards.status,
                        'apply_name': apply_record.id_apply
                        })

#我的申请-查询功能
def apply_search( request ):
    apply_award = str(request.GET.get('apply_award'))
    apply_status = str(request.GET.get('apply_status'))
    apply_time = str(request.GET.get('apply_time'))
    
    search_record = ApplyForm.objects.all();
    
    return render_json({'result': True, 
                        'organ': "ha",
                        'apply_award': apply_award,
                        'award_status':search_record.apply_award.status,
                        'apply':search_record.id_apply,
                        'apply_status':apply_status,
                        'apply_time':apply_time
                        })
    
#系统管理-奖项信息-新增奖项功能
def add_award(request):
    award_name = str(request.GET.get('award_name'))
    organ = str(request.GET.get('organ'))
    award_if = str(request.GET.get('award_if'))
    award_level = (int)(request.GET.get('award_level'))
    start_time = datetime.strptime(str(request.GET.get('start_time')),'%Y-%m-%d&nbsp;%H:%M:%S')
    apply_time = datetime.strptime(str(request.GET.get('apply_time')),'%Y-%m-%d&nbsp;%H:%M:%S')
    is_attach = int(request.GET.get('is_attach'))
    status = Boolean(request.GET.get('status'))
    apply_number = (int)(request.GET.get('apply_number'))
    award_number = (int)(request.GET.get('award_number'))
    
    organ_record = Organization.objects.create(
                                               id_organ = organ
                                               )
    
    award_record = Award.objects.create(
                                         id_award = award_name, 
                                         group_award = organ_record,
                                         award_level = award_level,
                                         status = status,
                                         start_time = start_time,
                                         end_time = apply_time,
                                         apply_number = apply_number,
                                         award_number = award_number,
                                         award_condition = award_if
                                          )
    
    return render_json()

#系统管理-组织管理-新增组织信息
def new_add_organization(request):
    
    organ = str(request.GET.get('organ'))
    charge_person = str(request.GET.get('charge_person'))
    assessor = str(request.GET.get('assessor'))
    
#    organizaiton_record = 
    
    return render_json()
    
    
#系统管理-奖项信息-奖项列表删除功能
def delete_award(request):
    
    award_name = str(request.GET.get('id_award'))
    
    Award.objects.get( id_award = award_name ).delete();
    
    return render_json()
    
    
    
    