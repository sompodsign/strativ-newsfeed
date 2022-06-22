from django.contrib import admin

from news.models import NewsSetting


@admin.register(NewsSetting)
class SettingsAdmin(admin.ModelAdmin):
    """
    Admin class for Settings model
    """
    list_display = ('country', 'sources', 'keywords')
