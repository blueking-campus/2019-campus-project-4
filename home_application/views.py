# -*- coding: utf-8 -*-
from common.mymako import render_mako_context
#from account.models import BkUser
from .models import Organization
from home_application import models


def orm(request):
    models.Organization.objects.create(id_organ='alex', id_user= '123')

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
    example
    """
    return render_mako_context(request, '/home_application/myApply.html')

def awardApply(request):
    """
    example
    """
    return render_mako_context(request, '/home_application/awardApply.html')

def myReview(request):
    """
    example
    """
    return render_mako_context(request, '/home_application/myReview.html')


