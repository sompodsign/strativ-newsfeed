from django.contrib import admin

from news.models import Settings


@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):
    """
    Admin class for Settings model
    """
    list_display = ('country', 'sources', 'keywords')
