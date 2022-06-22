from django.urls import path
from .views import news_view, SettingsView

app_name = 'news'

urlpatterns = [
    path('', news_view, name='news_view'),
    path('settings/', SettingsView.as_view(), name='settings_view'),
]
