# -*- coding: utf-8 -*-
from common.mymako import render_mako_context
from account.models import BkUser
from .models import Organization


# 开发框架中通过中间件默认是需要登录态的，如有不需要登录的，可添加装饰器login_exempt【装饰器引入from account.decorators import login_exempt】
def home(request):
    """
    首页
    """
    data = [];
    last_getAward = Organization.objects.all()
    
    for item in last_getAward :
        data.append( {
                      'organ' : item.id_organ,
                      'award': item.award.id_award,
                      'applyTime' : item.applyform.apply_time,
                      'team' : item.applyform.group_apply,
                      
                      })
    
    return render_mako_context(request, '/home_application/home.html',{'data':data})


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
    return render_mako_context(request, '/home_application/myApply.html')

def myReview(request):
    """
    个人中心-我的审核页面
    """
    return render_mako_context(request, '/home_application/myReview.html')


def awards(request):
    """
    系统管理-奖项信息页面
    """
    return render_mako_context(request, '/home_application/awards.html')

def ApplyAwards(request):
    """
    首页-查看奖项（我的申请页面下查看申请）
    """
    return render_mako_context(request, '/home_application/ApplyAwards.html')

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


#首页申请功能
def my_apply(request):
    apply_name = str(request.GET.get('apply_name'))
    introduction = str(request.GET.get('introduction'))
    attachment = str(request.GET.get('attachment'))
    
    apply_record = ApplyForm.objects.create(
                                         id_apply = apply_name, 
                                         intro = introduction,
                                         attachment = attachment
                                          )
    
    return render_json()
    
