#!/usr/bin/env python
# -*- coding:utf-8 -*-

__Author__ = "HackFun"
__Date__ = '2017/9/11 8:48'

import xadmin

from .models import CourseOrg, CityDict, Teacher


class CityDictAdmin(object):
    # 显示列
    list_display = ['name', 'desc', 'add_time']
    # 搜索框
    search_fields = ['name', 'desc']
    # 过滤器
    list_filter = ['name', 'desc', 'add_time']


class CourseOrgAdmin(object):
    # 显示列
    list_display = ['name', 'desc', 'click_nums', 'fav_nums', 'address', 'city']
    # 搜索框
    search_fields = ['name', 'desc', 'click_nums', 'fav_nums', 'address']
    # 过滤器
    list_filter = ['name', 'desc', 'click_nums', 'fav_nums', 'address']
    relfield_style = 'fk-ajax'


class TeacherAdmin(object):
    # 显示列
    list_display = ['org', 'name', 'work_years', 'work_company',
                    'work_position', 'points', 'click_nums', 'fav_nums', 'add_time']
    # 搜索框
    search_fields = ['org', 'name', 'work_years', 'work_company',
                     'work_position', 'points', 'click_nums', 'fav_nums']
    # 过滤器
    list_filter = ['org', 'name', 'work_years', 'work_company',
                   'work_position', 'points', 'click_nums', 'fav_nums', 'add_time']


xadmin.site.register(CourseOrg, CourseOrgAdmin)
xadmin.site.register(CityDict, CityDictAdmin)
xadmin.site.register(Teacher, TeacherAdmin)
