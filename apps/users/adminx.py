#!/usr/bin/env python
# -*- coding:utf-8 -*-

__Author__ = "HackFun"


import xadmin
from xadmin import views


from .models import EmailVerifyRecord, Banner


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = "HF后台管理系统"
    site_footer = "HFOnline"
    menu_style = "accordion"


class EmailVerifyRecordAdmin(object):

    # 显示列
    list_display = ['code', 'email', 'send_type', 'send_time']
    # 搜索框
    search_fields = ['code', 'email', 'send_type']
    # 过滤器
    list_filter = ['code', 'email', 'send_type', 'send_time']


class BannerAdmin(object):

    list_display = ['title', 'image', 'url', 'index', 'add_time']
    # 搜索框
    search_fields = ['title', 'image', 'url', 'index']
    # 过滤器
    list_filter = ['title', 'image', 'url', 'index', 'add_time']


xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
