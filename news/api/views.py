from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .serializers import ArticleSerializer, NewsSettingSerializer
from ..models import Article, NewsSetting


class ArticleViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def get_queryset(self, *args, **kwargs):
        return self.queryset.filter(owner=self.request.user)

    # add user to Article before saving
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class NewsSettingViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = NewsSetting.objects.all()
    serializer_class = NewsSettingSerializer

    def get_queryset(self, *args, **kwargs):
        return self.queryset.filter(user=self.request.user)
