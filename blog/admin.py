from django.contrib import admin
from django.contrib.admin import AdminSite
from .models import Article, Feedback, AdminUser, Blogger
from django.contrib.auth.models import Group


class AdminUserAdmin(admin.ModelAdmin):
	list_display = ['first_name','last_name','email']


admin.site.register(Article)
admin.site.register(AdminUser, AdminUserAdmin)
admin.site.register(Feedback)
admin.site.unregister(Group)


admin.site.site_header = 'Red Eye FM'
admin.site.site_title = 'Red Eye FM'
#admin.site.register(AdminUser, Admins)
