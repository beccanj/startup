from django.contrib import admin

from main.models import Course


admin.site.site_header = "Mke Digi Admin"  # Changes the top-left header
admin.site.site_title = "Mke Digi Admin"  # Changes the title on the browser tab
admin.site.index_title = "Welcome to the Mke Digi Administration"  # Changes the dashboard title
# Register your models here.
admin.site.register(Course)
