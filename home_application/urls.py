# -*- coding: utf-8 -*-
from django.conf.urls import patterns

urlpatterns = patterns(
    'home_application.views',
    # 首页--your index
    (r'^$', 'home'),
    (r'^dev_guide/$', 'dev_guide'),
    (r'^contact/$', 'contact'),
    (r'^myApply/$', 'myApply'),
    (r'^myReview/$', 'myReview'),
    (r'^awards/$', 'awards'),
    (r'^ApplyAwards/$', 'ApplyAwards'),
    (r'^ReviewAwards/$', 'ReviewAwards'),
    (r'^ApplyCheck/$', 'ApplyCheck'),
    (r'^OrganManage/$', 'OrganManage'),
    (r'^newAddAwards/$', 'newAddAwards'),
    (r'^batchCloning/$', 'batchCloning'),
    (r'^CheckAwards/$', 'CheckAwards'),
    
#我的申请-我要申报按钮
    (r'^my_apply/$', 'my_apply'),
    
#我的申请-查询功能
    (r'^apply_search/$', 'apply_search'),
    
#系统管理-奖项信息-新增奖项功能
    (r'^add_award/$', 'add_award'),
    
#系统管理-组织管理-新增组织信息
    (r'^new_add_organization/$', 'new_add_organization'),
    
#系统管理-奖项信息-奖项列表删除功能
    (r'^delete_award/$', 'delete_award'),
    
#系统管理-奖项信息-渲染编辑页面
    (r'^edit_award/$', 'edit_award'),
    
#保存编辑数据
    (r'^edit_change/$', 'edit_change'),
    
#系统管理-奖项信息-克隆奖项渲染功能
    (r'^clone_change/$', 'clone_change'),
    
#系统管理-奖项信息-克隆奖项功能
    (r'^clone_award/$', 'clone_award'),
    
#奖项查看页面-奖项信息渲染
    (r'^check_award/$', 'check_award'),
    
#查询奖项信息
    (r'^query_award/$', 'query_award'),
)
