#!/usr/bin/env python
# -*- coding:utf-8 -*-

__Author__ = "HackFun"
__Date__ = '2017/9/11 8:34'

import xadmin

from .models import Course, Lesson, Video, CourseResource, BannerCourse
from organization.models import CourseOrg


class LessonInline(object):
    model = Lesson
    extra = 0


class CourseResourceInline(object):
    model = CourseResource
    extra = 0


class CourseAdmin(object):
    # 显示列
    list_display = ['name', 'desc', 'detail', 'degree', 'learn_times', 'get_zj_nums',
                    # 'go_to',
                    'students', 'fav_nums', 'click_nums']
    # 搜索框
    search_fields = ['name', 'desc', 'detail', 'degree', 'learn_times',
                     'students', 'fav_nums', 'image', 'click_nums']
    # 过滤器
    list_filter = ['name', 'desc', 'detail', 'degree', 'learn_times',
                   'students', 'fav_nums', 'image', 'click_nums', 'add_time']
    ordering = ['-click_nums']
    readonly_fields = ['click_nums']
    list_editable = ['degree', 'desc']  # 定义字段是否可以直接修改
    exclude = ['fav_nums']
    inlines = [LessonInline, CourseResourceInline]
    # refresh_times = [3, 5]  # 可以选择每几秒刷新一次也没
    import_excel = True

    def queryset(self):
        qs = super(CourseAdmin, self).queryset()
        qs = qs.filter(is_banner=False)
        return qs

    def save_models(self):
        # 在保存课程的时候统计课程机构的课程数
        obj = self.new_obj
        obj.save()
        if obj.course_org is not None:
            course_org = obj.course_org
            course_org.course_nums = Course.objects.filter(course_org=course_org).count()
            course_org.save()

    def post(self, request, *args, **kwargs):
        if 'excel' in request.FILES:  # TODO
            pass
        return super(CourseAdmin, self).post(request, args, kwargs)


class BannerCourseAdmin(object):
    # 显示列
    list_display = ['name', 'desc', 'detail', 'degree', 'learn_times',
                    'students', 'fav_nums', 'image', 'click_nums', 'add_time']
    # 搜索框
    search_fields = ['name', 'desc', 'detail', 'degree', 'learn_times',
                     'students', 'fav_nums', 'image', 'click_nums']
    # 过滤器
    list_filter = ['name', 'desc', 'detail', 'degree', 'learn_times',
                   'students', 'fav_nums', 'image', 'click_nums', 'add_time']
    ordering = ['-click_nums']
    readonly_fields = ['click_nums']
    exclude = ['fav_nums']
    inlines = [LessonInline, CourseResourceInline]

    def queryset(self):
        qs = super(BannerCourseAdmin, self).queryset()
        qs = qs.filter(is_banner=True)
        return qs


class LessonAdmin(object):
    # 显示列
    list_display = ['course', 'name', 'add_time']
    # 搜索框
    search_fields = ['course', 'name']
    # 过滤器
    list_filter = ['course__name', 'name', 'add_time']


class VideoAdmin(object):
    # 显示列
    list_display = ['lesson', 'name', 'add_time']
    # 搜索框
    search_fields = ['lesson', 'name']
    # 过滤器
    list_filter = ['lesson', 'name', 'add_time']


class CourseResourceAdmin(object):
    # 显示列
    list_display = ['course', 'name', 'download', 'add_time']
    # 搜索框
    search_fields = ['course', 'name', 'download']
    # 过滤器
    list_filter = ['course', 'name', 'download', 'add_time']


xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(BannerCourse, BannerCourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)
