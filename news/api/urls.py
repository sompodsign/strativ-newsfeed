from django.urls import path
from .views import SourcesView

urlpatterns = [
    path('news/sources/<str:country>', SourcesView.as_view(), name='get_sources'),
]
