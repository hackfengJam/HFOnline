#!/usr/bin/env python
# -*- coding:utf-8 -*-

__Author__ = "HackFun"

import xadmin
from xadmin import views

from .models import EmailVerifyRecord, Banner, UserProfile


# from xadmin.plugins.auth import UserAdmin
# from xadmin.layout import Fieldset, Main, Side, Row
# from django.utils.translation import ugettext as _
#
#
# class UserProfileAdmin(UserAdmin):
#     def get_form_layout(self):
#         if self.org_obj:
#             self.form_layout = (
#                 Main(
#                     Fieldset('',
#                              'username', 'password',
#                              css_class='unsort no_title'
#                              ),
#                     Fieldset(_('Personal info'),
#                              Row('first_name', 'last_name'),
#                              'email'
#                              ),
#                     Fieldset(_('Permissions'),
#                              'groups', 'user_permissions'
#                              ),
#                     Fieldset(_('Important dates'),
#                              'last_login', 'date_joined'
#                              ),
#                 ),
#                 Side(
#                     Fieldset(_('Status'),
#                              'is_active', 'is_staff', 'is_superuser',
#                              ),
#                 )
#             )
#         return super(UserAdmin, self).get_form_layout()


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
    # model_icon = 'fa address-book-o'


class BannerAdmin(object):
    list_display = ['title', 'image', 'url', 'index', 'add_time']
    # 搜索框
    search_fields = ['title', 'image', 'url', 'index']
    # 过滤器
    list_filter = ['title', 'image', 'url', 'index', 'add_time']


# xadmin.site.unregister(UserProfile)
# xadmin.site.register(UserProfile, UserProfileAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(views.CommAdminView, GlobalSettings)
