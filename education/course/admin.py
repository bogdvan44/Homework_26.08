from django.contrib import admin

from .models import Author, Course, Topic


admin.site.register(Author)
admin.site.register(Course)
admin.site.register(Topic)

