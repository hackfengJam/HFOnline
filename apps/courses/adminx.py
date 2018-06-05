#!/usr/bin/env python
# -*- coding:utf-8 -*-

__Author__ = "HackFun"
__Date__ = '2017/9/11 8:34'

import os
import sys
import uuid
import xlrd

import xadmin

from .models import Course, Lesson, Video, CourseResource, BannerCourse
from organization.models import CourseOrg
from django.db.models import Sum


class LessonInline(object):
    model = Lesson
    extra = 0


class CourseResourceInline(object):
    model = CourseResource
    extra = 0


class VideoInline(object):
    model = Video
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
    # import_excel = True

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
    list_editable = ['name']  # 定义字段是否可以直接修改
    inlines = [VideoInline]

    import_excel = True

    def post(self, request, *args, **kwargs):
        if 'excel' in request.FILES:
            params = request.FILES
            exc = params.get('excel')
            base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            if exc is not None:
                tmp_file_folder = 'courses/tmp_files'

                filename = os.path.join(base_dir, tmp_file_folder + "/" + str(uuid.uuid4()) + '.xls')
                with open(filename, 'wb+') as f:
                    f.writelines(exc.readlines())

                data = xlrd.open_workbook(filename)
                table = data.sheets()[0]  # 打开第一张表
                nrows = table.nrows  # 获取表的行数
                for i in range(nrows):  # 循环逐行打印
                    try:
                        line = table.row_values(i)
                        lesson = Lesson()
                        course = Course.objects.get(id=int(line[1]))
                        if course is not None:
                            lesson.course = course
                        lesson.name = line[0]
                        lesson.save()
                    except Exception as e:
                        pass
                if os.path.exists(filename):  # 删除临时文件
                    os.remove(filename)
        return super(LessonAdmin, self).post(request, args, kwargs)


class VideoAdmin(object):
    # 显示列
    list_display = ['lesson', 'name', 'add_time']
    # 搜索框
    search_fields = ['lesson', 'name']
    # 过滤器
    list_filter = ['lesson', 'name', 'add_time']
    import_excel = True

    def save_models(self):
        obj = self.new_obj
        obj.save()
        if obj.lesson is not None and obj.lesson.course is not None:
            lesson = obj.lesson
            course = lesson.course
            all_lesson = Lesson.objects.filter(course=course).all()
            all_lesson_learn_times = 0
            for i_lesson in all_lesson:
                one_lesson_learn_times = Video.objects.filter(lesson=i_lesson).aggregate(Sum('learn_times')).get(
                    'learn_times__sum', 0)
                one_lesson_learn_times = one_lesson_learn_times if one_lesson_learn_times is not None else 0
                all_lesson_learn_times += one_lesson_learn_times
            course.learn_times = all_lesson_learn_times
            course.save()

    def post(self, request, *args, **kwargs):
        if 'excel' in request.FILES:
            params = request.FILES
            exc = params.get('excel')
            base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            if exc is not None:
                tmp_file_folder = 'courses/tmp_files'

                filename = os.path.join(base_dir, tmp_file_folder + "/" + str(uuid.uuid4()) + '.xls')
                with open(filename, 'wb+') as f:
                    f.writelines(exc.readlines())

                data = xlrd.open_workbook(filename)
                table = data.sheets()[0]  # 打开第一张表
                nrows = table.nrows  # 获取表的行数
                for i in range(nrows):  # 循环逐行打印
                    try:
                        line = table.row_values(i)
                        name, lesson_id, url, learn_times = line
                        video = Video()
                        lesson = Lesson.objects.get(id=int(lesson_id))
                        if lesson is not None:
                            video.lesson = lesson
                        video.name = name
                        video.url = url
                        video.learn_times = int(learn_times)
                        video.save()

                        course = lesson.course
                        all_lesson = Lesson.objects.filter(course=course).all()
                        all_lesson_learn_times = 0
                        for i_lesson in all_lesson:
                            one_lesson_learn_times = Video.objects.filter(lesson=i_lesson).aggregate(
                                Sum('learn_times')).get(
                                'learn_times__sum', 0)
                            one_lesson_learn_times = one_lesson_learn_times if one_lesson_learn_times is not None else 0
                            all_lesson_learn_times += one_lesson_learn_times
                        course.learn_times = all_lesson_learn_times
                        course.save()

                    except Exception as e:
                        pass
                if os.path.exists(filename):  # 删除临时文件
                    os.remove(filename)
        return super(VideoAdmin, self).post(request, args, kwargs)


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
