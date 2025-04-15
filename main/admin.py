from django.contrib import admin

from main.models import Course, Article

admin.site.site_header = "Agrico Admin"  # Changes the top-left header
admin.site.site_title = "Agricol Admin"  # Changes the title on the browser tab
admin.site.index_title = "Welcome to the Agricol Administration"  # Changes the dashboard title
# Register your models here.
admin.site.register(Course)
admin.site.register(Article)
