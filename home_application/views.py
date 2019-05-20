# -*- coding: utf-8 -*-
from account.models import BkUser
from home_application.models import *
from common.mymako import render_mako_context , render_json
from django.db import connection
from datetime import datetime
from celery.worker.job import Request
from django.shortcuts import render_to_response
import json
from django.core.serializers.json import DjangoJSONEncoder

# 开发框架中通过中间件默认是需要登录态的，如有不需要登录的，可添加装饰器login_exempt【装饰器引入from account.decorators import login_exempt】
def home(request):
    """
    首页
    """
    apply_award = Award.objects.all()
    
    prize_record = ApplyForm.objects.filter(ap_status = 6);
#     for item in last_getAward :
#         data.append( {
#                       'organ' : item.id_organ,
#                       'award': item.award.id_award,
#                       'applyTime' : item.applyform.apply_time,
#                       'team' : item.applyform.group_apply,
#                       
#                       })
#     cursor = connection.cursor()
#     cursor.execute("SET foreign_key_checks = 0;")
#     cursor.execute("drop table award;")
#     cursor.execute("SET foreign_key_checks = 1;")
    
    return render_mako_context(request, '/home_application/home.html' , {'apply_award' : apply_award,
                                                                         'prize_record' : prize_record
                                                                         })


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
    review_record = ApplyForm.objects.exclude(ap_status = 1);
    
    return render_mako_context(request, '/home_application/myReview.html',{'review_record' : review_record})


def awards(request):
    """
    系统管理-奖项信息页面
    """
    awards_information = Award.objects.all()
    return render_mako_context(request, '/home_application/awards.html',{"awards_information":awards_information})
    
#    if  query_name == "":
#        awards_information = Award.objects.filter( id_award = query_name)
#    else :
#        awards_information = Award.objects.all()
#    awards_information = Award.objects.filter( id_award = query_name)
#    return render_mako_context(request, '/home_application/awards.html',{"awards_information":awards_information})

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
    #测试输入(2019-5-16)
#     obj = Organization.objects.create( 
#                                  id_organ = "456" , 
#                                  organ_id_id = "1",
#                                  apply_time = "2019-1-1 1:00:00"
#                                  )
#     obj.save();
    organ_information = Organ_User.objects.all()
    
    return render_mako_context(request, '/home_application/OrganManage.html',{'organ_information':organ_information})

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


#我要申报页面奖项信息渲染
def my_apply_award( request ):
    
    apply_award  = str(request.GET.get('apply_award_name'));
    
    apply_award_record = Award.objects.get( id_award = apply_award )
    
    organ_name = apply_award_record.group_award.id_organ
    
    organ_record = Organization.objects.get( id_organ = organ_name )
    
    organ_user_record = Organ_User.objects.get(organ = organ_record)
    
    return render_json({'result': True, 
                        'award_if': apply_award_record.award_condition,
                        'award_level': apply_award_record.award_level,
                        'organ': apply_award_record.group_award.id_organ,
                        'status': apply_award_record.status,
                        'reviewer': organ_user_record.organ_charge,
                        'award_start' : datetime.strftime(apply_award_record.start_time,"%Y-%m-%d %H:%M:%S"),
                        'award_end' : datetime.strftime(apply_award_record.end_time,"%Y-%m-%d %H:%M:%S")
                        })



#我的申请-我要申报按钮
def my_apply(request):
    apply_name = str(request.GET.get('apply_name'))
    introduction = str(request.GET.get('introduction'))
    file_fakepath = str(request.GET.get('file_fakepath'))
    fileName = str(request.GET.get('fileName'))
    award_name = str(request.GET.get('award_name'))
    ap_status = 2

    attachment_record = Attachment.objects.create(
                                                  attach_id = fileName,
                                                  attach_path = file_fakepath
                                                  )
    
    award_record = Award.objects.get( id_award = award_name )
    
    apply_record = ApplyForm.objects.create(
                                            id_apply = apply_name, 
                                            apply_award = award_record,
                                            ap_status = ap_status,
                                            intro = introduction,
                                            attachment = attachment_record
                                            )
    apply_record.save()
    return render_json()


