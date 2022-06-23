from django.urls import path

from newsfeed.users.api.views import ChangePasswordView

urlpatterns = [
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),
]
