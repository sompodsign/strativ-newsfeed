from django.urls import path
from .views import news_view

app_name = 'news'

urlpatterns = [
    path('', news_view, name='news_view'),
    # path('settings/', NewsSettingsView.as_view(), name='settings_view'),
]
