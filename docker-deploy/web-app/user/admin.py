from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from user.models import RSSUser
# Register your models here.

class RSSAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('is_driver',)}),  # 在后台显示 is_driver 字段
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('is_driver',)}),  # 在创建用户时显示 is_driver 字段
    )


admin.site.register(RSSUser, RSSAdmin)