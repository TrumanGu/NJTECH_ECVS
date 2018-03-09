from django.contrib import admin
from comment.models import Subject, UserInfo, Teacher
# Register your models here.

admin.site.register(Subject)
admin.site.register(Teacher)
admin.site.register(UserInfo)