#我的申请-保存按钮（未申报数据的保存）
def my_apply_save(request):
    apply_name = str(request.GET.get('apply_name'))
    introduction = str(request.GET.get('introduction'))
    file_fakepath = str(request.GET.get('file_fakepath'))
    fileName = str(request.GET.get('fileName'))
    award_name = str(request.GET.get('award_name'))
    ap_status = 1

    attachment_record = Attachment.objects.create(
                                                  attach_id = fileName,
                                                  attach_path = file_fakepath
                                                  )
    
    award_record = Award.objects.get( id_award = award_name )
    
    apply_record = ApplyForm.objects.create(
                                            id_apply = apply_name, 
                                            apply_award = award_record,
                                            ap_status = ap_status,
                                            intro = introduction,
                                            attachment = attachment_record
                                            )
    apply_record.save()
    return render_json()

#个人中心-申报查看页面
def apply_award(request):   
     
     apply_award_name  = str(request.GET.get('apply_award_name'))
     apply_name = str(request.GET.get('apply_name'))

     view_award_record = Award.objects.get( id_award = apply_award_name)
     view_apply_record = ApplyForm.objects.get(apply_award = view_award_record, id_apply = apply_name)
     
     return render_json({'result': True, 
                        'award_if': view_award_record.award_condition,
                        'award_status':view_award_record.status,
                        'award_level': view_award_record.get_award_level_display(),
                        'organ': view_award_record.group_award.id_organ,
                        'start_time': datetime.strftime(view_award_record.start_time,"%Y-%m-%d %H:%M:%S"),
                        'end_time' : datetime.strftime(view_award_record.end_time,"%Y-%m-%d %H:%M:%S"),

                        'intro':view_apply_record.intro,
                        'ap_status':view_apply_record.get_ap_status_display(),
                        'comments':view_apply_record.comments
                        })
     
#个人中心-申报编辑渲染页面
def apply_award_edit(request):   
     
     edit_award_name  = str(request.GET.get('edit_award_name'))
     edit_apply_name = str(request.GET.get('edit_apply_name'))

     edit_award_record = Award.objects.get( id_award = edit_award_name)
     edit_apply_record = ApplyForm.objects.get(apply_award = edit_award_record, id_apply = edit_apply_name)
     
     return render_json({'result': True, 
                        'award_if': edit_award_record.award_condition,
                        'award_status':edit_award_record.status,
                        'award_level': edit_award_record.award_level,
                        'organ': edit_award_record.group_award.id_organ,
                        'start_time': datetime.strftime(edit_award_record.start_time,"%Y-%m-%d %H:%M:%S"),
                        'end_time' : datetime.strftime(edit_award_record.end_time,"%Y-%m-%d %H:%M:%S"),

                        'intro':edit_apply_record.intro,
                        'ap_status':edit_apply_record.ap_status,
                        'comments':edit_apply_record.comments
                        })



#个人中心-我的申报-编辑-我要申报按钮
def edit_myApply(request):
     award_name  = str(request.GET.get('edit_award_name'))
     apply_name = str(request.GET.get('edit_apply_name'))
     intro = str(request.GET.get('edit_intro'))
     file_fakepath = str(request.GET.get('file_fakepath'))
     fileName = str(request.GET.get('fileName'))
     ap_status = 2
 
     edit_award_record = Award.objects.get( id_award = award_name)
     obj = ApplyForm.objects.get(apply_award = edit_award_record, id_apply = apply_name)
     
#     obj.id_apply = apply_name
     obj.intro = intro
     obj.ap_status = ap_status
 
     attachment_record = Attachment.objects.create(
                                                   attach_id = fileName,
                                                   attach_path = file_fakepath
                                                   )
 
     obj.attachment = attachment_record
     obj.save();
     
     return render_json()


