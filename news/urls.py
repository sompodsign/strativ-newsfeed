from django.urls import path
from .views import NewsFeedView, SettingsView

app_name = 'news'

urlpatterns = [
    path('', NewsFeedView.as_view(), name='news_view'),
    path('settings/', SettingsView.as_view(), name='settings_view'),
]
