from django.contrib import admin
from django.contrib.admin import AdminSite
from .models import Article, Feedback, AdminUser, Blogger

class Admins(admin.ModelAdmin):
	list_display = ['first_name','last_name','email']


admin.site.register(Article)
admin.site.register(Feedback)
admin.site.site_header = 'Red Eye FM'
admin.site.site_title = 'Red Eye FM'
#admin.site.register(AdminUser, Admins)
