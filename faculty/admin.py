from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import (
    exam_name,
    department,
    faculty,
    session,
    time,
    duty_type,
    semester
)


@admin.register(exam_name)
class ExamNameAdmin(admin.ModelAdmin):
    list_display = ('exam', 'center_incharge', 'gtu_co', 'sr_sup', 'jr_sup',
                    'st_sup', 'num_sup', 'peon', 'st_peon', 'sweeper', 'page_amount')
    search_fields = ('exam',)


@admin.register(department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('department_name',)
    search_fields = ('department_name',)


@admin.register(faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ('pancard', 'short_name', 'full_name', 'department',
                    'bank_name', 'account_no', 'ifsc', 'is_active')
    list_filter = ('department', 'is_active')
    search_fields = ('pancard', 'short_name', 'full_name', 'account_no')
    list_editable = ('is_active',)


@admin.register(session)
class SessionAdmin(admin.ModelAdmin):
    list_display = ('session',)
    search_fields = ('session',)


@admin.register(time)
class TimeAdmin(admin.ModelAdmin):
    list_display = ('session_id', 'time')
    search_fields = ('session_id',)


@admin.register(duty_type)
class DutyTypeAdmin(admin.ModelAdmin):
    list_display = ('duty',)
    search_fields = ('duty',)


@admin.register(semester)
class SemesterAdmin(admin.ModelAdmin):
    list_display = ('sem',)
    search_fields = ('sem',)