#个人中心-我的申报-编辑-保存按钮（未申报数据的保存）
def edit_apply_save(request):
    award_name  = str(request.GET.get('save_award_name'))
    apply_name = str(request.GET.get('save_apply_name'))
    intro = str(request.GET.get('save_intro'))
    file_fakepath = str(request.GET.get('file_fakepath'))
    fileName = str(request.GET.get('fileName'))
    ap_status = 1

    edit_award_record = Award.objects.get( id_award = award_name)
    obj = ApplyForm.objects.get(apply_award = edit_award_record, id_apply = apply_name)
    
#    obj.id_apply = apply_name
    obj.intro = intro
    obj.ap_status = ap_status
    attachment_record = Attachment.objects.create(
                                                  attach_id = fileName,
                                                  attach_path = file_fakepath
                                                  )
    obj.attachment = attachment_record


    obj.save();
    
    return render_json()


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

#我的审核——通过按钮
def review_pass( request ):
    
    award_name = str(request.GET.get('award_name'))
    apply_name = str(request.GET.get('apply_name'))
    
    award_record = Award.objects.get(id_award = award_name)
    
    apply_record = ApplyForm.objects.get( 
                                         id_apply = apply_name,
                                         apply_award = award_record
                                         )
    apply_record.ap_status = 4
    apply_record.save()
    
    return render_json()

#我的审核——驳回按钮
def review_reject( request ):
    
    award_name = str(request.GET.get('award_name'))
    apply_name = str(request.GET.get('apply_name'))
    
    award_record = Award.objects.get(id_award = award_name)
    
    apply_record = ApplyForm.objects.get( 
                                         id_apply = apply_name,
                                         apply_award = award_record
                                         )
    apply_record.ap_status = 3
    apply_record.save()
    
    return render_json()

#我的审核——评奖页面渲染
def review_prize( request ) :
    
    apply_award_name  = str(request.GET.get('apply_award_name'))
    apply_name = str(request.GET.get('apply_name'))

    prize_award_record = Award.objects.get( id_award = apply_award_name)
    prize_apply_record = ApplyForm.objects.get(apply_award = prize_award_record, id_apply = apply_name)
     
    return render_json({'result': True, 
                        'award_if': prize_award_record.award_condition,
                        'award_status':prize_award_record.status,
                        'award_level': prize_award_record.get_award_level_display(),
                        'organ': prize_award_record.group_award.id_organ,
                        'start_time': datetime.strftime(prize_award_record.start_time,"%Y-%m-%d %H:%M:%S"),
                        'end_time' : datetime.strftime(prize_award_record.end_time,"%Y-%m-%d %H:%M:%S"),

                        'intro':prize_apply_record.intro,
#                        'ap_status':prize_apply_record.ap_status,
                        'comments':prize_apply_record.comments
                        })
    
#我的审核——评奖页面提交
def review_prize_submit( request ):
    
    prize_award_name  = str(request.GET.get('prize_award_name'))
    prize_apply_name = str(request.GET.get('prize_apply_name'))
    prize_status  = int(request.GET.get('prize_status'))
    comments = str(request.GET.get('comments'))
    
    prize_award_record = Award.objects.get( id_award = prize_award_name)
    
    prize_applyform_record = ApplyForm.objects.get(apply_award = prize_award_record, id_apply = prize_apply_name)
    
    prize_applyform_record.ap_status = prize_status
    prize_applyform_record.comments = comments
    
    prize_applyform_record.save()
    
    return render_json()
   
#系统管理-奖项信息-新增奖项功能
def add_award(request):
    award_name = str(request.GET.get('award_name'))
    organ = str(request.GET.get('organ'))
    award_if = str(request.GET.get('award_if'))
    award_level = (int)(request.GET.get('award_level'))
    start_time = datetime.strptime(str(request.GET.get('start_time')),'%Y-%m-%d&nbsp;%H:%M:%S')
    apply_time = datetime.strptime(str(request.GET.get('apply_time')),'%Y-%m-%d&nbsp;%H:%M:%S')
    end_time = datetime.strptime(str(request.GET.get('end_time')),'%Y-%m-%d&nbsp;%H:%M:%S')
    is_attach = int(request.GET.get('is_attach'))
    status = (request.GET.get('status'))
    apply_number = (int)(request.GET.get('apply_number'))
    award_number = (int)(request.GET.get('award_number'))
    
    
    organ_record = Organization.objects.get(
                                               id_organ = organ
                                               )
    
    award_record = Award.objects.create(
                                         id_award = award_name, 
                                         group_award = organ_record,
                                         award_level = award_level,
                                         status = status,
                                         start_time = start_time,
                                         apply_time = apply_time,
                                         end_time = end_time,
                                         apply_number = apply_number,
                                         award_number = award_number,
                                         award_condition = award_if
                                          )
    
    return render_json()

