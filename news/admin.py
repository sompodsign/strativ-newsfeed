from django.contrib import admin

from news.models import NewsSetting, Article


@admin.register(NewsSetting)
class SettingsAdmin(admin.ModelAdmin):
    """
    Admin class for Settings model
    """
    list_display = ('country', 'sources', 'keywords')


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    """
    Admin class for Article model
    """
    list_display = ('title', 'thumbnail', 'url', 'sources', 'country', 'owner')
