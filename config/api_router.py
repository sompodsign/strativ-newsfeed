from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from newsfeed.users.api.views import UserViewSet
from news.api.views import ArticleViewSet, NewsSettingViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("news", ArticleViewSet)
router.register("news-settings", NewsSettingViewSet)


app_name = "api"
urlpatterns = router.urls