#系统管理-组织管理-新增组织信息
def new_add_organization(request):
    
    organ = str(request.GET.get('organ'))
    organ_charge = str(request.GET.get('organ_charge'))
    organ_apply = str(request.GET.get('organ_apply'))
    apply_time = datetime.strptime(str(request.GET.get('apply_time')),'%Y-%m-%d&nbsp;%H:%M:%S')
    
    organ_record = Organization.objects.create( 
                                  id_organ = organ , 
                                  organ_id_id = "1",
                                  apply_time = apply_time
                                  )
    organ_record.save();
    
    organ_user_record = Organ_User.objects.create(
                                                  organ = organ_record, 
                                                  organ_apply = organ_apply,
                                                  organ_charge = organ_charge
                                                  )
    organ_user_record.save();
    
    return render_json()
    
    
#系统管理-奖项信息-奖项列表删除功能
def delete_award(request):
    
    award_name = str(request.GET.get('id_award'))
    
    Award.objects.get( id_award = award_name ).delete();
    
    return render_json()
    
 
 
 #奖项编辑-渲染编辑页面
def edit_award(request):   
     
     edit_award_name  = str(request.GET.get('edit_award_name'));
     edit_record = Award.objects.get( id_award = edit_award_name )
     
     return render_json({'result': True, 
                        'award_if': edit_record.award_condition,
                        'award_level': edit_record.award_level,
                        'organ': edit_record.group_award.id_organ,
                        'start_time': datetime.strftime(edit_record.start_time,"%Y-%m-%d %H:%M:%S"),
                        'apply_time': datetime.strftime(edit_record.apply_time,"%Y-%m-%d %H:%M:%S"),
                        'end_time' : datetime.strftime(edit_record.end_time,"%Y-%m-%d %H:%M:%S"),
                        'apply_number': edit_record.apply_number,
                        'award_number': edit_record.award_number,
                        'status': edit_record.status
                        })

#保存编辑数据
def edit_change(request):
    
    
    award_name = str(request.GET.get('award_name'))
    organ = str(request.GET.get('organ'))
    award_if = str(request.GET.get('award_if'))
    award_level = (int)(request.GET.get('award_level'))
    start_time = datetime.strptime(str(request.GET.get('start_time')),'%Y-%m-%d&nbsp;%H:%M:%S')
    apply_time = datetime.strptime(str(request.GET.get('apply_time')),'%Y-%m-%d&nbsp;%H:%M:%S')
    end_time = datetime.strptime(str(request.GET.get('end_time')),'%Y-%m-%d&nbsp;%H:%M:%S')
    is_attach = int(request.GET.get('is_attach'))
    status = (request.GET.get('status'))
    apply_number = (int)(request.GET.get('apply_number'))
    award_number = (int)(request.GET.get('award_number'))
    
    obj = Award.objects.get(id_award = award_name)
    
    group_old = Award.objects.get(id_award = award_name).group_award.id_organ
    group = Organization.objects.get(id_organ = group_old)
    group.id_organ = organ
    group.save()
    
    obj.group_award = group;
    obj.award_level = award_level
    obj.award_condition = award_if
    obj.start_time = start_time
    obj.apply_time = apply_time
    obj.end_time = end_time
    obj.status = status
    obj.award_level = award_level
    obj.apply_number = apply_number
    obj.award_level = award_level

    obj.save();
    
    return render_json()
    
