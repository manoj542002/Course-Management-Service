from django.contrib import admin
from .models import Course

# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'duration', 'created_at', 'video')
    search_fields = ['title', 'description']  
admin.site.register(Course,CourseAdmin)