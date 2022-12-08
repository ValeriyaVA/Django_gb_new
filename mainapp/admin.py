from django.contrib import admin
from mainapp.models import News, Course, Lesson, CourseTeacher
from django.utils.html import format_html

admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(CourseTeacher)


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'slug', 'deleted')
    list_filter = ('deleted', 'created_at')
    ordering = ('pk',)
    list_per_page = 5
    search_fields = ('title', 'preamble', 'body',)
    actions = ('mark_as_delete',)

    def slug(self, obj):
        return format_html(
            '<a href="{}" target="_blank">{}</a>',
            obj.title.lower().replace(' ', '-'),
            obj.title
        )

    slug.short_description = 'Слаг'

    def mark_as_delete(self, request, queryset):
        queryset.update(deleted=True)

    mark_as_delete.short_description = 'Пометить удаленным'

    def mark_as_undelete(self, request, queryset):
        queryset.update(deleted=False)

    mark_as_undelete.short_description = 'Снять пометку удаления'
#
#
# @admin.register(Course)
# class CourseAdmin(admin.ModelAdmin):
#     list_display = ('name', 'description', 'cost', 'deleted', 'slug')
#     list_per_page = 2
#     list_filter = ('cost', 'deleted', 'created_at',)
#     search_fields = ('name', 'description',)
#     actions = ('mark_as_delete', 'mark_as_undelete',)
#
#     def slug(self, obj):
#         return format_html('<a href="{}" target="_blank">{}</a>',
#                            obj.name.lower().replace(' ', '-'), obj.name
#                            )
#
#     slug.short_description = 'СЛАГ'
#
#     def mark_as_delete(self, request, queryset):
#         queryset.update(deleted=True)
#
#     mark_as_delete.short_description = 'Пометить удаленным'
#
#     def mark_as_undelete(self, request, queryset):
#         queryset.update(deleted=False)
#
#     mark_as_undelete.short_description = 'Снять пометку удаления'
#
#
# @admin.register(Lesson)
# class LessonAdmin(admin.ModelAdmin):
#     list_display = ('num', 'course', 'title', 'description', 'deleted', 'slug')
#     list_per_page = 2
#     list_filter = ('course', 'deleted', 'created_at')
#     search_fields = ('title', 'description',)
#     actions = ('mark_as_delete', 'mark_as_undelete',)
#
#     def slug(self, obj):
#         return format_html('<a href="{}" target="_blank">{}</a>',
#                            obj.title.lower().replace(' ', '-'), obj.title
#                            )
#
#     slug.short_description = 'СЛАГ'
#
#     def mark_as_delete(self, request, queryset):
#         queryset.update(deleted=True)
#
#     mark_as_delete.short_description = 'Пометить удаленным'
#
#     def mark_as_undelete(self, request, queryset):
#         queryset.update(deleted=False)
#
#     mark_as_undelete.short_description = 'Снять пометку удаления'
#
#
# @admin.register(CourseTeacher)
# class CourseTeachersAdmin(admin.ModelAdmin):
#     list_display = ('name_first', 'name_second', 'deleted', 'slug')
#     list_per_page = 2
#     list_filter = ('courses', 'deleted', 'created_at')
#     search_fields = ('name_first', 'name_second',)
#     actions = ('mark_as_delete', 'mark_as_undelete',)
#
#     def slug(self, obj):
#         return format_html('<a href="{}" target="_blank">{}</a>',
#                            obj.name_first.lower().replace(' ', '-'), obj.name_first
#                            )
#
#     slug.short_description = 'СЛАГ'
#
#     def mark_as_delete(self, request, queryset):
#         queryset.update(deleted=True)
#
#     mark_as_delete.short_description = 'Пометить удаленным'
#
#     def mark_as_undelete(self, request, queryset):
#         queryset.update(deleted=False)
#
#     mark_as_undelete.short_description = 'Снять пометку удаления'