#系统管理-奖项信息-克隆奖项渲染功能
def clone_award(request):   
     
     clone_award_name  = str(request.GET.get('clone_award_name'));
     clone_record = Award.objects.get( id_award = clone_award_name  )
     
     return render_json({'result': True, 
                        'award_if': clone_record.award_condition,
                        'award_level': clone_record.award_level,
                        'organ': clone_record.group_award.id_organ,
                        'start_time': datetime.strftime(clone_record.start_time,"%Y-%m-%d %H:%M:%S"),
                        'apply_time': datetime.strftime(clone_record.apply_time,"%Y-%m-%d %H:%M:%S"),
                        'end_time' : datetime.strftime(clone_record.end_time,"%Y-%m-%d %H:%M:%S"),
                        'apply_number': clone_record.apply_number,
                        'award_number': clone_record.award_number,
                        'status': clone_record.status
                        })

 
 
    
#系统管理-奖项信息-克隆奖项功能
def clone_change(request):
    award_name = str(request.GET.get('award_name'))
    organ = str(request.GET.get('organ'))
    award_if = str(request.GET.get('award_if'))
    award_level = (int)(request.GET.get('award_level'))
    start_time = datetime.strptime(str(request.GET.get('start_time')),'%Y-%m-%d&nbsp;%H:%M:%S')
    apply_time = datetime.strptime(str(request.GET.get('apply_time')),'%Y-%m-%d&nbsp;%H:%M:%S')
    end_time = datetime.strptime(str(request.GET.get('end_time')),'%Y-%m-%d&nbsp;%H:%M:%S')
    is_attach = int(request.GET.get('is_attach'))
    status = (request.GET.get('status'))
    apply_number = (int)(request.GET.get('apply_number'))
    award_number = (int)(request.GET.get('award_number'))
    
    organ_record = Organization.objects.get(
                                               id_organ = organ
                                               )
    
    award_record = Award.objects.create(
                                         id_award = award_name, 
                                         group_award = organ_record,
                                         award_level = award_level,
                                         status = status,
                                         start_time = start_time,
                                         apply_time = apply_time,
                                         end_time = end_time,
                                         apply_number = apply_number,
                                         award_number = award_number,
                                         award_condition = award_if
                                          )
    
    return render_json()   


#奖项查看页面-奖项信息渲染
def check_award( request ):
    
    check_award_name  = str(request.GET.get('check_award_name'));
    check_record = Award.objects.get( id_award = check_award_name )
    
    return render_json({'result': True, 
                        'award_if': check_record.award_condition,
                        'award_level': check_record.award_level,
                        'organ': check_record.group_award.id_organ,
                        'start_time': datetime.strftime(check_record.start_time,"%Y-%m-%d %H:%M:%S"),
                        'end_time': datetime.strftime(check_record.end_time,"%Y-%m-%d %H:%M:%S"),
                        'status': check_record.status,
                        'reviewer':"2376200788"
                        })
    
    return render_json()

def edit_organ_manage(request):
    
    organ = str(request.GET.get('organ'))
    organ_charge = str(request.GET.get('organ_charge'))
    organ_apply = str(request.GET.get('organ_apply'))
    apply_time = datetime.strptime(str(request.GET.get('apply_time')),'%Y-%m-%d&nbsp;%H:%M:%S')
    
    organ_record = Organization.objects.get(id_organ = organ)
    
    organ_manage_record = Organ_User.objects.get(organ = organ_record)
    organ_manage_record.organ_charge = organ_charge
    organ_manage_record.organ_apply = organ_apply
    
    organ_manage_record.save()
    
    organ_record.apply_time = apply_time
    organ_record.save()
    
    
    
    return render_json()

#查询奖项信息
def query_award( request ):
    
    query_name  = str(request.GET.get('query_name'));
#     query_organ  = str(request.GET.get('query_organ'));
#     query_status  = str(request.GET.get('query_status'));
#     #query_apply_time  = str(request.GET.get('query_apply_time'));
# 
    awards_information = Award.objects.filter( id_award = query_name );
#   
    haha = json.dumps(awards_information , cls=DjangoJSONEncoder)
       
    return render_json(
                       {'haha' : haha }
                       );
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    