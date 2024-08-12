# main/admin.py

from django.contrib import admin
from .models import *

admin.site.register(Event)
admin.site.register(News)
admin.site.register(CalendarEvent)
admin.site.register(About)
admin.site.register(Administrator)
#admin.site.register(TeachingStaff)
admin.site.register(Achievement)
#admin.site.register(CoCurricularAward)
admin.site.register(HolidayAssignment)
admin.site.register(JobPosting)
admin.site.register(JobApplication)



@admin.register(TeachingStaff)
class TeachingStaffAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'title', 'subject1', 'subject2', 'order')
    list_editable = ('order',)
    list_filter = ('role',)
    search_fields = ('name', 'title', 'subject1', 'subject2')

@admin.register(BackgroundImage)
class BackgroundImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'is_active', 'order']
    list_editable = ['is_active', 'order']



@admin.register(CoCurricularAward)
class CoCurricularAwardAdmin(admin.ModelAdmin):
    list_display = ['title', 'year']
    list_filter = ['year']