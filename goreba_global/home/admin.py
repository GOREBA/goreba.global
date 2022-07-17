from django.contrib import admin

from home.models import Setting


class SettingAdmin(admin.ModelAdmin):
    list_display = [
        'store_name', 'store_title', 'store_icon', 'store_status', 'updated_at'
    ]


admin.site.register(Setting, SettingAdmin)
